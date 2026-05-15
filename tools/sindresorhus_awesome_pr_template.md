<!--
Pre-filled PR body for submitting `awesome-eu-compliance-tooling` to the
upstream `sindresorhus/awesome` meta-list. Paste this into the PR body
once the repo is publicly available and all CI checks are green.

Verify before submitting:
- README.md passes `npx awesome-lint`.
- All links in README.md return 2xx (run `markdown-link-check README.md`).
- Repo has: README.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md, LICENSE, .github/workflows/awesome-lint.yml.
- Repo has been public for ≥ 30 days OR has ≥ 200 stars (sindresorhus's stated minimum).
  → If neither, the PR will be closed politely. Wait or skip the upstream submission.
-->

## What is the list about?

`awesome-eu-compliance-tooling` is a curated, regulation-grouped list of open-source and commercial tooling that helps engineering teams comply with EU regulatory frameworks:

- **Cyber Resilience Act** (CRA — Regulation (EU) 2024/2847, vulnerability handling in force 2026-09-11)
- **European Health Data Space** (EHDS — Regulation (EU) 2025/327)
- **EU AI Act** (Regulation (EU) 2024/1689, post-Digital-Omnibus 2026)
- **NIS2** (Directive (EU) 2022/2555)
- **DORA** (Regulation (EU) 2022/2554)
- **Medical Device Regulation & IVDR** (Regulations (EU) 2017/745 + 2017/746)
- **GDPR** engineering tooling

The list was created because EU regulatory stacking 2026-2028 forces engineering teams to evaluate compliance tooling across 6-7 frameworks simultaneously, and no single existing awesome-list covers them together.

## Why does this belong in `awesome`?

- ≥ 90 curated entries across 8 sections; not a thin list.
- Strict inclusion criteria documented in CONTRIBUTING.md: tool must address a specific EU regulation article/annex, have a real maintained URL, declare its license, and have a verifiable last-release/commit within 18 months.
- Each entry single-line, link-first, license-and-cadence annotated, matching `awesome` format spec.
- Awesome-list `awesome-lint` CI on every commit (status badge in README).
- Markdown link check weekly (`linkcheck.yml`).
- Auto-update proposal workflow (`auto-update.yml`) that opens a PR every Tuesday with proposed additions from GitHub trending filtered for EU-compliance keywords. Operator reviews; no auto-merge.

## Checklist

- [x] Read the [Awesome Manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md).
- [x] Adheres to the [Awesome list guidelines](https://github.com/sindresorhus/awesome/blob/main/create-list.md).
- [x] List has been around for at least 30 days OR has at least 200 stars (verify before submit).
- [x] README has the `awesome` badge linked to https://awesome.re.
- [x] README has a description.
- [x] README has a `Contents` table-of-contents with anchor links.
- [x] One-line description per entry, in the format: `- [name](link) — description.`
- [x] Entries are sorted within each section by editorial relevance, with foundational tools at the top of each section.
- [x] List contains only items relevant to the list's theme; no irrelevant filler.
- [x] Each item links to its project page (NOT a personal blog post).
- [x] Repository has a CONTRIBUTING.md file.
- [x] Repository has a CODE_OF_CONDUCT.md (Contributor Covenant 2.1).
- [x] Repository has a LICENSE file (CC0-1.0 for the list itself).
- [x] Repository has at least one substantive contribution beyond the initial commit.

## Where would this fit in `awesome/readme.md`?

Recommended section: **Tech → Programming → Software architecture → Regulatory compliance** OR **Education → Other → Law and policy**.

If neither exists yet, propose creating a **"Regulatory compliance"** sub-section under Tech.

## Repository

https://github.com/plusultra-tools/awesome-eu-compliance-tooling

Last reviewed: <FILL_DATE_BEFORE_SUBMIT>
