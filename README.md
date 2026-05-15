# Awesome EU Compliance Tooling [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Curated list of open-source and commercial tools that help engineers comply with EU regulatory frameworks: CRA, EHDS, AI Act, NIS2, DORA, MDR, GDPR.

Between 2024 and 2027 the EU stacks seven major digital regulations on top of each other: the Cyber Resilience Act (CRA, fully applicable December 2027), the European Health Data Space (EHDS, phased in from 2027), the AI Act (high-risk obligations applicable August 2026), NIS2 (in force since October 2024), DORA (applicable January 2025), the Medical Device Regulation (MDR, applicable since 2021 with extended deadlines through 2028), and GDPR (since 2018). Each framework demands evidence (SBOMs, conformity assessments, fundamental-rights impact assessments, ICT-register exports, technical files, DPIAs). This list curates the tooling engineers actually reach for when producing that evidence. Inclusion bar: the tool exists, is reachable, has a discoverable license, and addresses a specific clause or annex of a named EU regulation. No vapor, no "compliance theatre" platforms with nothing to install.

> Note. Inclusion is editorial. Listing does not equal endorsement. PRs welcome, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Contents

- [Cyber Resilience Act (CRA)](#cyber-resilience-act-cra)
- [European Health Data Space (EHDS) and medical data](#european-health-data-space-ehds-and-medical-data)
- [EU AI Act](#eu-ai-act)
- [NIS2 and cybersecurity governance](#nis2-and-cybersecurity-governance)
- [DORA and financial-sector resilience](#dora-and-financial-sector-resilience)
- [Medical Device Regulation (MDR and IVDR)](#medical-device-regulation-mdr-and-ivdr)
- [GDPR engineering tooling](#gdpr-engineering-tooling)
- [Meta and cross-cutting](#meta-and-cross-cutting)
- [Educational resources](#educational-resources)
- [Contributing](#contributing)
- [License](#license)

## Cyber Resilience Act (CRA)

Tools for producing the SBOMs, VEX statements, vulnerability evidence, and PSIRT workflows that the CRA (Regulation EU 2024/2847) requires under Annex I section 2 (vulnerability handling requirements) and Annex VII (technical documentation).

- [syft](https://github.com/anchore/syft) - Generates CycloneDX and SPDX SBOMs from container images, filesystems, and source trees; the de-facto starting point for CRA Annex I section 2(1) software inventory (Go, Apache-2.0, last activity 2026-05).
- [cyclonedx-cli](https://github.com/CycloneDX/cyclonedx-cli) - Reference CLI for the CycloneDX BOM standard with validate, convert, diff, merge, and sign operations; CycloneDX is one of the two SBOM formats explicitly endorsed by the EU CRA implementing acts (C#/.NET, Apache-2.0, last activity 2026-05).
- [cdxgen](https://github.com/CycloneDX/cdxgen) - Polyglot SBOM generator covering 40+ ecosystems and producing CycloneDX 1.6 with VEX, formulation, and machine-learning BOM extensions; covers Annex VII technical-file inventory across heterogeneous stacks (JavaScript, Apache-2.0, last activity 2026-05).
- [parlay](https://github.com/snyk/parlay) - Enriches existing SBOMs with license, OpenSSF Scorecard, and vulnerability data via stdin/stdout pipelines; useful for closing CRA Annex I section 2(2) exploitable-vulnerabilities evidence gaps (Go, Apache-2.0, last activity 2026-05).
- [Dependency-Track](https://github.com/DependencyTrack/dependency-track) - Continuous SBOM-driven vulnerability and license platform that persists CycloneDX BOMs, tracks VEX, integrates with NVD/OSV/GHSA, and supports policy alerts mappable to CRA vulnerability-handling obligations (Java, Apache-2.0, last activity 2026-05).
- [GUAC](https://github.com/guacsec/guac) - Graph for Understanding Artifact Composition; aggregates SBOMs, SLSA attestations, OSV, and VEX into a queryable graph useful for cross-product supply-chain queries CRA-regulated manufacturers face during audits. OpenSSF incubating project (Go, Apache-2.0, last activity 2026-05).
- [FOSSology](https://github.com/fossology/fossology) - License and copyright scanner with bulk-analysis workflow; widely used to produce the FOSS-component license evidence that complements an Annex VII technical file (PHP/C, GPL-2.0, last activity 2026-05).
- [REUSE tool](https://github.com/fsfe/reuse-tool) - Reference implementation of the FSFE REUSE specification for in-source SPDX licensing headers; makes downstream FOSSology/SPDX reporting tractable (Python, License not declared via SPDX, last activity 2026-04).
- [SPDX tools (Java)](https://github.com/spdx/tools-java) - Reference Java toolkit for the ISO/IEC 5962 SPDX SBOM standard; SPDX is the second SBOM format named in CRA guidance (Java, Apache-2.0, last activity 2026-05).
- [sbomify](https://sbomify.com/) - Hosted SBOM lifecycle and sharing platform with explicit CRA and FDA mapping; supports CycloneDX, SPDX, VEX, and Annex VII evidence packs (proprietary, free tier available, still-live commercial page).
- [CRA Evidence](https://craevidence.com/) - Commercial CRA compliance platform covering SBOM/HBOM management, VEX automation, ENISA 24h/72h/14d incident reporting, and the Annex VII technical file. Currently waitlist-only (beta closed) (proprietary, still-live commercial page).
- [Prismor](https://prismor.dev/) - Build-time SPDX SBOM and VEX generation, CVE remediation, and AI-agent guardrails marketed as CRA autopilot (proprietary, still-live commercial page).
- [OPSWAT MetaDefender Software Supply Chain](https://www.opswat.com/products/metadefender/software-supply-chain) - Enterprise SBOM, malware multi-scan, and software-supply-chain inspection with explicit CRA roadmap; supports CycloneDX and SPDX export (proprietary, still-live commercial page).
- [Snyk Open Source](https://snyk.io/product/open-source-security-management/) - Commercial SCA with SBOM export, VEX, and a free tier; widely deployed for the known-exploitable-vulnerabilities leg of CRA Annex I section 2 (proprietary, free tier available, still-live commercial page).

## European Health Data Space (EHDS) and medical data

Tools relevant to the EHDS Regulation (EU 2025/327): secondary-use access, FHIR interoperability under MyHealth@EU, and the DICOM/FHIR pseudonymisation work that any secondary-use data holder must do.

- [pydicom](https://github.com/pydicom/pydicom) - Pure-Python DICOM toolkit; foundation for nearly every Python-based de-identifier touching EHDS Article 50 secondary-use datasets (Python, MIT-style license not declared via SPDX, last activity 2026-05).
- [dcm4che](https://github.com/dcm4che/dcm4che) - Java DICOM implementation with a full archive (`dcm4chee-arc-light`); used by hospitals and imaging biobanks across the EU to operate DICOM endpoints (Java, multi-license MPL/GPL/LGPL not declared via SPDX, last activity 2026-04).
- [MIRC CTP (Clinical Trial Processor)](https://github.com/johnperry/CTP) - RSNA reference pipeline for DICOM de-identification per the DICOM PS3.15 Attribute Confidentiality profile (basic plus retention options); the most-cited baseline for EHDS-grade pseudonymisation of imaging (Java, RSNA Public License not declared via SPDX, last activity 2025-10).
- [DICOM Anonymizer (Kitware/Python)](https://github.com/KitwareMedical/dicom-anonymizer) - Tag-by-tag DICOM anonymizer aligned with PS3.15; scriptable for batch re-identification pipelines (Python, BSD-3-Clause, last activity 2025-08).
- [Synthea](https://github.com/synthetichealth/synthea) - MITRE synthetic-patient generator producing FHIR R4, C-CDA, and CSV bundles; a workhorse for EHDS test environments where real PHI is off-limits (Java, Apache-2.0, last activity 2026-05).
- [HAPI FHIR](https://github.com/hapifhir/hapi-fhir) - Reference Java implementation of HL7 FHIR with validator, server, and CLI; conformance baseline for the FHIR profiles MyHealth@EU mandates (Java, Apache-2.0, last activity 2026-05).
- [MONAI Label](https://github.com/Project-MONAI/MONAILabel) - Open-source server for AI-assisted medical-image labelling with 3D Slicer, OHIF, and QuPath plugins; relevant where EHDS secondary-use datasets feed AI development (Python, Apache-2.0, last activity 2026-04).
- [OHIF Viewer](https://github.com/OHIF/Viewers) - Web-based, DICOMweb-native viewer used as the reference UI for many EU imaging-research platforms exposing EHDS-style access (TypeScript, MIT, last activity 2026-05).
- [Presidio](https://github.com/microsoft/presidio) - Microsoft PII detection and de-identification framework for free text; usable on FHIR narrative fields and clinical notes prior to EHDS secondary-use release (Python, MIT, last activity 2026-05).
- [ONC Certification (g)(10) Test Kit](https://github.com/onc-healthit/onc-certification-g10-test-kit) - Successor to the archived Inferno program; FHIR conformance and security test kit reusable in EU MyHealth@EU pilots to validate FHIR endpoints (Ruby, Apache-2.0, last activity 2026-04).

## EU AI Act

Tools that produce the technical-documentation evidence required by Annex IV (high-risk AI systems), the fundamental-rights impact assessments of Article 27, and the bias/robustness measurements implicit in Articles 9 to 15.

- [Microsoft Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox) - Dashboard combining InterpretML, Fairlearn, error-analysis, and counterfactual tools; covers a large fraction of Annex IV section 2(g) fitness-for-purpose evidence (Python, MIT, last activity 2026-04).
- [Fairlearn](https://github.com/fairlearn/fairlearn) - Python toolkit for assessing and mitigating group fairness; directly supports Article 10(2)(f-g) bias-examination requirements (Python, MIT, last activity 2026-05).
- [AI Fairness 360 (AIF360)](https://github.com/Trusted-AI/AIF360) - IBM and LF-AI comprehensive fairness metrics and mitigation library; long-standing reference for AI Act Article 10 bias examination (Python, Apache-2.0, last activity 2025-11).
- [Holistic AI](https://github.com/holistic-ai/holisticai) - Trustworthy-AI library covering bias, robustness, explainability, security, and efficacy in one API; useful single-vendor pane for Annex IV documentation (Python, Apache-2.0, last activity 2026-01).
- [MLflow](https://github.com/mlflow/mlflow) - Open-source experiment-tracking and model registry; the artifact-tracking backbone many teams use to assemble Annex IV section 2(c) design-specifications evidence (Python, Apache-2.0, last activity 2026-05).
- [Credo AI Platform](https://www.credo.ai/) - Hosted governance platform with explicit EU AI Act mapping; produces audit-ready evidence packs (proprietary, still-live commercial page).
- [Weights & Biases](https://wandb.ai/) - Experiment tracking, model registry, and artifact lineage with freemium tier and OSS client. Supports Annex IV section 2(c) traceability (proprietary, free tier available, still-live commercial page).

## NIS2 and cybersecurity governance

Tooling for the technical and operational measures of NIS2 Article 21 (cybersecurity risk-management measures) and Article 23 (incident reporting). Most entries are battle-tested OSS already deployed in EU CSIRTs.

- [OpenSCAP](https://github.com/OpenSCAP/openscap) - NIST-validated SCAP scanner; produces hardening evidence (DISA STIG, CIS, ANSSI) often reused as NIS2 Article 21(2)(d) supply-chain-security evidence (C, LGPL-2.1, last activity 2026-05).
- [Wazuh](https://github.com/wazuh/wazuh) - Open-source XDR/SIEM with FIM, log analysis, and SCA; broadly deployed for NIS2 Article 21(2)(b) incident-handling baselines (C/Python, License not declared via SPDX, last activity 2026-05).
- [OSSEC](https://github.com/ossec/ossec-hids) - Long-standing host-based intrusion-detection system; the OG of NIS2-style logging-and-monitoring controls (C, GPL-2.0, last activity 2026-04).
- [Lynis](https://github.com/CISOfy/lynis) - Hardening audit tool for Unix systems with NIS2-aligned controls catalogue (Shell, GPL-3.0, last activity 2026-05).
- [OpenVAS / Greenbone Community Edition](https://github.com/greenbone/openvas-scanner) - Open vulnerability scanner; canonical for Article 21(2)(e) vulnerability-handling (C, GPL-2.0, last activity 2026-05).
- [MISP](https://github.com/MISP/MISP) - Malware-information-sharing platform used by ENISA, national CSIRTs, and ISACs; supports NIS2 Article 29 information-sharing arrangements (PHP/Python, AGPL-3.0, last activity 2026-05).
- [Suricata](https://github.com/OISF/suricata) - High-performance NIDS/NIPS engine; pillar of NIS2 Article 21(2)(b) detection capabilities (C, GPL-2.0, last activity 2026-05).
- [Falco](https://github.com/falcosecurity/falco) - CNCF-graduated runtime security for containers and Linux hosts; produces NIS2-relevant runtime telemetry (C++, Apache-2.0, last activity 2026-05).
- [Sigma](https://github.com/SigmaHQ/sigma) - Generic detection-rule format with SIEM-agnostic conversion; lingua franca for Article 21(2)(g) detection-engineering catalogues (YAML, DRL-1.1 not declared via SPDX, last activity 2026-05).
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) - Library of small, portable detection-test scripts mapped to MITRE ATT&CK; produces evidence of NIS2 Article 21(2)(f) effectiveness testing (YAML/PowerShell, MIT, last activity 2026-05).

## DORA and financial-sector resilience

DORA (Regulation EU 2022/2554) demands ICT risk-management, third-party-risk registers, threat-led penetration testing, and incident reporting. No single OSS covers it; the entries here cover individual obligations.

- [HashiCorp Vault (Community)](https://github.com/hashicorp/vault) - Secrets management; supports DORA Article 9 cryptographic key management (Go, BUSL-1.1 not declared via SPDX, last activity 2026-05).
- [OWASP ASVS](https://github.com/OWASP/ASVS) - Application Security Verification Standard; common control framework for DORA Article 8 (ICT risk-management framework) at the application layer (Markdown, CC-BY-SA-4.0, last activity 2026-03).
- [OWASP MASVS](https://github.com/OWASP/owasp-masvs) - Mobile equivalent of ASVS; useful where DORA scope covers retail-banking mobile apps (Markdown, CC-BY-SA-4.0, last activity 2025-12).
- [OWASP Threat Dragon](https://github.com/OWASP/threat-dragon) - Free, open-source threat-modelling tool (STRIDE/LINDDUN/CIA); supports DORA Article 8(2) risk-identification documentation (JavaScript, Apache-2.0, last activity 2026-05).
- [Microsoft Threat Modeling Tool](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool) - Free desktop threat-modelling tool with STRIDE templates (proprietary, free, still-live documentation page).
- [MITRE ATT&CK](https://github.com/mitre/cti) - Adversary-behaviour knowledge base in STIX 2.1; foundation for DORA Article 26 threat-led pen testing (TLPT) under TIBER-EU (STIX/JSON, License not declared via SPDX, last activity 2026-05).
- [MITRE Caldera](https://github.com/mitre/caldera) - Automated adversary-emulation platform mapped to ATT&CK; usable for TIBER-EU style threat-led tests (Python, Apache-2.0 not declared via SPDX, last activity 2026-05).
- [in-toto](https://github.com/in-toto/in-toto) - Supply-chain integrity framework with formal attestations; supports DORA Article 28 third-party ICT-supplier evidence (Python, License not declared via SPDX, last activity 2026-05).
- [sigstore / cosign](https://github.com/sigstore/cosign) - Keyless signing for containers, blobs, and in-toto attestations; standard for verifiable artefact provenance in DORA supplier audits (Go, Apache-2.0, last activity 2026-05).

## Medical Device Regulation (MDR and IVDR)

MDR (EU 2017/745) and IVDR (EU 2017/746) require ISO 13485 quality systems, ISO 14971 risk management, IEC 62304 software lifecycle, and a technical file per Annex II/III. Most credible OSS lives in templates and lifecycle automation.

- [OpenRegulatory templates](https://openregulatory.com/templates/) - Free MDR/IVDR-aligned templates for ISO 13485, ISO 14971, IEC 62304, IEC 62366 in Word, Markdown, and PDF; the de-facto OSS starter pack for small medical-device companies (proprietary with free templates under CC-BY-SA-4.0, still-live commercial page).
- [Formwork (OpenRegulatory eQMS)](https://openregulatory.com/formwork) - Commercial AI-assisted eQMS that consumes the OpenRegulatory templates; multiple MDR audit passes reported (proprietary, free tier available, still-live commercial page).
- [Ketryx](https://www.ketryx.com/) - Connected lifecycle-management platform for IEC 62304, ISO 13485, MDR, and 21 CFR 820 with auto-maintained traceability matrix, eQMS, and risk module (proprietary, still-live commercial page).
- [Matrix One (formerly Matrix Requirements)](https://matrixone.health/) - Requirements, risk, and test-management for medical-device software with explicit IEC 62304 and ISO 14971 templates; now a consolidated platform including former Simploud eQMS, Galen Data, and Dokspot (proprietary, still-live commercial page).
- [Greenlight Guru](https://www.greenlight.guru/) - Purpose-built medical-device QMS covering ISO 13485, MDR Annex II, and risk; widely used by EU CE-marked manufacturers (proprietary, still-live commercial page).
- [Cognidox](https://www.cognidox.com/) - Lean document-control eQMS validated for ISO 13485 with eSignatures and training matrix (proprietary, still-live commercial page).
- [Advisera 13485 / EU MDR Documentation Toolkit](https://advisera.com/13485academy/iso-13485-eu-mdr-documentation-toolkit/) - 117 editable MS-Word and Excel templates covering ISO 13485, ISO 14971, and EU MDR (proprietary, still-live commercial page).
- [DICOM PS3.15 reference (Innolitics DICOM standard browser)](https://dicom.innolitics.com/) - Free hyperlinked reference to the DICOM standard including the PS3.15 Attribute Confidentiality profile that MDR and IVDR teams cite for de-identification (proprietary, free reference, still-live reference site).

## GDPR engineering tooling

Tools that engineers actually run (anonymisation, differential privacy, synthetic data, PII detection) to satisfy GDPR Articles 5(1)(c), 25 (data protection by design), 32 (security of processing), and 35 (DPIAs).

- [ARX Data Anonymization Tool](https://github.com/arx-deidentifier/arx) - Open-source desktop and Java library for k-, l-, and t-anonymity, delta-presence, and differential privacy; reference toolkit for GDPR Recital 26 anonymisation (Java, Apache-2.0, last activity 2025-10).
- [Amnesia (OpenAIRE)](https://amnesia.openaire.eu/) - EU-funded k-anonymity and km-anonymity tool with online and desktop UI; tailored for publishing research datasets under GDPR (Java, Apache-2.0, still-live project page).
- [Presidio](https://github.com/microsoft/presidio) - Microsoft PII detection and de-identification for text, images, and structured data; common building block for GDPR Article 32 minimisation pipelines (Python, MIT, last activity 2026-05).
- [OpenDP](https://github.com/opendp/opendp) - Harvard and Microsoft differentially-private analytics library (Rust core, Python bindings); peer-reviewed primitives suitable for GDPR-grade anonymisation claims (Rust/Python, MIT, last activity 2026-05).
- [SmartNoise](https://github.com/opendp/smartnoise-sdk) - OpenDP-based DP toolkit for SQL queries and synthetic data (Python, MIT, last activity 2026-05).
- [diffprivlib](https://github.com/IBM/differential-privacy-library) - IBM general-purpose differential-privacy library with scikit-learn-style API (Python, MIT, last activity 2025-09).
- [PyDP](https://github.com/OpenMined/PyDP) - Python wrapper around Google's C++ differential-privacy library (Python/C++, Apache-2.0, last activity 2026-05).
- [Synthetic Data Vault (SDV)](https://github.com/sdv-dev/SDV) - Toolkit for synthesising single-table, relational, and time-series tabular data; one of the most-cited alternatives to direct GDPR processing (Python, BSL-1.1 not declared via SPDX, last activity 2026-05).
- [synthcity](https://github.com/vanderschaarlab/synthcity) - Library for generating and evaluating synthetic tabular data with privacy, fairness, and augmentation benchmarks (Python, Apache-2.0, last activity 2026-04).
- [GDPR Cookie Scanner](https://github.com/Slashgear/gdpr-cookie-scanner) - Headless-Chromium CLI that interacts with consent modals and classifies cookies and network requests against GDPR and ePrivacy (JavaScript, MIT, last activity 2026-05).
- [Privado](https://github.com/Privado-Inc/privado) - Privacy code-scanning engine that maps PII flows in source code; supports GDPR Article 30 records-of-processing automation (Scala, LGPL-3.0, last activity 2025-11).

## Meta and cross-cutting

Tools that span multiple regulations (supply-chain provenance, evidence packs, audit-log primitives) and tend to live in every EU compliance program.

- [in-toto attestations](https://github.com/in-toto/attestation) - Specification for typed supply-chain attestations (SLSA provenance, SBOM, VEX, vuln scans); the substrate for CRA, DORA, and NIS2 supplier evidence (Markdown/Proto, License not declared via SPDX, last activity 2026-04).
- [Sigstore](https://github.com/sigstore/sigstore) - Free signing service and transparency log for software artefacts; cited in EU CRA, NIS2, and DORA supply-chain guidance (Go, Apache-2.0, last activity 2026-05).
- [SLSA framework](https://github.com/slsa-framework/slsa) - Supply-chain Levels for Software Artifacts spec and reference implementations; common rubric for verifiable build provenance required by CRA Annex I section 2 (Markdown/Go, dual Community Specification 1.0 and Apache-2.0, last activity 2026 verified via GitHub web UI).
- [Tekton Chains](https://github.com/tektoncd/chains) - Kubernetes-native pipeline that auto-signs build outputs and emits in-toto and SLSA attestations (Go, Apache-2.0, last activity 2026 verified via GitHub web UI).
- [OpenChain Project repositories](https://github.com/OpenChain-Project) - Working-group repositories for the ISO/IEC 5230 open-source compliance standard; complements CRA Annex I supply-chain requirements (Markdown, CC-BY-4.0, organization with active repos through 2026-05).
- [auditbeat / Elastic Common Schema](https://github.com/elastic/beats) - Open audit-log shipper and schema; common substrate for the appropriate-logging controls cited across NIS2, DORA, AI Act, and GDPR Article 32 (Go, dual Apache-2.0 / Elastic-2.0, last activity 2026 verified via GitHub web UI).

## Educational resources

Primary sources and well-regarded analyses. No vendor blogs unless they sit on top of an authoritative dataset.

- [EU Cyber Resilience Act, Commission portal](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act) - Official Commission landing page with the consolidated CRA text and implementing-acts roadmap.
- [European Health Data Space, Commission portal](https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space_en) - Commission landing page for EHDS with implementation timeline.
- [EU AI Act explorer (Future of Life Institute)](https://artificialintelligenceact.eu/) - Hyperlinked, multi-language reading view of the AI Act text, Annexes, and Code of Practice.
- [EU AI Act, EUR-Lex consolidated text](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) - Authoritative Official Journal version (Regulation EU 2024/1689).
- [NIS2, EUR-Lex consolidated text](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) - Directive EU 2022/2555 official text.
- [DORA, EUR-Lex consolidated text](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) - Regulation EU 2022/2554 official text.
- [ENISA publications](https://www.enisa.europa.eu/publications) - The EU cybersecurity agency's reports, threat landscape, NIS2 guidance, and CRA harmonised-standards work.
- [EDPB guidelines](https://www.edpb.europa.eu/our-work-tools/general-guidance/guidelines-recommendations-best-practices_en) - Authoritative GDPR and ePrivacy interpretive guidance from the European Data Protection Board.
- [OpenRegulatory blog](https://openregulatory.com/blog/) - Plain-English MDR, IVDR, ISO 13485, and IEC 62304 explainers from a regulatory-affairs consultancy.
- [FRIA Guide (ECNL and Danish Institute for Human Rights)](https://ecnl.org/publications/guide-fundamental-rights-impact-assessments-fria) - Practical model for fulfilling AI Act Article 27 fundamental-rights impact assessments.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[CC0 1.0](LICENSE), listed tools retain their own licenses.
