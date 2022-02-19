#!/usr/bin/python3
# -*- coding:utf-8 -*-
# WiHKger_e-paper epd2in9_V2

import json
import requests

red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
bold = '\033[1m'
italics = '\033[3m'
underline = '\033[4m'
end = '\033[0m'

def dist_find():
    rhrread_url = 'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=tc'
    rhrread_data = json.loads(requests.get(rhrread_url).text)
    print ('分區', red + '氣溫' + end, '資料位置 :')
    for n_0 in range(len(rhrread_data["temperature"]["data"])):
        print ([n_0], rhrread_data["temperature"]["data"][n_0]["place"])

def rainfall_dist_find():
    rhrread_url = 'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=tc'
    rhrread_data = json.loads(requests.get(rhrread_url).text)
    print ('分區', blue + '雨量' + end, '資料位置 :')
    for n_1 in range(len(rhrread_data["rainfall"]["data"])):
        print ([n_1], rhrread_data["rainfall"]["data"][n_1]["place"])
    
dist_find()
print()
rainfall_dist_find()
print()

print (red + 'dist = 分區氣溫' + end, ',' , blue + 'rainfall = 分區雨量' + end)
