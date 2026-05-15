# Kill-gate -- awesome-eu-compliance-tooling

**Set:** 2026-05-15.
**Day-0 = first push of `plusultra-tools/awesome-eu-compliance-tooling` to GitHub.**
**Decision day = Day-30.** Secondary gate at d+90 for sindresorhus PR (per the 30-day repo-age rule).

This venture is an **audience/funnel asset** (Cluster C/D per `state/portfolio-v1.md`). Direct revenue is structurally low (curated lists do not monetize on their own); the bet is on indirect lead-gen into ventures #1-#5 of the compliance-manifest cluster. The kill-gate metrics reflect that.

---

## Pass conditions (any ONE = continue + double down on funnel)

| Metric | Threshold | How measured |
|---|---|---|
| GitHub stars | ≥ 100 by d+30 | Public counter on repo |
| Sidebar inclusion in another awesome-list (not sindresorhus, that's d+90+) | ≥ 1 by d+30 | grep curated-list trackers + manual check |
| Referrer traffic to any cluster-A venture (ai-act-conformity-pack, cra-sbom-evidence, ehds-anon-kit, etc.) from this repo | ≥ 50 unique visits by d+30 | GitHub repo referrer page on each venture |
| Direct PR contributions from non-personal accounts | ≥ 3 by d+30 | PR list, employer/affiliation visible in GitHub profile |
| Inbound email to ops@ asking for new-entry consideration with stated affiliation | ≥ 2 by d+30 | Mailbox |
| sindresorhus/awesome PR opened d+30+ AND accepted | by d+90 | sindresorhus/awesome PR queue |

**Hitting any one = green.** Continue maintenance + content-marketing schedule.

---

## Fail conditions (ALL of the below ⇒ kill)

- < 30 stars by d+30
- 0 referrer-traffic to any cluster-A venture from this repo
- 0 inbound contribution from non-personal accounts
- 0 sidebar inclusions in any other awesome-list by d+90

If all hit, archive the repo (preserve as personal portfolio artifact). The compliance-cluster ventures continue without the funnel.

---

## Yellow zone

1 metric near threshold, others below half: ramp content-marketing — publish one dev.to article every 2 weeks linking the curated list + one cluster-A venture (rotate). Wait another 30 days. Re-evaluate at d+60.

---

## Phase 2 conditions

On green:
1. Add a "Submit a tool" form (Formspree) and a transparent inclusion bar (open-source preferred; commercial allowed but flagged).
2. Add a monthly newsletter (Buttondown or similar, free tier ≤1k subs) summarizing new EU compliance acts + new tool additions. This becomes the durable funnel asset.
3. Affiliate links to a small set of commercial entries (vendors who agree to a flat 5% rev-share OR a one-off €99 inclusion fee for a "verified active" badge) — earliest d+90, only if d+30 was green AND principal §12-approves the commercial relationship.

---

## Anti-patterns to avoid

- Do not buy stars / traffic. The cluster-A ventures will see through it via referrer mix.
- Do not delete inactive entries silently; mark them `archived` or `last-active YYYY-MM`. Killing entries kills SEO links.
- Do not accept commercial entries with no OSS counterpart in the same category. The list dies as marketing channel if the OSS:commercial ratio drops below 2:1.
