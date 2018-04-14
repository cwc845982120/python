# -*- coding: UTF-8 -*-
import requests

URL = 'https://www.baidu.com'

res = requests.get(URL)
res.encoding = 'UTF-8'
print(res.text)

