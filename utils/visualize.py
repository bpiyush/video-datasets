"""Helper functions for image processing and visualizations."""
from typing import Any
import colorsys
from matplotlib.transforms import Bbox

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mc
from matplotlib import rc
import seaborn as sns


def set_latex_fonts(usetex=True, fontsize=14, show_sample=False, **kwargs):
    try:
        plt.rcParams.update({
            "text.usetex": usetex,
            "font.family": "serif",
            "font.serif": ["Computer Modern Roman"],
            "font.size": fontsize,
            **kwargs,
        })
        if show_sample:
            plt.figure()
            plt.title("Sample $y = x^2$")
            plt.plot(np.arange(0, 10), np.arange(0, 10)**2, "--o")
            plt.grid()
            plt.show()
    except:
        print("Failed to setup LaTeX fonts. Proceeding without.")
        pass


def denormalize(x, mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]):
    """Denormalizes an image."""
    from torchvision import transforms

    mean = np.array(mean)
    std = np.array(std)
    denormalize_transform = transforms.Normalize(
        mean=-(mean / std),
        std=(1.0 / std),
    )

    return denormalize_transform(x)


def show_single_image(x, figsize=None, normalized=False, title="Sample image", xlabel="", show=True, ax=None, **imshow_kwargs):
    """Displays a single image."""

    assert len(x.shape) in [1, 3]
    
    if normalized:
        x = denormalize(x)
    
    if x.shape[0] == 3:
        x = x.permute((1, 2, 0))
    elif x.shape[0] == 1:
        x = x.squeeze(dim=0)
    else:
        raise ValueError("Unsupported shape: {}".format(x.shape))

    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)

    ax.imshow(x, **imshow_kwargs)
    ax.set_title(title, fontsize=16, fontweight="bold")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel(xlabel, fontsize=14)

    if show:
        plt.show()


def show_multiple_images(
        x: list,
        subtitles=None,
        n_cols=4,
        figsize=None,
        normalized=True,
        title="Sample images",
        save=False,
        path=None,
        subtitlesize=16,
        titlesize=18,
        show=True,
        return_figure=False,
    ):
    """Displays multiple images."""

    assert len(x) % n_cols == 0

    if normalized:
        x = [denormalize(x_i) for x_i in x]
    
    if subtitles is None:
        subtitles = [None] * len(x)

    n_rows = int(np.ceil(len(x) / n_cols))
    fig, axs = plt.subplots(n_rows, n_cols, figsize=figsize, constrained_layout=True)
    for i in range(len(x)):
        if n_rows == 1:
            ax = axs[i % n_cols]
        else:
            ax = axs[int(i / n_cols), i % n_cols]

        if x[i].shape[0] == 3:
            x[i] = x[i].permute((1, 2, 0))
        ax.imshow(x[i])
        ax.set_xticks([])
        ax.set_yticks([])
        if i < len(subtitles):
            ax.set_title(subtitles[i], fontsize=subtitlesize)

    plt.suptitle(title, fontsize=titlesize)

    if save:
        assert path is not None
        plt.savefig(path, bbox_inches="tight")

    if show:
        plt.show()
    
    if return_figure:
        return fig