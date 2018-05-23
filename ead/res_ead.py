# _*_ coding:utf-8 _*_

import execjs
import os


class ResEad(object):
    def __init__(self):
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'JS')
        with open(path + '/res.js', 'r') as f:
            jsCon = f.read()
        self.ctx = execjs.compile(jsCon)

    def encode(self, strCon,  moduls, exponent='10001',):
        """
        加密函数
        :param strCon: 需要加密的原始字符串
        :param exponent: 加密指数， 默认为'10001'
        :param moduls: 加密公钥
        :return:
        """
        result = self.ctx.call('encode',strCon, exponent, moduls)
        return result




if __name__ == "__main__":
    res = ResEad()
    moduls = "932c4519403ebe3e0a10645ff42837b5679cad8a38f0937d05ba0b72b836ddaf6fb98ecd35d6be80c84c679d1a69a70016ec503686887b4b4afdf42d6ab47b9bc53ea272b711b6ed4f35b20c3aa4d1d046fe26ae55be0b6cbf7d242b3b65f6998b10ee7b33ee065e05602b92c4f6f34b0cc96fab9c52b9cb0f0ca7f89dea64db"
    # exponent = "10001"
    ll = res.encode('qwerqwer',  moduls)
    print (ll)

