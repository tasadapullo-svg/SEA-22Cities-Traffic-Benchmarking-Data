# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import seaborn as sns
from scipy import stats
import numpy as np

INPUT_CSV = "figure5_regression_dataset.csv"
OUTPUT_PNG = "figure5_regression_relationships.png"

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

country_colors = {
    "Indonesia": "#4c78a8",
    "Malaysia": "#59a14f",
    "Philippines": "#e15759",
    "Singapore": "#b07aa1",
    "Thailand": "#f28e2b",
    "Vietnam": "#76b7b2",
}
country_markers = {
    "Indonesia": "o",
    "Malaysia": "^",
    "Philippines": "o",
    "Singapore": "D",
    "Thailand": "s",
    "Vietnam": "P",
}

def scatter_by_country(ax, data, xcol, ycol):
    for country in ["Indonesia", "Malaysia", "Philippines", "Singapore", "Thailand", "Vietnam"]:
        d = data[data["country"] == country]
        ax.scatter(
            d[xcol], d[ycol],
            s=70,
            marker=country_markers[country],
            color=country_colors[country],
            edgecolor="0.3",
            linewidth=0.6,
            label=country,
            zorder=3
        )

def main():
    df = pd.read_csv(INPUT_CSV)

    if "road_length_per_1000_people_km" not in df.columns:
        df["road_length_per_1000_people_km"] = df["road_length_km"] / df["population"] * 1000

    fig, axes = plt.subplots(1, 3, figsize=(20, 7))
    plt.subplots_adjust(right=0.82, wspace=0.32)

    ax = axes[0]
    scatter_by_country(ax, df, "population_density_per_km2", "average_congestion_pct")
    x = np.log10(df["population_density_per_km2"].to_numpy())
    y = df["average_congestion_pct"].to_numpy()
    coef = np.polyfit(x, y, 2)
    xx = np.linspace(x.min(), x.max(), 300)
    yy = np.polyval(coef, xx)
    resid = y - np.polyval(coef, x)
    band = resid.std(ddof=1)
    ax.plot(10 ** xx, yy, color="black", lw=2)
    ax.fill_between(10 ** xx, yy - band, yy + band, color="0.75", alpha=0.25, zorder=1)
    ax.set_xscale("log")
    ax.set_xlabel("Population density (persons/km², log scale)")
    ax.set_ylabel("Average congestion level (%)")
    ax.set_title("(a)", loc="left", fontsize=20, fontweight="bold")
    lin = stats.linregress(np.log10(df["population_density_per_km2"]), df["average_congestion_pct"])
    ax.text(
        0.98, 0.98, f"$R^2$ = {lin.rvalue**2:.3f}\np = {lin.pvalue:.3f}",
        transform=ax.transAxes, ha="right", va="top",
        bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="0.3")
    )
    for city, offset in {"Manila": (10, 6), "Kuala Lumpur": (10, -12)}.items():
        r = df.loc[df["city"] == city].iloc[0]
        ax.annotate(city, (r["population_density_per_km2"], r["average_congestion_pct"]),
                    textcoords="offset points", xytext=offset, fontsize=9)

    ax = axes[1]
    scatter_by_country(ax, df, "motor_vehicles_per_1000_people", "average_travel_time_10km_sec")
    sns.regplot(
        data=df, x="motor_vehicles_per_1000_people", y="average_travel_time_10km_sec",
        scatter=False, ci=95, color="black", line_kws={"lw": 2}, ax=ax
    )
    ax.set_xlabel("Motor vehicles per 1,000 people")
    ax.set_ylabel("Average travel time for a 10 km drive (s)")
    ax.set_title("(b)", loc="left", fontsize=20, fontweight="bold")
    lin = stats.linregress(df["motor_vehicles_per_1000_people"], df["average_travel_time_10km_sec"])
    ax.text(
        0.98, 0.98, f"$R^2$ = {lin.rvalue**2:.3f}\np = {lin.pvalue:.3f}",
        transform=ax.transAxes, ha="right", va="top",
        bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="0.3")
    )
    for city, offset in {"Manila": (8, 8), "Kajang": (8, -12)}.items():
        r = df.loc[df["city"] == city].iloc[0]
        ax.annotate(city, (r["motor_vehicles_per_1000_people"], r["average_travel_time_10km_sec"]),
                    textcoords="offset points", xytext=offset, fontsize=9)

    ax = axes[2]
    scatter_by_country(ax, df, "road_length_per_1000_people_km", "average_speed_kmh")
    sns.regplot(
        data=df, x="road_length_per_1000_people_km", y="average_speed_kmh",
        scatter=False, ci=95, color="black", line_kws={"lw": 2}, ax=ax
    )
    ax.set_xlabel("Road length per 1,000 people (km)")
    ax.set_ylabel("Average speed (km/h)")
    ax.set_title("(c')", loc="left", fontsize=20, fontweight="bold")
    lin = stats.linregress(df["road_length_per_1000_people_km"], df["average_speed_kmh"])
    ax.text(
        0.98, 0.98, f"$R^2$ = {lin.rvalue**2:.3f}\np = {lin.pvalue:.3f}",
        transform=ax.transAxes, ha="right", va="top",
        bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="0.3")
    )
    for city, offset in {"Manila": (8, -12), "Kuala Lumpur": (8, 8), "Kajang": (8, -12)}.items():
        r = df.loc[df["city"] == city].iloc[0]
        ax.annotate(city, (r["road_length_per_1000_people_km"], r["average_speed_kmh"]),
                    textcoords="offset points", xytext=offset, fontsize=9)

    legend_handles = [
        Line2D([0], [0], marker=country_markers[c], color="w",
               markerfacecolor=country_colors[c], markeredgecolor="0.3",
               markeredgewidth=0.6, markersize=8, linestyle="None", label=c)
        for c in ["Indonesia", "Malaysia", "Philippines", "Singapore", "Thailand", "Vietnam"]
    ]
    fig.legend(
        handles=legend_handles, title="Country key",
        loc="center left", bbox_to_anchor=(0.835, 0.67),
        frameon=False, title_fontsize=13
    )
    fig.text(0.835, 0.41, "Highlighted cities\nManila\nKuala Lumpur\nKajang",
             ha="left", va="top", fontsize=11)

    for ax in axes:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    plt.savefig(OUTPUT_PNG, bbox_inches="tight")
    plt.close()
    print(f"Saved: {OUTPUT_PNG}")

if __name__ == "__main__":
    main()
