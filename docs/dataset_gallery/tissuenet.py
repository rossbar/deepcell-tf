"""
=========
TissueNet
=========

A dataset for training cell segmentation models with more than 1 million
manually-labeled cells.
"""
# TODO: Update with preferred access pattern
from deepcell.datasets import fetch_data
fetch_data("tissuenet/tissuenet_v1.1.zip")
# sphinx_gallery_thumbnail_path = "images/tissuenet.png"
