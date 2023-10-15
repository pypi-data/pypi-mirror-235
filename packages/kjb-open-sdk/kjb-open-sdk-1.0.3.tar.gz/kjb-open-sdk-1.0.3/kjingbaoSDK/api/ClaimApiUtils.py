"""
@version: python3.11
@author: 章鱼
@time: 2023/10/11 2023/10/11
"""
from kjingbaoSDK.ov.claim import *
from kjingbaoSDK.ov.KJBConfig import KJBConfig
import requests
import datetime
class ClaimApiUtils:
    @staticmethod
    def createClaimLink(claim_link: ClaimLinkParamDTO, config: KJBConfig):
        """
        创建一个理赔记录
        """
        timestamp = datetime.datetime.now()
        om = {'data': claim_link.model_dump(), 'sign': config.getSign(timestamp), 'timestamp': timestamp.strftime('%Y%m%d%H%M%S'), 'secretId': config.secretId}
        r = requests.post(config.serviceURL, json=om)
        return r

    @staticmethod
    def share(claim_share: ClaimShareDTO, config: KJBConfig):
        """查看一个理赔记录"""
        timestamp = datetime.datetime.now()
        om = {'data': claim_share.model_dump(), 'sign': config.getSign(timestamp),
              'timestamp': timestamp.strftime('%Y%m%d%H%M%S'), 'secretId': config.secretId}
        r = requests.post(config.serviceURL, json=om)
        return r


