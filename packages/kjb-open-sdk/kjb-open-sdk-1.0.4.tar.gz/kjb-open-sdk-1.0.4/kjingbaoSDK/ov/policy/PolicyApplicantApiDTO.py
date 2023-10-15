"""
@version: python3.11
@author: 章鱼
@time: 2023/10/08 2023/10/8
"""
from pydantic import BaseModel
from datetime import datetime


class PolicyApplicantApiDTO(BaseModel):
    # *投保人名称
    applicantName: str = None
    # *证件类型代码（101：身份证号；110：统一社会信用代码）
    certificateType: str = None
    # *证件号码
    certificateNo: str = None

    mobile: str = None
    # *联系人
    contact: str = None

    createTime: datetime = None

