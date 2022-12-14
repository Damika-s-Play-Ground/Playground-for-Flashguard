import os
import numpy as np
from metavision_sdk_core import BaseFrameGenerationAlgorithm
from metavision_core.event_io import EventsIterator
import metavision_sdk_cv
import cv2

from ipywidgets import interact
from PIL import Image

def display_sequence(images):
    def _show(frame=(0, len(images)-1)):
        return Image.fromarray(images[frame])
    interact(_show)