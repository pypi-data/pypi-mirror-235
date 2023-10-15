"""
@version: python3.11
@author: 章鱼
@time: 2023/10/09 2023/10/9
"""
from kjingbaoSDK.ov.policy import *
from kjingbaoSDK.ov.KJBConfig import KJBConfig
import requests, json
import datetime
class PolicyApiUtils:
    @staticmethod
    def createDraftLink(policy: PolicyApiDTO, config: KJBConfig):

        timestamp = datetime.datetime.now()
        om = {'data': policy.model_dump(), 'sign': config.getSign(timestamp), 'timestamp': timestamp.strftime('%Y%m%d%H%M%S'), 'secretId':config.secretId}
        r = requests.post(config.serviceURL, json=om)
        return r

    @staticmethod
    def createBatchDraftLink(policyBatchApiDTO: PolicyBatchApiDTO, config: KJBConfig):
        timestamp = datetime.datetime.now()
        om = {'data': policyBatchApiDTO.model_dump(), 'sign': config.getSign(timestamp),
              'timestamp': timestamp.strftime('%Y%m%d%H%M%S'), 'secretId': config.secretId}
        r = requests.post(config.serviceURL, json=om)
        return r

    @staticmethod
    def createPolicyLink(policyLinkParamDTO: PolicyLinkParamDTO, config: KJBConfig):
        timestamp = datetime.datetime.now()
        om = {'data': policyLinkParamDTO.model_dump(), 'sign': config.getSign(timestamp),
              'timestamp': timestamp.strftime('%Y%m%d%H%M%S'), 'secretId': config.secretId}
        r = requests.post(config.serviceURL, json=om)
        return r
