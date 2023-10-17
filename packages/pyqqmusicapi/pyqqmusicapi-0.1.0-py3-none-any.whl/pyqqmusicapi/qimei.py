import base64
import datetime
import json
import random
import time
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple

import requests
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from .utils import Utils

PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDEIxgwoutfwoJxcGQeedgP7FG9qaIuS0qzfR8gWkrkTZKM2iWHn2ajQpBRZjMSoSf6+KJGvar2ORhBfpDXyVtZCKpqLQ+FLkpncClKVIrBwv6PHyUvuCb0rIarmgDnzkfQAqVufEtR64iazGDKatvJ9y6B9NMbHddGSAUmRTCrHQIDAQAB
-----END PUBLIC KEY-----"""


@dataclass
class QImeiResult:
    """获取QImei返回结果"""

    q16: str  # Qimei16
    q36: str  # Qimei36


def rsa_encrypt(content: bytes) -> bytes:
    """
    使用RSA算法对数据进行加密

    Args:
        data(bytes): 待加密的数据

    Returns:
        bytes: 加密后的数据
    """
    key = serialization.load_pem_public_key(PUBLIC_KEY.encode())
    return key.encrypt(content, padding.PKCS1v15())


class AES:
    block_size = 16

    def __init__(self, key: bytes):
        self._cipher = Cipher(algorithms.AES(key), modes.CBC(key))

    @staticmethod
    def _pad(v: bytes) -> bytes:
        padding_size = AES.block_size - len(v) % AES.block_size
        return v + (padding_size * chr(padding_size)).encode()

    @staticmethod
    def _unpad(v: bytes) -> bytes:
        return v[: -v[-1]]

    def encrypt(self, content: bytes) -> bytes:
        enc = self._cipher.encryptor()
        return enc.update(self._pad(content)) + enc.finalize()

    def decrypt(self, content: bytes) -> bytes:
        dec = self._cipher.decryptor()
        return self._unpad(dec.update(content) + dec.finalize())


class Qimei:
    APP_KEY = "0AND0HD6FE4HY80F"
    SECRET = "ZdJqM15EeO2zWc08"

    @staticmethod
    def gen_query(device: Dict) -> Tuple[Dict[str, Any], str]:
        """
        生成查询参数和时间戳。

        Args:
            device: 设备信息字典。

        Returns:
            Tuple: 查询参数和时间戳的元组。
        """
        crypt_key = Utils.random_string(16, "abcdef1234567890")
        nonce = Utils.random_string(16, "abcdef1234567890")
        ts = int(time.time() * 1000)
        key = base64.b64encode(rsa_encrypt(crypt_key.encode())).decode()
        aes = AES(crypt_key.encode())
        params = base64.b64encode(aes.encrypt(json.dumps(device).encode())).decode()
        extra = '{"appKey":"' + Qimei.APP_KEY + '"}'
        sign = Utils.calc_md5(
            key,
            params,
            str(ts),
            nonce,
            Qimei.SECRET,
            extra,
        )
        data = {
            "app": 0,
            "os": 1,
            "qimeiParams": {
                "key": key,
                "params": params,
                "time": str(ts),
                "nonce": nonce,
                "sign": sign,
                "extra": extra,
            },
        }
        return data, str(int(ts / 1000))

    @staticmethod
    def gen_random_payload() -> Dict:
        """
        生成随机的payload字典。

        Returns:
            dict: 随机的payload字典。
        """
        beacon_id = ""
        time_month = datetime.datetime.now().strftime("%Y-%m-") + "01"
        rand1 = random.randint(100000, 999999)
        rand2 = random.randint(100000000, 999999999)

        for i in range(1, 41):
            if i in [1, 2, 13, 14, 17, 18, 21, 22, 25, 26, 29, 30, 33, 34, 37, 38]:
                beacon_id += f"k{i}:{time_month}{rand1}.{rand2}"
            elif i == 3:
                beacon_id += "k3:0000000000000000"
            elif i == 4:
                beacon_id += f"k4:{''.join(random.choices('123456789abcdef', k=16))}"
            else:
                beacon_id += f"k{i}:{random.randint(0, 9999)}"
            beacon_id += ";"
        brand = random.choice(("VIVO", "Xiaomi", "OPPO", "HUAWEI"))

        fixed_rand_seconds = random.randint(0, 14400)
        current_time = datetime.datetime.now()
        time_result = current_time - datetime.timedelta(seconds=fixed_rand_seconds)
        formatted_time = time_result.strftime("%Y-%m-%d %H:%M:%S")
        reserved = {
            "harmony": "0",
            "clone": "0",
            "containe": "",
            "oz": "UhYmelwouA+V2nPWbOvLTgN2/m8jwGB+yUB5v9tysQg=",
            "oo": "Xecjt+9S1+f8Pz2VLSxgpw==",
            "kelong": "0",
            "uptimes": formatted_time,
            "multiUser": "0",
            "bod": brand,
            "brd": brand,
            "dv": "PCRT00",
            "firstLevel": "",
            "manufact": brand,
            "name": "PCRT00",
            "host": "se.infra",
            "kernel": "Linux localhost 4.14.253-android+ #754 SMP Wed Nov 9 17:04:03 CST 2022 armv8",
        }
        return {
            "androidId": "BRAND.141613.779",
            "platformId": 1,
            "appKey": Qimei.APP_KEY,
            "appVersion": "12.6.0.12",
            "beaconIdSrc": beacon_id,
            "brand": brand,
            "channelId": "10003505",
            "cid": "",
            "imei": Qimei.gen_random_imei(),
            "imsi": "",
            "mac": "",
            "model": "",
            "networkType": "unknown",
            "oaid": "",
            "osVersion": "Android 11.0,level 30",
            "qimei": "",
            "qimei36": "",
            "sdkVersion": "1.2.13.6",
            "targetSdkVersion": "29",
            "audit": "",
            "userId": "{}",
            "packageId": "com.tencent.qqmusic",
            "deviceType": "Phone",
            "sdkName": "",
            "reserved": json.dumps(reserved, separators=(",", ":"), ensure_ascii=False),
        }

    @staticmethod
    def gen_random_imei() -> str:
        """
        生成随机的IMEI号码。

        Returns:
            str: 随机的IMEI号码。
        """
        tac = random.randint(100000, 999999)
        snr = random.randint(100000, 999999)
        imei_without_checksum = f"{tac}{snr}"
        checksum = Qimei.calculate_luhn_checksum(imei_without_checksum)
        return f"{imei_without_checksum}{checksum}"

    @staticmethod
    def calculate_luhn_checksum(number_str: str) -> int:
        """
        计算Luhn校验和。

        Args:
            number_str: 待计算的数字字符串。
        Returns:
            int: Luhn校验和。
        """

        def digits_of(n: int) -> List[int]:
            return [int(digit) for digit in str(n)]

        digits = digits_of(int(number_str))
        odd_digits_sum = sum(digits[-1::-2])
        even_digits_sum = sum([sum(digits_of(2 * digit)) for digit in digits[-2::-2]])
        total_sum = odd_digits_sum + even_digits_sum
        return (10 - total_sum % 10) % 10

    @staticmethod
    def get() -> QImeiResult:
        """
        获取 QImei。

        Returns:
            QImeiResult: 获取结果。
        """
        data, ts = Qimei.gen_query(Qimei.gen_random_payload())
        sign = Utils.calc_md5("qimei_qq_androidpzAuCmaFAaFaHrdakPjLIEqKrGnSOOvH", ts)
        try:
            res = requests.post(
                "https://api.tencentmusic.com/tme/trpc/proxy",
                headers={
                    "Host": "api.tencentmusic.com",
                    "method": "GetQimei",
                    "service": "trpc.tme_datasvr.qimeiproxy.QimeiProxy",
                    "appid": "qimei_qq_android",
                    "sign": sign,
                    "user-agent": "QQMusic",
                    "timestamp": ts,
                },
                json=data,
            )
        except Exception:
            return QImeiResult("", "")
        qimei_data = str(res.json()["data"])
        qimei = json.loads(qimei_data)
        if qimei["code"] == 0:
            return QImeiResult(qimei["data"]["q16"], qimei["data"]["q36"])
        else:
            return QImeiResult("", "")
