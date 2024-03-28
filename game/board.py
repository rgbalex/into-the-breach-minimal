import numpy as np

from enemies import *
from tiles import *


class Board:
    _board = np.array(object=BaseTile, shape=(8, 8))
