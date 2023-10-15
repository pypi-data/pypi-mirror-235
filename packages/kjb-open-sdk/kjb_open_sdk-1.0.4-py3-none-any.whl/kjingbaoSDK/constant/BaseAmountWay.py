from enum import Enum


class BaseAmountWay(str, Enum):

    VALUE = '01'  # '货值*加成比例'
    VALUE_AND_FREIGHT = '02'  # '货值+运费'
