#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib

data = b"My name is HankHe"
# data = "My name is HankHe".encode("utf-8")

# TODO: Calculate hash code
# ? Method 1：
m = hashlib.md5(data)

# ? Method 2：
# m = hashlib.md5()
# m.update(data)

# TODO: Get hash code
md5_hexstr = m.hexdigest()
print(md5_hexstr)
