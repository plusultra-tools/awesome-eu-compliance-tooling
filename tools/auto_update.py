"""Auto-update tooling for the awesome-eu-compliance-tooling list.

Stdlib only. No third-party deps. Python 3.10+.

Subcommands:
  scrape     - fetch GitHub trending and emit JSON to stdout
  lintcheck  - check links and emit removal proposals
  propose    - emit a Markdown PR body with additions+removals
  apply      - no-op in v1 (manual operator review)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, asdict
from html.parser import HTMLParser
from typing import Iterable

# ---------------------------------------------------------------------------
# Module constants
# ---------------------------------------------------------------------------

USER_AGENT = "awesome-eu-compliance-tooling-bot/0.1 (+https://github.com/plusultra-tools/awesome-eu-compliance-tooling)"

GITHUB_TRENDING_URLS: dict[str, str] = {
    "python_weekly": "https://github.com/trending/python?since=weekly&spoken_language_code=en",
    "python_monthly": "https://github.com/trending/python?since=monthly&spoken_language_code=en",
    "go_weekly": "https://github.com/trending/go?since=weekly&spoken_language_code=en",
    "typescript_weekly": "https://github.com/trending/typescript?since=weekly&spoken_language_code=en",
    "rust_weekly": "https://github.com/trending/rust?since=weekly&spoken_language_code=en",
    "all_weekly": "https://github.com/trending?since=weekly&spoken_language_code=en",
}

EU_KEYWORDS: list[str] = [
    "GDPR", "EHDS", "CRA", "AI Act", "NIS2", "DORA",
    "MDR", "IVDR", "DPIA", "compliance", "ENISA", "EUR-Lex",
]

# Awesome-list bullet pattern: "- [name](url) - description"
BULLET_RE = re.compile(
    r"^\s*[-*]\s+\[(?P<name>[^\]]+)\]\((?P<url>[^)]+)\)\s*(?:[-—–:]\s*(?P<desc>.+))?$"
)
SECTION_RE = re.compile(r"^##\s+(?P<title>.+?)\s*$")


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class ScrapedRepo:
    repo: str
    url: str
    description: str
    stars_today: str
    license_hint: str


@dataclass(frozen=True)
class ReadmeEntry:
    section: str
    name: str
    url: str
    description: str


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

def _open(url: str, method: str = "GET", timeout: float = 10.0):
    req = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT})
    return urllib.request.urlopen(req, timeout=timeout)


def check_link(url: str, timeout: float = 10.0) -> tuple[int, str, int]:
    """GET-with-HEAD-fallback link check.

    Returns (status, last_modified, content_length). On any failure, returns
    (0, "", 0) — never raises.
    """
    # Try HEAD first (cheap)
    try:
        with _open(url, method="HEAD", timeout=timeout) as resp:
            status = getattr(resp, "status", 200)
            lm = resp.headers.get("Last-Modified", "") or ""
            cl_raw = resp.headers.get("Content-Length", "0") or "0"
            try:
                cl = int(cl_raw)
            except ValueError:
                cl = 0
            return status, lm, cl
    except urllib.error.HTTPError as e:
        if e.code != 405:
            # 4xx/5xx other than method-not-allowed: report and skip GET
            return e.code, "", 0
        # 405 fall through to GET
    except (urllib.error.URLError, TimeoutError, OSError):
        # network error; fall through to GET (some servers reject HEAD via TCP reset)
        pass

    try:
        with _open(url, method="GET", timeout=timeout) as resp:
            status = getattr(resp, "status", 200)
            lm = resp.headers.get("Last-Modified", "") or ""
            cl_raw = resp.headers.get("Content-Length", "0") or "0"
            try:
                cl = int(cl_raw)
            except ValueError:
                cl = 0
            return status, lm, cl
    except urllib.error.HTTPError as e:
        return e.code, "", 0
    except (urllib.error.URLError, TimeoutError, OSError):
        return 0, "", 0


# ---------------------------------------------------------------------------
# Trending scraper (HTML parser)
# ---------------------------------------------------------------------------

class _TrendingParser(HTMLParser):
    """Parse github.com/trending HTML.

    The site renders one <article class="Box-row"> per repo. We extract:
      - repo slug (owner/name) from the <h2>/<h1> > <a href="/owner/name">
      - description from the first <p> in the article
      - stars-today from <span> matching "N stars today"
      - language/license hints: there's a <span itemprop="programmingLanguage"> and
        sometimes a license <span>; treat gracefully if absent.
    """

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.repos: list[ScrapedRepo] = []
        self._in_article = False
        self._article_depth = 0
        self._cur_repo = ""
        self._cur_url = ""
        self._cur_desc_parts: list[str] = []
        self._cur_stars_today = ""
        self._cur_license = ""
        self._capture: str | None = None  # "desc" | "stars_today" | "license" | None
        self._h_seen = False  # the first <a> after <h1>/<h2> is the repo link

    # --- helpers -----------------------------------------------------------

    def _reset_article(self) -> None:
        self._cur_repo = ""
        self._cur_url = ""
        self._cur_desc_parts = []
        self._cur_stars_today = ""
        self._cur_license = ""
        self._capture = None
        self._h_seen = False

    def _flush(self) -> None:
        if self._cur_repo and self._cur_url:
            self.repos.append(ScrapedRepo(
                repo=self._cur_repo,
                url=self._cur_url,
                description=" ".join(self._cur_desc_parts).strip(),
                stars_today=self._cur_stars_today.strip(),
                license_hint=self._cur_license.strip(),
            ))
        self._reset_article()

    # --- HTMLParser hooks --------------------------------------------------

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = dict(attrs)
        cls = attr.get("class", "") or ""

        if tag == "article" and "Box-row" in cls:
            if self._in_article:
                # nested? flush previous defensively
                self._flush()
            self._in_article = True
            self._article_depth = 1
            return

        if not self._in_article:
            return

        if tag == "article":
            self._article_depth += 1

        if tag in ("h1", "h2"):
            self._h_seen = True
            return

        if tag == "a" and self._h_seen and not self._cur_repo:
            href = attr.get("href", "") or ""
            # Trending repo links look like "/owner/repo"
            if href.startswith("/") and href.count("/") == 2 and "?" not in href:
                slug = href.lstrip("/")
                self._cur_repo = slug
                self._cur_url = f"https://github.com{href}"
            return

        if tag == "p" and not self._cur_desc_parts:
            self._capture = "desc"
            return

        if tag == "span":
            # heuristic: "stars today" lives in a span; license sometimes in a span
            # we capture text and post-filter in handle_data
            if self._capture is None:
                self._capture = "span_generic"
            return

    def handle_endtag(self, tag: str) -> None:
        if not self._in_article:
            return
        if tag == "article":
            self._article_depth -= 1
            if self._article_depth <= 0:
                self._in_article = False
                self._flush()
            return
        if tag in ("h1", "h2"):
            self._h_seen = False
        if tag == "p":
            if self._capture == "desc":
                self._capture = None
        if tag == "span":
            if self._capture == "span_generic":
                self._capture = None

    def handle_data(self, data: str) -> None:
        if not self._in_article or not data.strip():
            return
        if self._capture == "desc":
            self._cur_desc_parts.append(data.strip())
        elif self._capture == "span_generic":
            txt = data.strip()
            low = txt.lower()
            if "star" in low and "today" in low and not self._cur_stars_today:
                self._cur_stars_today = txt
            elif any(lic in txt for lic in ("MIT", "Apache", "BSD", "GPL", "MPL", "ISC", "Unlicense")):
                if not self._cur_license:
                    self._cur_license = txt


def scrape_github_trending(language: str = "python", topic: str = "weekly") -> list[dict]:
    """Fetch and parse GitHub trending. Returns list of dicts.

    Degrades gracefully: on network or parse error returns [].
    """
    base = f"https://github.com/trending/{language}?since={topic}&spoken_language_code=en"
    try:
        with _open(base, timeout=15.0) as resp:
            html = resp.read().decode("utf-8", errors="replace")
    except Exception:
        return []

    parser = _TrendingParser()
    try:
        parser.feed(html)
        parser.close()
    except Exception:
        # malformed HTML; return whatever we managed to collect
        pass

    return [asdict(r) for r in parser.repos]


# ---------------------------------------------------------------------------
# README parser
# ---------------------------------------------------------------------------

def parse_readme_sections(readme_path: str | None = None, *, text: str | None = None) -> list[tuple[str, str, str, str]]:
    """Extract awesome-list entries grouped by ## section.

    Returns list of (section, name, url, description) tuples.
    Either readme_path or text must be provided.
    """
    if text is None:
        if readme_path is None:
            raise ValueError("readme_path or text required")
        with open(readme_path, "r", encoding="utf-8") as f:
            text = f.read()

    out: list[tuple[str, str, str, str]] = []
    current_section = ""
    in_toc = False
    for line in text.splitlines():
        stripped = line.strip()
        # Detect a TOC heading and skip its bullets (they link to anchors, not repos)
        if stripped.startswith("##"):
            m = SECTION_RE.match(stripped)
            if m:
                title = m.group("title").strip()
                current_section = title
                in_toc = title.lower() in ("contents", "table of contents", "toc")
                continue
        if in_toc:
            continue
        if not current_section:
            continue
        m = BULLET_RE.match(line)
        if not m:
            continue
        name = m.group("name").strip()
        url = m.group("url").strip()
        # Skip anchor-only links (toc-ish stragglers)
        if url.startswith("#"):
            continue
        desc = (m.group("desc") or "").strip()
        out.append((current_section, name, url, desc))
    return out


# ---------------------------------------------------------------------------
# Diff: additions / removals
# ---------------------------------------------------------------------------

def _normalize_url(u: str) -> str:
    u = u.strip().rstrip("/")
    if u.startswith("http://"):
        u = "https://" + u[len("http://"):]
    return u.lower()


def propose_additions(
    scraped: Iterable[dict],
    current: Iterable[tuple[str, str, str, str]],
    eu_keywords: Iterable[str] = tuple(EU_KEYWORDS),
) -> list[dict]:
    """Return scraped repos that (a) are not already in current, (b) match a keyword."""
    current_urls = {_normalize_url(e[2]) for e in current}
    kws = [k.lower() for k in eu_keywords]
    additions: list[dict] = []
    for r in scraped:
        url = _normalize_url(r.get("url", ""))
        if not url or url in current_urls:
            continue
        haystack = (r.get("description", "") + " " + r.get("repo", "")).lower()
        if not any(k in haystack for k in kws):
            continue
        additions.append(dict(r))
    return additions


def propose_removals(
    current: Iterable[tuple[str, str, str, str]],
    max_age_days: int = 540,
    *,
    link_checker=check_link,
) -> list[dict]:
    """Return entries whose URL 404s or whose Last-Modified is older than max_age_days."""
    import email.utils
    import time

    now = time.time()
    removals: list[dict] = []
    for section, name, url, desc in current:
        status, last_modified, _cl = link_checker(url)
        reason = ""
        if status == 0 or status >= 400:
            reason = f"http_status={status}"
        elif last_modified:
            try:
                parsed = email.utils.parsedate_to_datetime(last_modified)
                age_days = (now - parsed.timestamp()) / 86400.0
                if age_days > max_age_days:
                    reason = f"stale {int(age_days)}d > {max_age_days}d"
            except (TypeError, ValueError):
                pass
        if reason:
            removals.append({
                "section": section, "name": name, "url": url,
                "description": desc, "reason": reason,
            })
    return removals


# ---------------------------------------------------------------------------
# PR body emitter
# ---------------------------------------------------------------------------

def emit_pr_body(additions: list[dict], removals: list[dict], run_id: str) -> str:
    lines: list[str] = []
    lines.append(f"# Auto-update proposal — run `{run_id}`")
    lines.append("")
    lines.append("This PR was generated by `tools/auto_update.py`. A maintainer must")
    lines.append("review every line before merging. Awesome-list quality is not negotiable.")
    lines.append("")

    lines.append("## Proposed additions")
    if not additions:
        lines.append("")
        lines.append("_None this run._")
    else:
        lines.append("")
        lines.append("| Repo | Description | Stars (period) | License hint |")
        lines.append("|------|-------------|----------------|--------------|")
        for a in additions:
            repo = a.get("repo", "")
            url = a.get("url", "")
            desc = (a.get("description", "") or "").replace("|", "\\|")
            stars = a.get("stars_today", "")
            lic = a.get("license_hint", "")
            lines.append(f"| [{repo}]({url}) | {desc} | {stars} | {lic} |")
    lines.append("")

    lines.append("## Proposed removals")
    if not removals:
        lines.append("")
        lines.append("_None this run._")
    else:
        lines.append("")
        lines.append("| Section | Entry | URL | Reason |")
        lines.append("|---------|-------|-----|--------|")
        for r in removals:
            section = r.get("section", "")
            name = r.get("name", "")
            url = r.get("url", "")
            reason = r.get("reason", "")
            lines.append(f"| {section} | {name} | {url} | {reason} |")
    lines.append("")

    lines.append("## Reviewer checklist")
    lines.append("- [ ] Each addition is genuinely related to EU compliance.")
    lines.append("- [ ] Each addition has an OSI license file.")
    lines.append("- [ ] Each addition has been pushed to in the last 18 months.")
    lines.append("- [ ] Each removal is verified (URL really 404s or repo really archived).")
    lines.append("- [ ] `awesome-lint` passes locally.")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _cmd_scrape(args: argparse.Namespace) -> int:
    repos = scrape_github_trending(args.language, args.topic)
    json.dump(repos, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


def _cmd_lintcheck(args: argparse.Namespace) -> int:
    current = parse_readme_sections(args.readme)
    removals = propose_removals(current, max_age_days=args.max_age_days)
    json.dump(removals, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


def _cmd_propose(args: argparse.Namespace) -> int:
    current = parse_readme_sections(args.readme)
    scraped: list[dict] = []
    for lang in args.languages.split(","):
        scraped.extend(scrape_github_trending(lang.strip(), args.topic))
    additions = propose_additions(scraped, current)
    removals = propose_removals(current, max_age_days=args.max_age_days) if args.with_removals else []
    body = emit_pr_body(additions, removals, args.run_id)
    sys.stdout.write(body)
    sys.stdout.write("\n")
    return 0


def _cmd_apply(args: argparse.Namespace) -> int:
    sys.stderr.write("apply: no-op in v1 — operator reviews diff manually.\n")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="auto_update", description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    p_scrape = sub.add_parser("scrape", help="fetch GitHub trending")
    p_scrape.add_argument("--language", default="python")
    p_scrape.add_argument("--topic", default="weekly")
    p_scrape.set_defaults(func=_cmd_scrape)

    p_lint = sub.add_parser("lintcheck", help="check README links for removal candidates")
    p_lint.add_argument("--readme", default="README.md")
    p_lint.add_argument("--max-age-days", type=int, default=540)
    p_lint.set_defaults(func=_cmd_lintcheck)

    p_prop = sub.add_parser("propose", help="emit PR body with additions+removals")
    p_prop.add_argument("--readme", default="README.md")
    p_prop.add_argument("--languages", default="python,go,typescript,rust")
    p_prop.add_argument("--topic", default="weekly")
    p_prop.add_argument("--max-age-days", type=int, default=540)
    p_prop.add_argument("--with-removals", action="store_true")
    p_prop.add_argument("--run-id", default="local")
    p_prop.set_defaults(func=_cmd_propose)

    p_apply = sub.add_parser("apply", help="no-op in v1")
    p_apply.set_defaults(func=_cmd_apply)

    args = p.parse_args(argv)
    return int(args.func(args) or 0)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
