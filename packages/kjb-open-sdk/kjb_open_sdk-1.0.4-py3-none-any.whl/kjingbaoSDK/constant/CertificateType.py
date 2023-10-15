from enum import Enum


class CertificateType(str, Enum):
    PID = '101'  # '身份证号'
    ECOMPANY_IDUR = '110'  # '统一信用代码'
