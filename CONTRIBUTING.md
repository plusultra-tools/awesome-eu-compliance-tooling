# Contributing

Thanks for helping keep **awesome-eu-compliance-tooling** current and useful.
This list curates **open-source tools and libraries that address EU regulatory
compliance** (CRA, EHDS, AI Act, NIS2, DORA, MDR, GDPR, eIDAS, and adjacent
regimes). It is **not** a directory of consultancies or generic security tools.

---

## How to add a tool

1. **Open a Pull Request** that modifies `README.md` only. One PR per tool.
2. **Add a single row** in the correct section, in alphabetical order.
3. Use the row template (see README for exact column order):

   ```markdown
   - [<Tool name>](<https URL>) — One-line description, ending with a period. License: <SPDX-id>. Regulation: <CRA|EHDS|AI Act|NIS2|DORA|MDR|GDPR|eIDAS>. Last release: <YYYY-MM>.
   ```

4. **Update the table of contents** if you add a new section.
5. **Run linters locally** before pushing (see "Local checks" below).

---

## Editorial criteria (the bar)

A tool is accepted into this list only if **all** of the following hold:

1. **Addresses an EU regulation explicitly.** The project's README, docs, or
   homepage must reference the relevant regulation by name (e.g., "CRA",
   "EU AI Act", "NIS2"). Generic SBOM/SAST/IAM tools that are *useful for*
   compliance but do not target EU regimes go elsewhere (e.g.,
   `awesome-security`, `awesome-sbom`).
2. **Has a real, reachable URL.** No 404s, no domain-squatted dead links.
   The CI link-check runs weekly; entries that 404 are removed automatically.
3. **License declared.** SPDX identifier required (`MIT`, `Apache-2.0`,
   `AGPL-3.0`, `EUPL-1.2`, etc.). Source-available-but-restrictive licenses
   (BSL, SSPL, Commons Clause) are accepted but must be clearly flagged.
4. **Recent activity.** Last commit or release **within 18 months** of
   submission. Maintained beats abandoned, even if abandoned was great.
5. **Not a paid service masquerading as a tool.** Tools whose only useful
   functionality requires a paid SaaS subscription belong in a different
   list. If the open-source core is real and self-hostable, it qualifies.
6. **Not duplicative.** If two tools do effectively the same job, the more
   mature / more maintained one stays.

The full editorial bar is also stated in `README.md` under
"Editorial criteria"; this file and the README must agree. If they
disagree, the README wins.

---

## PR template requirements

Every PR must include, in the body:

- **Tool name and homepage URL.**
- **Which EU regulation it addresses**, with a one-line justification (link
  to the project's own docs that mention the regulation).
- **License (SPDX).**
- **Last release date** (or last commit if no releases).
- **Why this tool belongs in the list** (1–3 sentences).
- **Checklist:**
  - [ ] I have read the editorial criteria above.
  - [ ] The tool addresses at least one EU regulation explicitly.
  - [ ] The URL works (no 404).
  - [ ] License is declared with an SPDX identifier.
  - [ ] Last commit or release is within 18 months.
  - [ ] I added a single row in alphabetical order in the correct section.
  - [ ] I ran `awesome-lint README.md` locally and it passed.

PRs that do not include this checklist will be asked to amend.

---

## Local checks (before pushing)

```bash
# Awesome-list lint (npm)
npm install --global awesome-lint
awesome-lint README.md

# Broken-link scan (cargo or pre-built binary)
# https://github.com/lycheeverse/lychee
lychee --verbose README.md

# Python tooling (if you touch tools/)
python -m pip install -e .
ruff check tools/
python -m py_compile tools/*.py
```

A `.pre-commit-config.yaml` is provided; install with:

```bash
pip install pre-commit
pre-commit install
```

---

## Submitting a removal

If a listed tool 404s, is abandoned (>18 months no activity), or has changed
scope so it no longer addresses an EU regulation, open a PR removing the row
and cite the evidence in the PR body. The weekly `auto-update` workflow does
this automatically, but human-submitted removals are welcome.

---

## Code of conduct

By participating, you agree to abide by the
[Contributor Covenant 2.1](./CODE_OF_CONDUCT.md).

---

## License

This list is published under [CC0 1.0](./LICENSE). Tools retain their own
licenses.
