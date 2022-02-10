#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import requests
import os

URL = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
md5file = "./Python_Web_Crawler/Python_從初學到生活應用超實務/07/html_md5.txt"
# md5file = "./html_md5.txt"

# TODO: Calculate new md5 code
html_content = requests.get(URL).text.encode('utf-8')
m = hashlib.md5(html_content)
new_md5 = m.hexdigest()

# TODO: Determine md5file is exist or not
old_md5 = ""
if os.path.exists(md5file):
    with open(md5file, 'r') as fp:
        old_md5 = fp.read()

    if old_md5 != new_md5:
        print("Taipei TouBike Data has been updated")
        with open(md5file, 'w') as fp:
            fp.write(new_md5)

    else:
        print("Taipei TouBike Data not updated")

else:
    with open(md5file, 'w') as fp:
        fp.write(new_md5)
    print("Taipei TouBike Data has been updated")
