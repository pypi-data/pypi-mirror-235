"""
@version: python3.11
@author: 章鱼
@time: 2023/10/08 2023/10/8
"""
from pydantic import BaseModel


class PolicyInsuredApiDTO(BaseModel):
    # * 被保险人名称
    insuredName: str = None
    # * 证件类型代码
    certificateType: str = None

    certificateNo: str = None
    # * 联系电话
    mobile: str = None
    # * 联系地址
    contactAddress: str = None
