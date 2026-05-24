# SEA 22 Cities Article Data Package: Validation Report

Generated: 2026-05-19 06:31:33

## Three-round checks

### Round 1 — Completeness

- **Annual KPI row count**: PASS — 22 rows
- **Monthly long row count**: PASS — 528 rows; expected 22 cities x 24 months = 528
- **Monthly wide row count**: PASS — 22 rows
- **Peak-hour row count**: PASS — 22 rows
- **Regression/context row count**: PASS — 22 rows
- **PT/ITS supplement row count**: PASS — 22 rows
- **PT/ITS source registry row count**: PASS — 35 rows
- **PT/ITS evidence log row count**: PASS — 53 rows

### Round 2 — City-set and key consistency

- **City set consistency: monthly_long**: PASS — missing=[]; extra=[]
- **City set consistency: monthly_wide**: PASS — missing=[]; extra=[]
- **City set consistency: peak_hour**: PASS — missing=[]; extra=[]
- **City set consistency: context**: PASS — missing=[]; extra=[]
- **City set consistency: pt_its**: PASS — missing=[]; extra=[]

### Round 3 — Numeric range and evidence audit

- **Annual numeric parse**: PASS — all numeric
- **PT/ITS score numeric parse**: PASS — all numeric
- **PT/ITS score range 0-3**: PASS — all scores within range
- **Thailand TomTom screenshot evidence**: WARN — 0 files found in uploaded Thailand screenshot folders; CSV traffic data included separately.

## Important notes

- The PT and Signal/ITS indicators are contextual proxy variables. They should be used for exploratory diagnosis, not causal inference.
- PT mode share is included only when evidence was found. The complete cross-city variable is `PT_supply_score_0_3`.
- Signal coordination percentage is not uniformly available across 22 cities; `ITS_signal_score_0_3` is the harmonized proxy.
- Uploaded Thailand TomTom screenshot folders appear incomplete/empty; keep the traffic CSV values, but supplement screenshots later if the journal requests raw webpage evidence.
- For submission, cite primary sources from `pt_its_source_registry.csv` and keep screenshots/PDFs as supplementary evidence, not necessarily as main manuscript tables.