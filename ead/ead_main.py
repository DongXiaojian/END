# _*_ coding:utf-8 _*_

import hashlib
import hmac
from aes_ead import AesEad
from des_ead import DesEad
from res_ead import ResEad
from sm2_ead import Sm2Ead


class Ead(object):
    def m5(self, strCon):
        """
        md5加密
        :param strCon:原始字符串
        :return: str
        """
        m = hashlib.md5()
        m.update(strCon)
        return m.hexdigest()

    def hmac(self, key, msg=None, digestmod=None):
        if msg:
            HASH = hmac.new(key.encode(), msg.encode(), digestmod).hexdigest()
        else:
            HASH = hmac.new(key.encode(), msg, digestmod).hexdigest()
        return HASH

    def aesEncode(self, word, pwd):
        aes = AesEad()
        return aes.encode(word, pwd)

    def desEncode(self, strCon):
        des = DesEad()
        return des.encode(strCon)

    def resEncode(self, strCon, moduls, exponent='10001'):
        res = ResEad()
        return res.encode(strCon, moduls, exponent)

    def sm2Encode(self, strCon):
        sm2 = Sm2Ead()
        return sm2.encode(strCon)


if __name__ == "__main__":
    ead = Ead()
    print(ead.hmac('qwerqwer', None, hashlib.sha256))
    print(ead.aesEncode('qwer', 'qwerqwerwe'))
