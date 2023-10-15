"""
@version: python3.11
@author: 章鱼
@time: 2023/10/07 2023/10/7
"""
from pydantic import BaseModel


class ClaimLinkParamDTO(BaseModel):

    trackingNo: str
    kjbAccount: str = None
    thirdPartAccount: str = None
