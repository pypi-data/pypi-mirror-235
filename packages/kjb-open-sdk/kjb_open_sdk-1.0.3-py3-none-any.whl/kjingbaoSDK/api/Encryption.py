"""
@version: python3.11
@author: 章鱼
@time: 2023/10/09
"""
import hashlib


class Encryption:
    @staticmethod
    def md5(string: str):
        md5_hash = hashlib.md5()
        md5_hash.update(string.encode('utf-8'))
        return md5_hash.hexdigest()

