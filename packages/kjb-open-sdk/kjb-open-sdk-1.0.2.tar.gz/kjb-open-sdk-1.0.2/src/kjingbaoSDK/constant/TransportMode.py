"""
@version: python3.11
@author: 章鱼
@time: 2023/10/07 2023/10/7
"""
from enum import Enum


class TransportMode(str, Enum):
    """
        干线运输方式
    """
    SEA = "01"  # "海运"
    AIR = "02"  # "空运"
    ROAD = "03"  # "公路"
    RAILWAY = "04"  # "铁路"
    POSTAL = "05"  # "全程邮政"
    EXPRESS = "06"  # "全程快递"
    COMBINE = "07"  # "多式联运"
