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

#################################################################
# 測試用 #########################################################
#################################################################

print (red + 'dist = 分區氣溫' + end, ',' , blue + 'rainfall = 分區雨量' + end, ',' , green + 'ltmv_station = 最新十分鐘平均能見度資料位置')
print('*'*83)

# 地區設定 測試用
# dist = "香港天文台"
dist = "九龍城"
# dist = "深水埗"
# dist = "觀塘"
# dist = "元朗公園"

# 雨量資料位置 測試用
rainfall_dist = "油尖旺"
# rainfall_dist = "九龍城"
# rainfall_dist = "深水埗"
# rainfall_dist = "觀塘"
# rainfall_dist = "元朗"

def dist_list():
    rhrread_url = 'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=tc'
    rhrread_data = json.loads(requests.get(rhrread_url).text)

    dlist = []
    for i in range(len(rhrread_data["temperature"]["data"])):
        dlist.append(rhrread_data["temperature"]["data"][i]["place"])        
    return dlist  

print ('分區', red + '氣溫' + end, '資料位置 :')
if dist in dist_list() != True:
    n_0 = dist_list().index(dist)
    print([n_0], dist)
else:
    print('*','分區', red + '氣溫' + end, [dist], '地區設定不正確 !')
    print('請重新輸入, 只可輸入以下地區 :')
    print(dist_list())

def rainfall_dist_list():
    rhrread_url = 'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=tc'
    rhrread_data = json.loads(requests.get(rhrread_url).text)
        
    rlist = []
    for i in range(len(rhrread_data["rainfall"]["data"])):
        rlist.append(rhrread_data["rainfall"]["data"][i]["place"])        
    return rlist

print ('分區', blue + '雨量' + end, '資料位置 :')
if rainfall_dist in rainfall_dist_list() != True:
    n_1 = rainfall_dist_list().index(rainfall_dist)
    print([n_1], rainfall_dist)
else:
    print('*','分區', blue + '雨量' + end, [rainfall_dist], '地區設定不正確 !')
    print('請重新輸入, 只可輸入以下地區 :')
    print(rainfall_dist_list())

# 最新十分鐘平均能見度資料位置 測試用
def ltmv_dist_list():
    ltmv_url = 'https://data.weather.gov.hk/weatherAPI/opendata/opendata.php?dataType=LTMV&lang=tc&rformat=json'
    ltmv_data = json.loads(requests.get(ltmv_url).text)
    llist = []
    for i in range(len(ltmv_data["data"])):
        llist.append(ltmv_data["data"][i][1])        
    return llist

# ltmv_station = '中環'
ltmv_station = '赤鱲角'
# ltmv_station = '西灣河'
# ltmv_station = '橫瀾島'
print (green + '最新十分鐘平均能見度' + end, '資料位置 :')
if ltmv_station in ltmv_dist_list() != True:
    n_2 = ltmv_dist_list().index(ltmv_station)
    print([n_2], ltmv_station)
else:
    print('*',green + '最新十分鐘平均能見度' + end, [ltmv_station], '地區設定不正確 !')
    print('請重新輸入, 只可輸入以下地區 :')
    print(ltmv_dist_list())
