#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

data = {'蘋果': [4, 3, 1, 0],
        '香蕉': [0, 4, 6, 2],
        '橘子': [1, 5, 2, 4]}

fruitsDF = pd.DataFrame(data)
print(fruitsDF)
