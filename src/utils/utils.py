import os
import seaborn as sns
from src.constants import *
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize


def plot_bar(
    array, region, title, image_name, no2=False, figsize=(28, 8), minimum_val=20
):
    """This function plots the bar plot of the countries of the given region with PM10 or PM2.5 or NO2 values"""

    import warnings

    warnings.filterwarnings("ignore")

    plt.figure()

    fig, ax = plt.subplots(figsize=figsize)

    countries = array.groupby("country").mean().index
    countries_pm = array.groupby("country").mean().iloc[:, 0].values
    countries_pm = [round(pm, 2) for pm in countries_pm]

    norm = Normalize(vmin=min(countries_pm) - minimum_val, vmax=max(countries_pm))
    if no2:
        colors = plt.cm.BuGn(norm(countries_pm))
    else:
        colors = plt.cm.Blues(norm(countries_pm))

    bars = ax.barh(countries, countries_pm, color=colors)

    for country, pm in zip(countries, countries_pm):
        ax.text(pm, country, str(pm), va="center", fontsize=14)

    ax.tick_params(axis="x", labelsize=19)
    ax.tick_params(axis="y", labelsize=19)

    # Add a color bar to show the value-color mapping
    if no2:
        sm = plt.cm.ScalarMappable(cmap=plt.cm.BuGn, norm=norm)
    else:
        sm = plt.cm.ScalarMappable(cmap=plt.cm.Blues, norm=norm)
    sm.set_array([])
    colorbar = plt.colorbar(sm, ax=ax, label="Values")  # Specify ax=ax

    colorbar.ax.yaxis.label.set_size(19)
    colorbar.ax.yaxis.set_tick_params(labelsize=19)

    ax.set_title(f"Average value of {title} of {region} Countries", fontsize=29)
    plt.tight_layout()

    path = "static/" + IMAGE_DIR + "/" + BAR_PLOT_DIR
    os.makedirs(path, exist_ok=True)
    image_path = os.path.join(path, image_name)
    plt.savefig(image_path)


def plot_hist(df, column, color, plot_attr, bins, image_name, figsize=(9, 4)):
    plt.figure()
    plt.figure(figsize=figsize)
    sns.histplot(x=df[column], color=color, bins=bins)
    plt.title(f"Histogram plot of {plot_attr} with city ")
    # Saving the image file
    path = "static/" + IMAGE_DIR + "/" + HIST_PLOT_DIR
    os.makedirs(path, exist_ok=True)
    image_path = os.path.join(path, image_name)
    plt.savefig(image_path)


def plot_vertical_bar(
    df, column, year, color_pallete, image_name, bbox_val, legend_fontsize=8
):

    x_values = (
        df[df["Measurement Year"] == year].groupby("WHO Region")[column].mean().index
    )
    y_values = (
        df[df["Measurement Year"] == year].groupby("WHO Region")[column].mean().values
    )
    plt.figure()
    ax = sns.barplot(
        x=x_values,
        y=y_values,
        hue=x_values,
        errorbar=None,
        orient="vertical",
        palette=color_pallete,
        saturation=1.7,
        dodge=False,
        alpha=0.9,
    )

    plt.xticks([])
    plt.xlabel("WHO Region")
    plt.ylabel(f"Mean {column}")

    legend_handles = [
        plt.bar(
            0, 0, align="center", color=sns.color_palette(color_pallete)[i], label=label
        )
        for i, label in enumerate(x_values)
    ]

    # Adding legend with manual legend handles
    plt.legend(
        handles=legend_handles,
        title="WHO Region",
        loc="center",
        bbox_to_anchor=bbox_val,
        fontsize=legend_fontsize,
    )

    for i, v in enumerate(y_values):
        plt.text(
            i,
            round(v + 0.3, 2),
            str(round(v, 2)),
            color="black",
            ha="center",
            va="bottom",
            fontsize=9.2,
        )
    plt.title(year)

    path = "static/" + IMAGE_DIR + "/" + V_BAR_PLOT_DIR
    os.makedirs(path, exist_ok=True)
    image_path = os.path.join(path, image_name)
    plt.savefig(image_path)
