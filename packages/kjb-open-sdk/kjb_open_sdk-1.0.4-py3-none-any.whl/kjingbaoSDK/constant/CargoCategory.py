import enum
from enum import Enum


class CargoCategory(str, Enum):
    NORMAL = '01'  # '无易碎品'
    FRAGILE = '02'  # '是易碎品'

