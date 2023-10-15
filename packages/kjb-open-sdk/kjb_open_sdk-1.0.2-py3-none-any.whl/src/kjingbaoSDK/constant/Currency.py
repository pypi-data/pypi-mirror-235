"""
@version: python3.11
@author: 章鱼
@time: 2023/10/07 2023/10/7
"""

from enum import Enum


class Currency(str, Enum):
    CNY = "CNY"  # "人民币"
    EUR = "EUR"  # "欧元"
    GBP = "GBP"  # "英镑"
    HKD = "HKD"  # "港元"
    USD = "USD"  # "美元"
    CAD = "CAD"  # "加拿大元"
    CHF = "CHF"  # "瑞士法郎"
    JPY = "JPY"  # "日元"

