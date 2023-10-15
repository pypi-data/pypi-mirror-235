import enum
from enum import Enum


class CargoCategoryTraditional(str, Enum):
    CARGO_CATEGORY_0301 = "0301"  # "玻璃制品"
    CARGO_CATEGORY_0307 = "0307"  # "日用杂品类"
    CARGO_CATEGORY_0309 = "0309"  # "其他轻工品"
    CARGO_CATEGORY_0405 = "0405"  # "其它纺织品"
    CARGO_CATEGORY_0504 = "0504"  # "有色金属及其制品"
    CARGO_CATEGORY_0604 = "0604"  # "其它工艺品类"
    CARGO_CATEGORY_0708 = "0708"  # "其它设备"
    CARGO_CATEGORY_0810 = "0810"  # "其它电子产品"
    CARGO_CATEGORY_0911 = "0911"  # "其它化工品"
