# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import transforms
import seaborn as sns

INPUT_CSV = "figure4_peak_hour_comparison_2025.csv"
OUTPUT_PNG = "figure4_peak_hour_comparison_2025.png"

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

def label_diverging_bars(ax, morning_vals, evening_vals, fmt="{:.0f}"):
    ymax = max(max(np.abs(morning_vals)), max(np.abs(evening_vals)))
    offset = ymax * 0.04
    for i, v in enumerate(morning_vals):
        ax.text(i, v + offset, fmt.format(v), ha="center", va="bottom", fontsize=7)
    for i, v in enumerate(evening_vals):
        ax.text(i, -v - offset, fmt.format(v), ha="center", va="top", fontsize=7)

def main():
    df = pd.read_csv(INPUT_CSV)
    df = df.set_index("city").loc[plot_order].reset_index()
    x = np.arange(len(df))

    fig, axes = plt.subplots(3, 1, figsize=(17, 13), sharex=True, gridspec_kw={"hspace": 0.28})

    m = df["morning_time_10km_sec"].to_numpy()
    e = df["evening_time_10km_sec"].to_numpy()
    axes[0].bar(x, m, color="#4c78a8", width=0.58, label="Morning rush hour")
    axes[0].bar(x, -e, color="#b0b0b0", width=0.58, label="Evening rush hour")
    axes[0].axhline(0, color="0.3", lw=0.8)
    axes[0].set_ylabel("Time taken to travel 10 km (s)")
    axes[0].set_title(
        "(a) Comparison of 10 km Travel Time during Morning and Evening Rush Hours across 22 Southeast Asian Cities (2025)",
        fontsize=13, fontweight="bold", loc="left"
    )
    axes[0].text(0.01, 0.92, "Morning rush hour", transform=axes[0].transAxes,
                 color="#4c78a8", fontsize=10, fontweight="bold")
    axes[0].text(0.01, 0.04, "Evening rush hour", transform=axes[0].transAxes,
                 color="#6e6e6e", fontsize=10, fontweight="bold")
    label_diverging_bars(axes[0], m, e, fmt="{:.0f}")
    axes[0].legend(loc="upper right", frameon=False)

    m = df["morning_level_pct"].to_numpy()
    e = df["evening_level_pct"].to_numpy()
    axes[1].bar(x, m, color="#4c78a8", width=0.58, label="Morning rush hour")
    axes[1].bar(x, -e, color="#f28e2b", width=0.58, label="Evening rush hour")
    axes[1].axhline(0, color="0.3", lw=0.8)
    axes[1].set_ylabel("Time taken to travel 10 km (level, %)")
    axes[1].set_title(
        "(b) Comparison of 10 km Travel-Time Level during Morning and Evening Rush Hours across 22 Southeast Asian Cities (2025)",
        fontsize=13, fontweight="bold", loc="left"
    )
    axes[1].text(0.01, 0.92, "Morning rush hour", transform=axes[1].transAxes,
                 color="#4c78a8", fontsize=10, fontweight="bold")
    axes[1].text(0.01, 0.04, "Evening rush hour", transform=axes[1].transAxes,
                 color="#f28e2b", fontsize=10, fontweight="bold")
    label_diverging_bars(axes[1], m, e, fmt="{:.1f}%")
    axes[1].legend(loc="upper right", frameon=False)

    m = df["morning_speed_kmh"].to_numpy()
    e = df["evening_speed_kmh"].to_numpy()
    axes[2].bar(x, m, color="#4c78a8", width=0.58, label="Morning rush hour")
    axes[2].bar(x, -e, color="#59a14f", width=0.58, label="Evening rush hour")
    axes[2].axhline(0, color="0.3", lw=0.8)
    axes[2].set_ylabel("Average speed (km/h)")
    axes[2].set_title(
        "(c) Comparison of Average Speed during Morning and Evening Rush Hours across 22 Southeast Asian Cities (2025)",
        fontsize=13, fontweight="bold", loc="left"
    )
    axes[2].text(0.01, 0.92, "Morning rush hour", transform=axes[2].transAxes,
                 color="#4c78a8", fontsize=10, fontweight="bold")
    axes[2].text(0.01, 0.04, "Evening rush hour", transform=axes[2].transAxes,
                 color="#59a14f", fontsize=10, fontweight="bold")
    label_diverging_bars(axes[2], m, e, fmt="{:.1f}")
    axes[2].legend(loc="upper right", frameon=False)

    axes[2].set_xticks(x)
    axes[2].set_xticklabels(df["city"], rotation=45, ha="right")
    add_country_group_labels(axes[2], plot_order, country_by_city, y_line=-0.50, y_text=-0.58)

    for ax in axes:
        lim = max(ax.get_ylim()[1], abs(ax.get_ylim()[0]))
        ax.set_ylim(-lim * 1.06, lim * 1.06)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    plt.subplots_adjust(bottom=0.22, top=0.96)
    plt.savefig(OUTPUT_PNG, bbox_inches="tight")
    plt.close()
    print(f"Saved: {OUTPUT_PNG}")

if __name__ == "__main__":
    main()
