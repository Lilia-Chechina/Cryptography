# Условие (ЛР1, п.2.1–2.3):
# Спроектируйте интерфейс расширения ключа: на вход подаётся ключ (массив байтов), на выходе — массив
# раундовых ключей (каждый ключ — массив байтов). Спроектируйте интерфейс шифрующего преобразования:
# входной блок и раундовый ключ — массивы байтов, результат — выходной блок. Спроектируйте интерфейс
# симметричного алгоритма для шифрования и дешифрования блока с предварительной настройкой ключей
# отдельным методом.

from abc import ABC, abstractmethod


class IKeySchedule(ABC):
    @abstractmethod
    def expand_key(self, master_key: bytes) -> list[bytes]:
        pass


class IRoundFunction(ABC):
    @abstractmethod
    def apply(self, half_block: bytes, round_key: bytes) -> bytes:
        pass


class ISymmetricCipher(ABC):
    @abstractmethod
    def encrypt_block(self, block: bytes) -> bytes:
        pass

    @abstractmethod
    def decrypt_block(self, block: bytes) -> bytes:
        pass

    @abstractmethod
    def setup_keys(self, key: bytes) -> None:
        pass
