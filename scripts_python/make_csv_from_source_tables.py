# -*- coding: utf-8 -*-
"""
Build figure-specific CSV files from the two source tables.

Expected inputs in the same directory as this script:
    - table_transport_source.csv
    - table_city_covariates_source.csv

Outputs:
    - figure1_cross_city_comparison_2025.csv
    - figure3_monthly_congestion_2024_2025.csv
    - figure4_peak_hour_comparison_2025.csv
    - figure5_city_covariates_2024.csv
    - figure5_regression_dataset.csv
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
TRANSPORT_CSV = BASE_DIR / "table_transport_source.csv"
COVARIATES_CSV = BASE_DIR / "table_city_covariates_source.csv"

FIG1_CSV = BASE_DIR / "figure1_cross_city_comparison_2025.csv"
FIG3_CSV = BASE_DIR / "figure3_monthly_congestion_2024_2025.csv"
FIG4_CSV = BASE_DIR / "figure4_peak_hour_comparison_2025.csv"
FIG5_COV_CSV = BASE_DIR / "figure5_city_covariates_2024.csv"
FIG5_REG_CSV = BASE_DIR / "figure5_regression_dataset.csv"

months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
month_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def check_required_columns(df, required, name):
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"{name} is missing required columns: {missing}")

def main():
    transport = pd.read_csv(TRANSPORT_CSV)
    covariates = pd.read_csv(COVARIATES_CSV)

    check_required_columns(
        transport,
        [
            "country", "city", "average_congestion_pct", "average_travel_time_10km_sec", "average_speed_kmh",
            "morning_time_10km_sec", "morning_level_pct", "morning_speed_kmh",
            "evening_time_10km_sec", "evening_level_pct", "evening_speed_kmh"
        ] + [f"{m}_2024" for m in months] + [f"{m}_2025" for m in months],
        "table_transport_source.csv"
    )

    check_required_columns(
        covariates,
        [
            "country", "city", "population", "population_density_per_km2",
            "motor_vehicles_per_1000_people", "road_length_km"
        ],
        "table_city_covariates_source.csv"
    )

    fig1_df = transport[
        ["country", "city", "average_congestion_pct", "average_travel_time_10km_sec", "average_speed_kmh"]
    ].copy()
    fig1_df.to_csv(FIG1_CSV, index=False)

    records = []
    for _, row in transport.iterrows():
        for y in [2024, 2025]:
            for m_short, m_label in zip(months, month_labels):
                records.append({
                    "country": row["country"],
                    "city": row["city"],
                    "year": y,
                    "month": m_label,
                    "congestion_pct": row[f"{m_short}_{y}"]
                })
    fig3_df = pd.DataFrame(records)
    fig3_df.to_csv(FIG3_CSV, index=False)

    fig4_df = transport[
        ["country", "city",
         "morning_time_10km_sec", "morning_level_pct", "morning_speed_kmh",
         "evening_time_10km_sec", "evening_level_pct", "evening_speed_kmh"]
    ].copy()
    fig4_df.to_csv(FIG4_CSV, index=False)

    fig5_cov_df = covariates.copy()
    fig5_cov_df.to_csv(FIG5_COV_CSV, index=False)

    fig5_reg_df = fig1_df.merge(
        covariates[
            [
                "country", "city", "population", "population_density_per_km2",
                "motor_vehicles_per_1000_people", "road_length_km"
            ]
        ],
        on=["country", "city"],
        how="left"
    )
    fig5_reg_df["road_length_per_1000_people_km"] = fig5_reg_df["road_length_km"] / fig5_reg_df["population"] * 1000
    fig5_reg_df.to_csv(FIG5_REG_CSV, index=False)

    print("Done.")
    print(f"Saved: {FIG1_CSV.name}")
    print(f"Saved: {FIG3_CSV.name}")
    print(f"Saved: {FIG4_CSV.name}")
    print(f"Saved: {FIG5_COV_CSV.name}")
    print(f"Saved: {FIG5_REG_CSV.name}")

if __name__ == "__main__":
    main()
