"""
@version: python3.11
@author: 章鱼
@time: 2023/10/07 2023/10/7
"""
from enum import Enum


class Packing(str, Enum):
    """
        包装类型
    """
    WOODEN_CASE = "001"  # "木箱"
    CARTON = "002"  # "纸箱"
    PALLETE = "020"  # "托盘"
    STANDARD_CONTAINER = "025"  # "集装箱"
    OTHER = "99"  # "其他"

