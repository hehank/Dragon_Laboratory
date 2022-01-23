#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

# csvfile = "./Python_Web_Crawler/Python_從初學到生活應用超實務/05/Example.csv"
csvfile = "./Example.csv"

with open(csvfile, 'r') as fp:
    reader = csv.reader(fp)
    for row in reader:
        print(','.join(row))
