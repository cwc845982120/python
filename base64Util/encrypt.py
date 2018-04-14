# -*- coding: UTF-8 -*-
# auth: caowencheng<845982120@qq.com>
# date: 2018/4/13

import base64

nameCode = base64.b64encode('曹文成')
nameStr = base64.b64decode(nameCode)

if __name__ == "__main__":
    print('base64编码后：' + nameStr)
    print('base64解码后：' + nameCode)
