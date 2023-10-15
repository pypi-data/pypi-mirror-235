"""
@version: python3.11
@author: 章鱼
@time: 2023/10/08 2023/10/8
"""
from pydantic import BaseModel


class PolicyLinkParamDTO(BaseModel):
    trackingNo: str

    kjbAccount: str = None

    thirdPartAccount: str = None

