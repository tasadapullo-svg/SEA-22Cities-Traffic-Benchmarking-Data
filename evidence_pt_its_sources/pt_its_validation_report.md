# Validation Report: PT Supply and Signal/ITS Supplement

Generated: 2026-05-19 06:17 UTC

## Round 1: completeness check

- Rows in master dataset: 22
- Unique cities: 22
- Cities missing PT_supply_score: 0
- Cities missing ITS_signal_score: 0

**Round 1 status:** PASS

## Round 2: value-range and type check

- All PT and ITS scores are within 0–3.
- Rapid-transit lengths are numeric or blank where no comparable value was assigned.

**Round 2 status:** PASS

## Round 3: source and confidence check

- Every city has at least one public-transport source.
- Every city with ITS score above 0 has at least one ITS/source evidence entry.

**Round 3 status:** PASS

## Low-confidence or caution rows

- Indonesia - Medan: PT=High, ITS=Low
- Indonesia - Palembang: PT=Medium, ITS=Low
- Indonesia - Surabaya: PT=Medium, ITS=Low
- Malaysia - George Town: PT=Medium, ITS=Low
- Malaysia - Ipoh: PT=High, ITS=Low
- Malaysia - Johor Bahru: PT=High, ITS=Low
- Malaysia - Kajang: PT=Medium, ITS=Low
- Malaysia - Kota Bharu: PT=Medium, ITS=Low
- Malaysia - Seberang Perai: PT=Medium, ITS=Low
- Thailand - Chiang Mai: PT=Medium, ITS=Low
- Thailand - Hat Yai: PT=Low, ITS=Low
- Thailand - Khon Kaen: PT=Medium, ITS=Low
- Thailand - Nakhon Ratchasima: PT=Medium, ITS=Low

## Interpretation warning

The dataset is suitable for an exploratory contextual-diagnosis layer. It is not suitable for causal inference or for claiming exact coordinated-signal percentages across all cities.
