import os
import time
from collections import OrderedDict


from PIL import Image
import numpy as np
import tensorflow as tf


import vgg


CONTENT_LAYERS = ('relu4_2', 'relu5_2')
STYLE_LAYERS = ('relu1_1', 'relu2_1', 'relu3_1', 'relu4_1', 'relu5_1')


try:
  reduce
except NameError:
  from functools import reduce

  def get_loss_vals(loss_store):
    return OrderedDict