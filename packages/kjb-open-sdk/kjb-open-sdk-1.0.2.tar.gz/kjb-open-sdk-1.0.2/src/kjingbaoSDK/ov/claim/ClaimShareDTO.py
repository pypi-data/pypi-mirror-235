"""
@version: python3.11
@author: 章鱼
@time: 2023/10/08 2023/10/8
"""
from pydantic import BaseModel


class ClaimShareDTO(BaseModel):
    # 保单号
    policyNo: str
    # 原单号
    trackingNo: str
    # 展示报案信息
    showReportInfo: bool = True
    # 展示理赔状态信息
    showCliamStatusInfo: bool = True
    # 展示查勘状态信息
    showSurveyStatusInfo: bool = True
    # 展示理算信息
    showAdjustmentInfo: bool = True
    # 展示调查结果
    showSurveyResultInfo: bool = True
    # 展示理赔金额赔付信息
    showClaimAmountInfo: bool = True
    # 展示理赔资料信息
    showClaimDataInfo: bool = True
