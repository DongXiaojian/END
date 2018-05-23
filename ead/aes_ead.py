# _*_ coding:utf-8 _*_

import execjs
import os


class AesEad(object):
    def __init__(self):
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'JS')
        with open(path + '/aes.js', 'r') as f:
            jsCon = f.read()
        self.ctx = execjs.compile(jsCon)

    def encode(self, word, pwd):
        """
        加密函数
        :param pwd: 加密的密码
        :param word: 加密的字符串
        :return:
        """
        result = self.ctx.call('Encrypt', word, pwd)
        return result


if __name__ == "__main__":
    des = AesEad()
    print(des.encode('qwer', '1234'))
