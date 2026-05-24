# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

INPUT_CSV = "figure3_monthly_congestion_2024_2025.csv"
OUTPUT_PNG = "figure3_spatiotemporal_patterns_2024_2025.png"

sns.set_theme(style="whitegrid")
plt.rcParams.update({
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "font.size": 11,
    "axes.titlesize": 12,
    "axes.labelsize": 11,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
})

plot_order = [
    "George Town", "Kota Bharu", "Kuala Lumpur", "Seberang Perai", "Johor Bahru", "Ipoh", "Kajang",
    "Bangkok", "Hat Yai", "Chiang Mai", "Khon Kaen", "Nakhon Ratchasima",
    "Medan", "Bandung", "Jakarta", "Palembang", "Surabaya",
    "Davao City", "Manila",
    "Ha Noi", "Ho Chi Minh",
    "Singapore"
]

month_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def main():
    df = pd.read_csv(INPUT_CSV)
    df["month"] = pd.Categorical(df["month"], categories=month_labels, ordered=True)

    mat_2024 = (
        df[df["year"] == 2024]
        .pivot(index="city", columns="month", values="congestion_pct")
        .loc[plot_order, month_labels]
    )
    mat_2025 = (
        df[df["year"] == 2025]
        .pivot(index="city", columns="month", values="congestion_pct")
        .loc[plot_order, month_labels]
    )

    vmin = min(mat_2024.min().min(), mat_2025.min().min())
    vmax = max(mat_2024.max().max(), mat_2025.max().max())

    fig, axes = plt.subplots(2, 1, figsize=(11, 15), gridspec_kw={"hspace": 0.18})

    sns.heatmap(
        mat_2024, ax=axes[0], cmap="viridis_r", vmin=vmin, vmax=vmax,
        linewidths=0.3, linecolor="white",
        cbar_kws={"label": "Congestion level (%)"}
    )
    axes[0].set_title("(a) 2024", fontsize=16, fontweight="bold", pad=10)
    axes[0].set_xlabel("Month")
    axes[0].set_ylabel("City Name")

    sns.heatmap(
        mat_2025, ax=axes[1], cmap="viridis_r", vmin=vmin, vmax=vmax,
        linewidths=0.3, linecolor="white",
        cbar_kws={"label": "Congestion level (%)"}
    )
    axes[1].set_title("(b) 2025", fontsize=16, fontweight="bold", pad=10)
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("City Name")

    plt.savefig(OUTPUT_PNG, bbox_inches="tight")
    plt.close()
    print(f"Saved: {OUTPUT_PNG}")

if __name__ == "__main__":
    main()
