#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json

jsonfile = "./Python_Web_Crawler/Python_從初學到生活應用超實務/06/Example.json"
# jsonfile = "./Example.json"

with open(jsonfile, mode='r', newline='') as fp:
    data = json.load(fp)

print("Name：", data["name"])
print("Score", data["score"])
