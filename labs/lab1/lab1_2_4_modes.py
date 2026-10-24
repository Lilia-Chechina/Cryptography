# Условие (ЛР1, п.2.4):
# Режим шифрования задаётся перечислением: ECB, CBC, PCBC, CFB, OFB, CTR или Random Delta. Режим
# набивки задаётся перечислением: Zeros, ANSI X.923, PKCS7 или ISO 10126.

from enum import Enum, auto


class CipherMode(Enum):
    ECB = auto()
    CBC = auto()
    PCBC = auto()
    CFB = auto()
    OFB = auto()
    CTR = auto()
    RANDOM_DELTA = auto()


class PaddingMode(Enum):
    ZEROS = auto()
    ANSI_X923 = auto()
    PKCS7 = auto()
    ISO_10126 = auto()
