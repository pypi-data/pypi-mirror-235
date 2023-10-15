"""
@version: python3.11
@author: 章鱼
@time: 2023/10/07 2023/10/7
"""
from pydantic import BaseModel, field_validator
from kjingbaoSDK.constant import *
from kjingbaoSDK.ov.policy.PolicyApplicantApiDTO import PolicyApplicantApiDTO
from kjingbaoSDK.ov.policy.PolicyInsuredApiDTO import PolicyInsuredApiDTO
from kjingbaoSDK.ov.policy.PolicyAttachmentApiDTO import PolicyAttachmentApiDTO
from kjingbaoSDK.ov.policy.PolicyOwnerApiDTO import PolicyOwnerApiDTO
from kjingbaoSDK.ov.policy.InsuranceRiskApiDTO import InsuranceRiskApiDTO
from datetime import datetime
from typing import List, Union


class PolicyApiDTO(BaseModel):
    # *原单号 (第三方系统的唯一编号，或称系统跟踪号)
    trackingNo: str
    # 被保险人名称 (填发货人或者贵司全称（与营业执照一致）。)
    insuredName: str = None
    owner: str = None
    # 货值
    cargoValue: float = None
    # 货值币别
    currencyCode: Currency = None
    freight: float = None
    # 运费币种
    freightCurrencyCode: Currency = None
    # 保额确定方式 (货值*加成比例或货值+运费见基础数据<保费确定方式>)
    baseAmountWay: BaseAmountWay = None
    # 投保比例（%）(根据运输方式1、海运和陆运最高110%； 2、空运和快递最高130%；3、如果选择货值+运费方式投保，那么无加成比例即为100%；根据实际情况选择比例)
    ratio: float = None
    # 计费重量
    chargeableWeight: float = None
    # *备注
    remark: str = None
    # 保险产品名称
    productName: str = None
    # 保险产品code
    productCode: str = None
    # *运输方式（代码）
    transportModeCode: TransportMode = None
    # *运输工具及航次 (海运填船名航次；空运填航班号；铁路填车次号；公路填车牌号；全程快递不用填；多式联运填上述组合方式 如果上述信息拿不到，可用原单号代替)
    transportTool: str = None
    # 提单号/运单号 (海运填船东提单号或货代分单号；空运填航司运单号或货代分单号；铁路填铁路运单号；公路填公路运单号；全程快递填快递单号；多式联运填上述组合方式如果提单拿不到，可用柜号或者原单号代替)
    blNo: str = None
    # *派送方式
    deliverywayCode: Deliveryway = None
    # 快递公司Code
    expressCompanyCode: ExpressCompany = None
    # 快递单号 (快递派必填。如果国内打单，填实际快递单号；如果国外打单，填“海外打单”四个字)
    expressNo: str = None
    # *shipment (目的地是以下海外仓的为必填，其他为选填：FBA，菜鸟海外仓，京东仓，易达，谷仓，万邑通，4PX，Cdiscount。)
    shipmentId: str = None
    # *包装类型
    packingCode: Packing = None

    @field_validator("packingCode", mode='before')
    def packingCode_validate(cls, value):
        if value == '木箱':
            return Packing.WOODEN_CASE.value
        elif value == '纸箱':
            return Packing.CARTON.value
        elif value == '托盘':
            return Packing.PALLETE.value
        elif value == '集装箱':
            return Packing.STANDARD_CONTAINER.value
        elif value == '其他':
            return Packing.OTHER.value
        else:
            return value
    # *包装数量
    packingQuantity: int = None
    # *货描
    cargoDesc: str = None
    # *货物种类
    cargoCategoryCode: Union[CargoCategory, CargoCategoryTraditional]= None
    # *起运时间
    departureDate: int = None

    @field_validator("departureDate", mode='before')
    def validate(cls, value):
        if isinstance(value, datetime):
            return int(value.timestamp() * 1000)
        if isinstance(value, int):
            if len(str(value)) == 13:
                return value
            else:
                raise ValueError("departureDate: 日期格式错误, 请传13位时间戳或者datetime类型")
    # 起运国(国家二字码或三字码)
    departureCountryCode: str = None
    # 起运地
    departureAddress: str = None
    # 目的地类型
    destType: DestType = None
    # 目的国(国家二字码或三字码)
    destinationCountryCode: str = None
    # *目的地(填写最终的目的地详细地址，含街道门牌等。目的地是亚马逊的，可填写仓库代码，例如ONT8。)
    destinationAddress: str = None
    # *中转国
    transferCountryCode: str = None
    transferAddress: str = None
    @field_validator("departureCountryCode", "destinationCountryCode", "transferCountryCode")
    def CountryCode_validate(cls, value):
        if len(value) > 3:
            raise ValueError("国家code支持: 国家二字码或三字码型")
        else:
            return value
    # *上架类型(1、保上架（整箱）的仓库有FBA，菜鸟海外仓，京东仓，易达，谷仓，万邑通，4PX，Cdiscount；2、保上架（整箱/单个）的仓库只有FBA（有限开放，若要使用请跟商务确认）3、其他海外仓和非海外仓，只能选不保上架)
    shelfType: str = None
    # *上架地
    shelfName: str = None
    # *数据权限用
    kjbAccount: str = None
    # *新增（第三方系统账号，比如宇腾的userId，kjbAccount和thirdPartAccount必须传一个，如果都传以kjbAccount为准）
    thirdPartAccount: str = None
    # *暴动保障
    unrestRisk: bool = None
    # *投保人信息
    applicantInfo: PolicyApplicantApiDTO = None
    # *被保险人信息
    insuredInfo: PolicyInsuredApiDTO = None
    # *货主信息
    ownerInfo: PolicyOwnerApiDTO = None
    # *附件
    attachmentList: List[PolicyAttachmentApiDTO] = None
    # 是否需要仓至仓条款
    whsToWhs: bool = False
    # 起运日期显示方式True: 同起运日 false：AS PER B/L 默认：同起运日
    departureDateFlag: bool = None
    # 赔付地 默认地址:HANGZHOU China
    claimSite: str = None
    # 信用证号
    creditNo: str = None
    # 信用证条款
    creditLetter: str = None
    # *发票号码
    invoiceNo: str = None
    # *销售合同号
    bargainNo: str = None
    # *保险条款
    insuranceRiskList: List[InsuranceRiskApiDTO] = None
    # 汇率
    exchangeRate: float = None
    # 保险金额
    sumInsured: float = None
    # 保险金额（人民币）
    rmbSumInsured: float = None
    # *费率千分之几
    feeRate: float = None
    # *保费
    premium: float = None
    rmbPremium: float = None
    # *保险起期
    startDate: datetime = None
    # *投保时间
    proposalDate: datetime = None
    # *保单号
    policyNo: str = None
    # *电子保单地址
    policyUrl: str = None
    # *审核状态（0 核保中 1 初审通过 2：拒绝; 10：已承保）
    status: int = None
    enable: bool = None
    # *提单号
    ladingNo: str = None
    # *派送方式 value
    deliverywayValue: str = None
    departureCountryValue: str = None
    departureCity: str = None
    destinationCountryValue: str = None
    destinationCity: str = None
    # *唛头
    cargoMarks: str = None

    # *货物种类
    cargoCategoryValue: str = None
    # *批改理由
    amendmentReason: str = None
    # *审核拒绝原因
    reason: str = None
    # *跨境堡投保单号
    uniqueCode: str = None
    # *特色版 非海外仓 订单编号
    orderNo: str = None
    # *战争险开关
    warRisk: bool = None
    callbackUrl: str = None
    # *物流渠道商
    logisticsChannel: str = None


