"""
@version: python3.11
@author: 章鱼
@time: 2023/10/07 2023/10/7
"""
from enum import Enum


class ExpressCompany(str, Enum):
    UPS = "UPS"
    TNT = "TNT"
    FEDEX = "FEDEX"
    DPD = "DPD"
    DHL = "DHL"
    OTHER = "OTHER"  # "其他"

