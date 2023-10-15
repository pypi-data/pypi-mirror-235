"""
@version: python3.11
@author: 章鱼
@time: 2023/10/09
"""
from src.kjingbaoSDK.api.Encryption import Encryption
import datetime


class KJBConfig(object):
    def __init__(self, secretId: str, secretKey: str, serviceURL: str):
        self.secretId = secretId
        self.secretKey = secretKey
        self.serviceURL = serviceURL

    def getSign(self, now: datetime.datetime):

        return Encryption.md5(self.secretId + now.strftime('%Y%m%d%H%M%S') + self.secretKey)

