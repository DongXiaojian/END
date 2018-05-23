# _*_ coding:utf-8 _*_

import execjs
import os


class DesEad(object):
    def __init__(self):
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'JS')
        with open(path + '/des.js', 'r') as f:
            jsCon = f.read()
        self.ctx = execjs.compile(jsCon)

    def encode(self, strCon):
        """
        加密函数
        :param strCon: 需要加密的原始字符串
        :return: str
        """
        result = self.ctx.call('enString', strCon)
        return result


if __name__ == "__main__":
    des = DesEad()
    print(des.encode('qwer'))
