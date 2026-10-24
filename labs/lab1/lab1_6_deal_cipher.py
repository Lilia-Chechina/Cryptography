# Условие (ЛР1, п.6):
# Реализуйте алгоритм шифрования DEAL на базе класса сети Фейстеля из задания 3, определив собственные
# реализации интерфейсов расписания ключей и раундового преобразования.

from labs.lab1.lab1_6_deal_key_schedule import DEALKeySchedule
from labs.lab1.lab1_6_deal_adapter import DESAdapter
from labs.lab1.lab1_3_feistel_cipher import FeistelCipher


class DEAL(FeistelCipher):

    BLOCK_SIZE = 16

    def __init__(self, key_size: int = 128):
        if key_size not in (128, 192, 256):
            raise ValueError("Key size must be 128, 192, or 256 bits")

        self.key_size_bits = key_size
        self.num_rounds = 6 if key_size in (128, 192) else 8

        key_schedule = DEALKeySchedule(key_size_bits=key_size)
        round_function = DESAdapter()

        super().__init__(
            key_schedule=key_schedule,
            round_function=round_function,
            block_size=self.BLOCK_SIZE,
            num_rounds=self.num_rounds,
        )
