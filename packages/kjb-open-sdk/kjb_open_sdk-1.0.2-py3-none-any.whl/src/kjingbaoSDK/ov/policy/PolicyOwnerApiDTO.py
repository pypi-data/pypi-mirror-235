"""
@version: python3.11
@author: 章鱼
@time: 2023/10/08 2023/10/8
"""
from pydantic import BaseModel


class PolicyOwnerApiDTO(BaseModel):
    # *货主
    owner: str = None
    # *证件类型代码（101：身份证号；110：统一社会信用代码）
    certificateType: str = None
    certificateNo: str = None
    # *联系电话
    mobile: str = None
    # *邮箱地址
    email: str = None
    # *联系地址
    contactAddress: str = None


