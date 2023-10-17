import hashlib
import random
import re
import time


class Utils:
    """工具类"""

    @staticmethod
    def get_sign(data: str) -> str:
        """
        计算 QQ 音乐的 sign 值。
        来源于 https://github.com/Superheroff/musicapi/blob/main/musicapi.py

        Args:
            data : 待加密的数据。

        Returns:
            str: 计算后的 sign 值。
        """
        k1 = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "A": 10,
            "B": 11,
            "C": 12,
            "D": 13,
            "E": 14,
            "F": 15,
        }
        l1 = [
            212,
            45,
            80,
            68,
            195,
            163,
            163,
            203,
            157,
            220,
            254,
            91,
            204,
            79,
            104,
            6,
        ]
        t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
        md5 = hashlib.md5(data.encode()).hexdigest().upper()
        t1 = "".join([md5[i] for i in [21, 4, 9, 26, 16, 20, 27, 30]])
        t3 = "".join([md5[i] for i in [18, 11, 3, 2, 1, 7, 6, 25]])
        ls2 = []
        for i in range(16):
            x1 = k1[md5[i * 2]]
            x2 = k1[md5[i * 2 + 1]]
            x3 = ((x1 * 16) ^ x2) ^ l1[i]
            ls2.append(x3)
        ls3 = []
        for i in range(6):
            if i == 5:
                ls3.append(t[ls2[-1] >> 2])
                ls3.append(t[(ls2[-1] & 3) << 4])
            else:
                x4 = ls2[i * 3] >> 2
                x5 = (ls2[i * 3 + 1] >> 4) ^ ((ls2[i * 3] & 3) << 4)
                x6 = (ls2[i * 3 + 2] >> 6) ^ ((ls2[i * 3 + 1] & 15) << 2)
                x7 = 63 & ls2[i * 3 + 2]
                ls3.extend(t[x4] + t[x5] + t[x6] + t[x7])
        t2 = "".join(ls3)
        t2 = re.sub(r"[\\/+\']", "", t2)
        sign = f"zzb{(t1 + t2 + t3).lower()}"
        return sign

    @staticmethod
    def random_string(length: int, chars: str) -> str:
        """
        获取指定长度的随机字符串。

        Args:
            length: 字符串长度。
            chars: 字符集。

        Returns:
            str: 指定长度的随机字符串。
        """
        return "".join(random.choices(chars, k=length))

    @staticmethod
    def calc_md5(*multi_string) -> str:
        """
        计算 MD5 哈希值。

        Args:
            multi_string: 多个字符串参数。

        Returns:
            str: MD5 哈希值的字符串形式。
        """
        md5 = hashlib.md5()
        for s in multi_string:
            md5.update(s if isinstance(s, bytes) else s.encode())
        return md5.hexdigest()

    @staticmethod
    def get_ptqrtoken(qrsig: str) -> int:
        """
        计算 ptqrtoken。

        Args:
            qrsig: 输入字符串。

        Returns:
            int: ptqrtoken 的整数形式。
        """
        e = 0
        for c in qrsig:
            e += (e << 5) + ord(c)
        return 2147483647 & e

    @staticmethod
    def get_token(p_skey: str) -> int:
        """
        计算 g_tk。

        Args:
            p_skey: 输入字符串。

        Returns:
            int: g_tk 的整数形式。
        """
        h = 5381
        for c in p_skey:
            h += (h << 5) + ord(c)
        return 2147483647 & h

    @staticmethod
    def random_uuid() -> str:
        """
        生成随机 UUID。

        Returns:
            str: 随机 UUID 的字符串形式。
        """
        uuid_string = "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx"

        def callback(c: str) -> str:
            r = random.randint(0, 15)
            v = r if c == "x" else (r & 0x3 | 0x8)
            return hex(v)[2:]

        return "".join(
            [callback(c) if c in ["x", "y"] else c for c in uuid_string]
        ).upper()

    @staticmethod
    def gen_searchID() -> str:
        """
        生成搜索ID。

        Returns:
            str: 搜索ID。
        """
        e = random.randint(1, 20)
        t = e * 18014398509481984
        n = random.randint(0, 4194304) * 4294967296
        a = time.time()
        r = round(a * 1000) % (24 * 60 * 60 * 1000)
        return str(t + n + r)
