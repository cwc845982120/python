# -*- coding: UTF-8 -*-
import requests

URL = 'https://www.baidu.com'

res = requests.get(URL)

print res.text

