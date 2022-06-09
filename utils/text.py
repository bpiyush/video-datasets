"""All helpers related to textual processing."""

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


# define some temporal prepositions
temporal_keywords = ["after", "before", "then", "while", "during", "as soon as"]


def check_in_caption(caption, keywords):
    """Checks if any of the given keywords occur in the caption."""
    caption = caption.lower()
    for word in keywords:
        if word.lower() in caption:
            return True
    return False


def filter_temporal_sentences(sentences: list, temporal_keywords: list):
    """Filters out sentences that contain any of the given temporal keywords."""
    return [
        sentence for sentence in sentences \
            if check_in_caption(sentence, temporal_keywords)
    ]


def get_temporal_sentences_by_keyword(sentences: list, temporal_keywords: list):
    """Gets sentences that contain any of the given temporal keywords."""
    temporal_sentences = dict()
    for keyword in tqdm(temporal_keywords, "Getting temporal sentences for keywords"):
        temporal_sentences[keyword] = filter_temporal_sentences(
            sentences, [keyword],
        )
    return temporal_sentences


def plot_distribution_of_temporal_sentences(
        temporal_sentences: dict, dataset_name: str,
        yoffsets=-400,
    ):
    
    if isinstance(yoffsets, int):
        yoffsets = [yoffsets for _ in range(len(temporal_sentences))]
    elif isinstance(yoffsets, list):
        assert len(yoffsets) == len(temporal_sentences)
    elif isinstance(yoffsets, dict):
        pass
    else:
        raise ValueError("yoffsets must be int or list or dict")

    # convert to dictinary
    keys = [k.capitalize() for k in temporal_sentences]

    if not isinstance(yoffsets, dict):
        values = yoffsets
        yoffsets = dict(zip(keys, values))
    else:
        for key in keys:
            if key not in yoffsets.keys():
                yoffsets[key] = -400

    fig, ax = plt.subplots(1, 1, figsize=(10, 7))

    counts = [len(temporal_sentences[k]) for k in temporal_sentences]

    indices = np.argsort(keys)
    counts = np.array(counts)[indices]
    keys = np.array(keys)[indices]

    ax.grid(alpha=0.5)
    ax.bar(keys, counts)
    ax.set_title(f"Distribution of temporal words in {dataset_name} captions", fontsize=15)
    ax.set_xlabel("Temporal keywords", fontsize=13)
    ax.set_ylabel("Frequency", fontsize=13)

    rects = ax.patches
    for i, rect, count in zip(keys, rects, counts):
        height = rect.get_height()
        yoffset = yoffsets[i]
        color = "white" if yoffset < 0 else "black"
        
        ax.text(
            rect.get_x() + rect.get_width() / 2, height + yoffset,
            count, ha="center", va="bottom", fontsize=13, color=color, weight='bold',
        )

    plt.show()


def plot_temporal_sentences_fraction(
        temporal_sentences_fraction: dict, dataset_name: str, dataset_size: int,
    ):
    # convert to dictinary
    keys = [k.capitalize() for k in temporal_sentences_fraction]
    counts = [v for k, v in temporal_sentences_fraction.items()]
    indices = np.argsort(keys)
    counts = np.array(counts)[indices]
    keys = np.array(keys)[indices]
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    ax.grid(alpha=0.5)
    ax.bar(keys, counts)
    ax.set_title(f"Distribution of temporal words in {dataset_name} captions", fontsize=15)
    ax.set_xlabel(f"Temporal keywords (Size: {dataset_size})", fontsize=13)
    ax.set_ylabel("Frequency", fontsize=13)

    plt.show()
