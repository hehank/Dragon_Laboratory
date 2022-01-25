#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

csvfile = "./out.csv"

with open(csvfile, mode="w", encoding="utf-8", newline='') as fp:

    writer = csv.writer(fp, delimiter=' ')

    lst = []
    for i in range(1, 10, 3):
        lst.append([i, i+1, i+2])

    writer.writerows(lst)
