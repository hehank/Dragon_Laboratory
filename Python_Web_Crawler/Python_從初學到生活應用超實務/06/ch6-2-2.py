# ! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json

data = {
    "name": "Hank",
    "score": 80,
    "tel": "0987-987-987"
}

json_str = json.dumps(data, sort_keys=True, indent=4)
print("JSON Object：", json_str)
print("JSON Object Type：", type(json_str))
