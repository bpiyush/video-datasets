"""Stores all relevant paths for the dataset"""
from os.path import join


DATASET_ROOT = "/ssd/pbagad/datasets/rvos"


def get_videos_dir(mode="valid") -> str:
    """Returns the path to the videos of the given mode"""
    return join(DATASET_ROOT, mode, "JPEGImages")


def get_annotations_dir(mode="valid") -> str:
    """Returns the path to the annotations of the given mode"""
    return join(DATASET_ROOT, mode, "Annotations")


def get_meta_path(mode="valid") -> str:
    """Returns the path to the meta file of the given mode"""
    return join(DATASET_ROOT, mode, "meta.json")


def get_expressions_path(mode="valid") -> str:
    """Returns the path to the expressions file of the given mode"""
    return join(DATASET_ROOT, "meta_expressions", mode, "meta_expressions.json")
