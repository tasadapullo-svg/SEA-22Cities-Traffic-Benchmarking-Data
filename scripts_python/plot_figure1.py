# -*- coding: utf-8 -*-
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import transforms
import seaborn as sns

INPUT_CSV = "figure1_cross_city_comparison_2025.csv"
OUTPUT_PNG = "figure1_cross_city_comparison_2025.png"

sns.set_theme(style="whitegrid")
plt.rcParams.update({
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "font.size": 11,
    "axes.titlesize": 12,
    "axes.labelsize": 11,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
})

plot_order = [
    "George Town", "Kota Bharu", "Kuala Lumpur", "Seberang Perai", "Johor Bahru", "Ipoh", "Kajang",
    "Bangkok", "Hat Yai", "Chiang Mai", "Khon Kaen", "Nakhon Ratchasima",
    "Medan", "Bandung", "Jakarta", "Palembang", "Surabaya",
    "Davao City", "Manila",
    "Ha Noi", "Ho Chi Minh",
    "Singapore"
]

country_by_city = {
    "George Town": "Malaysia", "Kota Bharu": "Malaysia", "Kuala Lumpur": "Malaysia",
    "Seberang Perai": "Malaysia", "Johor Bahru": "Malaysia", "Ipoh": "Malaysia", "Kajang": "Malaysia",
    "Bangkok": "Thailand", "Hat Yai": "Thailand", "Chiang Mai": "Thailand",
    "Khon Kaen": "Thailand", "Nakhon Ratchasima": "Thailand",
    "Medan": "Indonesia", "Bandung": "Indonesia", "Jakarta": "Indonesia",
    "Palembang": "Indonesia", "Surabaya": "Indonesia",
    "Davao City": "Philippines", "Manila": "Philippines",
    "Ha Noi": "Vietnam", "Ho Chi Minh": "Vietnam",
    "Singapore": "Singapore"
}

def add_country_group_labels(ax, order, country_map, y_line=-0.50, y_text=-0.58):
    trans = transforms.blended_transform_factory(ax.transData, ax.transAxes)
    start = 0
    while start < len(order):
        country = country_map[order[start]]
        end = start
        while end + 1 < len(order) and country_map[order[end + 1]] == country:
            end += 1
        x0, x1 = start - 0.45, end + 0.45
        ax.plot([x0, x1], [y_line, y_line], transform=trans, color="0.35", lw=0.8, clip_on=False)
        ax.plot([x0, x0], [y_line, y_line + 0.06], transform=trans, color="0.35", lw=0.8, clip_on=False)
        ax.plot([x1, x1], [y_line, y_line + 0.06], transform=trans, color="0.35", lw=0.8, clip_on=False)
        ax.text((start + end) / 2, y_text, country, transform=trans, ha="center", va="top", fontsize=10)
        start = end + 1

def label_positive_bars(ax, bars, fmt="{:.1f}", dy=0.02):
    ymin, ymax = ax.get_ylim()
    offset = (ymax - ymin) * dy
    for b in bars:
        h = b.get_height()
        ax.text(
            b.get_x() + b.get_width() / 2, h + offset, fmt.format(h),
            ha="center", va="bottom", fontsize=8
        )

def main():
    df = pd.read_csv(INPUT_CSV)
    df = df.set_index("city").loc[plot_order].reset_index()
    x = np.arange(len(df))

    fig, axes = plt.subplots(3, 1, figsize=(17, 10), sharex=True, gridspec_kw={"hspace": 0.14})

    bars1 = axes[0].bar(x, df["average_congestion_pct"], color="#4c78a8", edgecolor="#355b84", linewidth=0.8)
    axes[0].set_ylabel("Average congestion (%)")
    axes[0].text(0.0, 1.03, "(a) Average congestion", transform=axes[0].transAxes,
                 fontsize=12, fontweight="bold", ha="left")
    label_positive_bars(axes[0], bars1, fmt="{:.1f}", dy=0.012)

    bars2 = axes[1].bar(x, df["average_travel_time_10km_sec"], color="#76b7b2", edgecolor="#4f8f8a", linewidth=0.8)
    axes[1].set_ylabel("10-km travel time (s)")
    axes[1].text(0.0, 1.03, "(b) 10-km travel time", transform=axes[1].transAxes,
                 fontsize=12, fontweight="bold", ha="left")
    label_positive_bars(axes[1], bars2, fmt="{:.0f}", dy=0.012)

    bars3 = axes[2].bar(x, df["average_speed_kmh"], color="#f28e2b", edgecolor="#b96c1f", linewidth=0.8)
    axes[2].set_ylabel("Average speed (km/h)")
    axes[2].text(0.0, 1.03, "(c) Average speed", transform=axes[2].transAxes,
                 fontsize=12, fontweight="bold", ha="left")
    label_positive_bars(axes[2], bars3, fmt="{:.1f}", dy=0.012)

    axes[0].set_title(
        "Figure 1. Cross-city comparison of average congestion, travel time, and speed (2025)",
        fontsize=14, fontweight="bold", pad=12
    )

    axes[2].set_xticks(x)
    axes[2].set_xticklabels(df["city"], rotation=45, ha="right")
    add_country_group_labels(axes[2], plot_order, country_by_city, y_line=-0.50, y_text=-0.58)

    for ax in axes:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    plt.subplots_adjust(bottom=0.22, top=0.93)
    plt.savefig(OUTPUT_PNG, bbox_inches="tight")
    plt.close()
    print(f"Saved: {OUTPUT_PNG}")

if __name__ == "__main__":
    main()
