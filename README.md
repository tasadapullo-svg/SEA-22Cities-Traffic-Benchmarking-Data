# SEA 22 Cities Traffic Performance Dataset

Generated: 2026-05-24

This repository-ready package contains the cleaned datasets, plot-ready CSV files, figure files, Python plotting scripts, validation records, and source-evidence files used for a manuscript on multidimensional traffic-performance benchmarking and contextual diagnosis of 22 Southeast Asian cities.

## Repository structure

```text
README.md
CITATION.cff
MANIFEST.csv
DATA_DICTIONARY.csv
VALIDATION_REPORT.md
VALIDATION_CHECKS.csv
data_master_workbooks/
data_plot_ready_csv/
figures_png/
scripts_python/
evidence_pt_its_sources/
evidence_tomtom_screenshots/
EXCLUDED_DUPLICATE_FILES.md
```

## Key analysis files

- `data_plot_ready_csv/article_master_dataset_22cities.csv`: merged city-level master dataset.
- `data_plot_ready_csv/figure3_annual_traffic_performance_2025.csv`: 2025 annual congestion, 10 km travel time, and average speed.
- `data_plot_ready_csv/figure4_monthly_congestion_long_2024_2025.csv`: monthly congestion in long format for 2024-2025.
- `data_plot_ready_csv/figure5_peak_hour_comparison_2025.csv`: morning-evening peak-hour comparison indicators.
- `data_plot_ready_csv/urban_context_and_regression_variables.csv`: population, vehicle, and road-context variables.
- `data_plot_ready_csv/pt_its_supplement_22cities.csv`: public-transport supply and Signal/ITS proxy scores.
- `data_plot_ready_csv/pt_its_source_registry.csv`: source registry for PT/ITS variables.

## Validation files

- `DATA_DICTIONARY.csv`: variable definitions and intended use.
- `VALIDATION_REPORT.md`: three-round validation summary.
- `VALIDATION_CHECKS.csv`: structured validation checks.
- `MANIFEST.csv`: regenerated file manifest with English file paths and SHA-256 checksums.

## Scope notes

Public-transport supply and Signal/ITS scores are contextual proxy variables. They are suitable for exploratory diagnosis and benchmarking, not for causal inference. `PT_mode_share_pct` is populated only where comparable evidence was available. The complete cross-city proxy variables are `PT_supply_score_0_3` and `ITS_signal_score_0_3`.

TomTom screenshot evidence is provided as supporting source material. The screenshots were renamed and flattened into `evidence_tomtom_screenshots/`; the file `tomtom_screenshot_manifest.csv` records the original source path for each screenshot.

## GitHub and Zenodo upload notes

1. Upload the full contents of this package to a GitHub repository.
2. Create a GitHub release after the repository is complete.
3. Archive the release in Zenodo to generate a DOI.
4. After Zenodo assigns the DOI, update `CITATION.cff` and the manuscript Data Availability Statement with the final DOI.

## License note

No license is imposed in this package. Select the final data license in Zenodo after confirming author and third-party-source permissions. For manuscript submission, cite the generated Zenodo DOI rather than redistributing vendor-controlled material outside the permitted evidence scope.

## Suggested citation text

Sun, W. (2026). SEA 22 Cities Traffic Performance Dataset. GitHub/Zenodo archived dataset. Use the final Zenodo DOI after release.
