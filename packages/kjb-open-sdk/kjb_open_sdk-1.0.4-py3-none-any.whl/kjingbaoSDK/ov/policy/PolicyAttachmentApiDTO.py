"""
@version: python3.11
@author: 章鱼
@time: 2023/10/08 2023/10/8
"""
from pydantic import BaseModel


class PolicyAttachmentApiDTO(BaseModel):
    # *文件路径 (外网可访问的文件路径（若没有，则可先调用上传接口，得到路径）)
    url: str
    # *文件类型
    # Application：批改申请书
    # guarantee_letter：无货损保函
    # InsureAttachedFileExpressNo：投保信息附件（快递单号）
    # InsureAttachedFileCargoDesc：投保信息附件（货物描述）
    # Fragile：易碎品内包装图片
    type: str
    # *备注
    remake: str = None
