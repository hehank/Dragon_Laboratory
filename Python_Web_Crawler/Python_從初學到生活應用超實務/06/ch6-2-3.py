#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json

jsonfile = "./Python_Web_Crawler/Python_從初學到生活應用超實務/06/Example.json"
# jsonfile = "./Example.json"

json_str = '{"name": "Hank","score": 80,"tel": "0987-987-987"}'
data = json.loads(json_str)

with open(jsonfile, 'w', encoding='utf-8', newline='') as fp:
    json.dump(data, fp)
