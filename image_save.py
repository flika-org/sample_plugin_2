import numpy as np
from qtpy import QtWidgets, QtCore, QtGui
import skimage.filters
import flika
flika_version = flika.__version__
from flika import global_vars as g
from flika.process.BaseProcess import BaseProcess
from flika.window import Window
from flika.process import generate_random_image
from scipy import ndimage
from flika.process.file_ import save_file

class SaveImage(BaseProcess):

    def __init__(self):
        super().__init__()

    def save(self):
        if g.currentWindow is None:
            generate_random_image(500, 128)
        save_file()

Image_to_save = SaveImage()



