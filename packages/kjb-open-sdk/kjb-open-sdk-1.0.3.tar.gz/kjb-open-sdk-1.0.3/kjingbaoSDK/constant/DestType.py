"""
@version: python3.11
@author: 章鱼
@time: 2023/10/07 2023/10/7
"""
from enum import Enum


class DestType(str, Enum):
    FBA = "FBA"  # "FBA"
    CAINIAO = "CAINIAO"  # "菜鸟海外仓"
    OVERSEAS = "OVERSEAS"  # "其他海外仓"
    NOT_OVERSEAS = "NOT_OVERSEAS"  # "非海外仓"


