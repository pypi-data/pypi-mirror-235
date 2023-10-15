"""
@version: python3.11
@author: 章鱼
@time: 2023/10/07 2023/10/7
"""
from enum import Enum


class Deliveryway(str, Enum):
    PENDING = "0"  # "待定"
    EXPRESS = "1"  # "快递派"
    TRUCK = "2"  # "卡车派"
    POSTAL = "3"  # "邮政派"

