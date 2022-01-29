#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# ? 空氣品質指標(AQI).json => 來源 => https://data.epa.gov.tw/dataset/aqx_p_432/resource/8ff027dc-2da2-42e8-85de-78ac3faf470e

jsonfile = "./Python_Web_Crawler/Python_從初學到生活應用超實務/06/空氣品質指標(AQI).json"
# jsonfile = "./空氣品質指標(AQI).json"

output_file = "./Python_Web_Crawler/Python_從初學到生活應用超實務/06/6-3-2_out.txt"
# output_file = "./6-3-2_out.txt"

with open(jsonfile, mode="r", encoding="utf-8") as fp:
    all_data = json.load(fp)

records_data = all_data['result']['records']
# print(all_data['result']['records'])

total = len(records_data)
# print(total)

with open(output_file, mode='w', encoding='utf-8') as fp:
    for info in records_data:
        print(f"測站名稱： {info['SiteName']}", file=fp)
        print(f"發佈時間： {info['PublishTime']}", file=fp)
        print(f"空汙狀態： {info['Status']}", file=fp)
        print(f"AQI 指標： {info['AQI']}", file=fp)
        print(f"PM 2.5： {info['PM2.5']}", file=fp)
        print("----------------------------------------------", file=fp)

    print(f"總計： {total} 筆資料", file=fp)
