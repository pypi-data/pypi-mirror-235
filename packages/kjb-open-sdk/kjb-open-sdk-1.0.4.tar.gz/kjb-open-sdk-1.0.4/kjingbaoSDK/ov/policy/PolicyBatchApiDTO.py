"""
@version: python3.11
@author: 章鱼
@time: 2023/10/08 2023/10/8
"""
from pydantic import BaseModel
from kjingbaoSDK.ov.policy.PolicyApiDTO import PolicyApiDTO
from typing import List


class PolicyBatchApiDTO(BaseModel):

    policyList: List[PolicyApiDTO] = None

    kjbAccount: str = None

    thirdPartAccount: str = None
