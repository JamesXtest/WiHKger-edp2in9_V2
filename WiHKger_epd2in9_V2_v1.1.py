#!/usr/bin/python3
# -*- coding:utf-8 -*-
# WiHKger_e-paper epd2in9_V2 v1.1

import os, sys, json, requests
import time, datetime
from PIL import Image, ImageFont, ImageDraw
from data_folder import epd2in9_V2

# 地區設定
dist = "香港天文台"
# dist = "九龍城"
# dist = "深水埗"
# dist = "觀塘"
# dist = "元朗公園"

# 雨量資料位置
rainfall_dist = "油尖旺"
# rainfall_dist = "九龍城"
# rainfall_dist = "深水埗"
# rainfall_dist = "觀塘"
# rainfall_dist = "元朗"

# Delay period
delay = 1800        # 60 = Refresh every 1 minute.

# Folder directory
basedir = os.path.dirname(os.path.realpath(__file__))
icondir = os.path.join(basedir, 'icons')
fontdir = os.path.join(basedir, 'fonts')
tempdir = os.path.join(basedir, 'temp')

# Font setting
font_cn15 = ImageFont.truetype(os.path.join(fontdir, 'msjh.ttc'), 15)
font_cn18 = ImageFont.truetype(os.path.join(fontdir, 'msjh.ttc'), 18)
font_cn48 = ImageFont.truetype(os.path.join(fontdir, 'msjh.ttc'), 48)

# icon setting
L_icon_size = 80, 80
S_icon_size = 55, 55

def rhrread_process(): # 本港地區天氣報告
    rhrread_url = 'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=tc'
    rhrread_data = json.loads(requests.get(rhrread_url).text)

    for n_0 in range(len(rhrread_data["temperature"]["data"])):
        if rhrread_data["temperature"]["data"][n_0]["place"] ==dist:
            break
    if n_0 >= len(rhrread_data["temperature"]["data"])-1:
        n_0 = 1

    for n_1 in range(len(rhrread_data["rainfall"]["data"])):
        if rhrread_data["rainfall"]["data"][n_1]["place"] ==rainfall_dist:
            break
    if n_1 >= len(rhrread_data["rainfall"]["data"]):
        n_1 = 1

    print('- 本港地區天氣報告 -')
    print('地區 :', rhrread_data["temperature"]["data"][n_0]["place"])
    print('氣溫 :', rhrread_data["temperature"]["data"][n_0]["value"],'°C')
    print('濕度 :', rhrread_data["humidity"]["data"][0]["value"],'%')
    # print('濕度資料位置 :', rhrread_data["humidity"]["data"][0]["place"])
    print('圖示 :',  + rhrread_data["icon"][0])

    print('雨量資料位置 :', rhrread_data["rainfall"]["data"][n_1]["place"])
    print('最高雨量紀錄 :', rhrread_data["rainfall"]["data"][n_1]["max"],'mm')

    print('更新時間 :', rhrread_data["temperature"]["recordTime"],'\n')

    rhrread_logo = Image.open(os.path.join(icondir, str(rhrread_data["icon"][0])+".bmp"))         
    rhrread_logo = rhrread_logo.resize(L_icon_size)

    # current_W, current_H = 163, 118
    Himage.paste(rhrread_logo, (85 + xP, 35))
    draw.text((10 + xP, 10), str(rhrread_data["temperature"]["data"][n_0]["place"]), font=font_cn18, fill=0)
    draw.text((10 + xP, 23), str(rhrread_data["temperature"]["data"][n_0]["value"])+'°', font=font_cn48, fill=0)
    draw.text((10 + xP, 80), "濕度 : " + str(rhrread_data["humidity"]["data"][0]["value"])+'%', font=font_cn15, fill=0)
    draw.text((10 + xP, 95), "雨量 : " + str(rhrread_data["rainfall"]["data"][n_1]["max"])+'mm', font=font_cn15, fill=0)   

def fnd_process(): # 九天天氣預報   
    fnd_url = 'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=tc'
    fnd_data = json.loads(requests.get(fnd_url).text) 

    print('- 天氣預報 -')  
    for i in range (2):       
        print("預報日期 :", fnd_data["weatherForecast"][i]["forecastDate"])
        print("星期天數 :", fnd_data["weatherForecast"][i]["week"])
        print("預測溫度 :", fnd_data["weatherForecast"][i]["forecastMintemp"]["value"],"-", 
            fnd_data["weatherForecast"][i]["forecastMaxtemp"]["value"], "°C")
        print("預測濕度 :", fnd_data["weatherForecast"][i]["forecastMinrh"]["value"],"-", 
            fnd_data["weatherForecast"][i]["forecastMaxrh"]["value"], "%")
        print("預測圖示 :", fnd_data["weatherForecast"][i]["ForecastIcon"])
        print("預測風向 :", fnd_data["weatherForecast"][i]["forecastWind"])
        print("預測天氣 :", fnd_data["weatherForecast"][i]["forecastWeather"])
        print("降雨概率 :", fnd_data["weatherForecast"][i]["PSR"],'\n')
    print("天氣預測概況 :", fnd_data["generalSituation"])
    print("更新時間 :", fnd_data["updateTime"],'\n')

    current_W, current_H = 118, 118  
    fnd_logo = Image.open(os.path.join(icondir, str(fnd_data["weatherForecast"][0]["ForecastIcon"]) + ".bmp")) 
    fnd_logo = fnd_logo.resize(S_icon_size)
    S_logo_W, S_logo_H = S_icon_size
    Himage.paste(fnd_logo, (int((current_W-S_logo_W)/2+175+yP), 27))

    text_W, text_H = draw.textsize("明日預測", font=font_cn15)
    draw.text((int((current_W-text_W)/2+175+yP), 10), "明日預測", font=font_cn15, fill=0)

    draw.text((180 + yP, 80), "溫度 : " + 
        str(fnd_data["weatherForecast"][0]["forecastMintemp"]["value"])+"-"+
        str(fnd_data["weatherForecast"][0]["forecastMaxtemp"]["value"]) +"°", font=font_cn15, fill=0)
    draw.text((180 + yP, 95), "濕度 : " + 
        str(fnd_data["weatherForecast"][0]["forecastMinrh"]["value"])+"-"+ 
        str(fnd_data["weatherForecast"][0]["forecastMaxrh"]["value"]) +"%", font=font_cn15, fill=0) 

def draw_frame():
    draw.rectangle((0, 0, 296, 128), fill=zCol)
    draw.rounded_rectangle((5 + xP, 5, 168 + xP, 123), fill=1, outline=0, width=2, radius=15)
    draw.rounded_rectangle((173 + yP, 5, 291 + yP, 123), fill=1, outline=0, width=2, radius=15)

def time_Chop():
    strTimeChop = time.strftime('%Y/%m/%d %H:%M:%S')    
    print('Last update : '+ strTimeChop,'\n')

def print_Logo():
    Lg = 50
    print()
    print('*'*Lg)
    print(" WiHKger - Weather Info for HongKongers ".center(Lg, '*'))
    print(" e-Paper epd2in9_V2 Version ".center(Lg, '*'))
    print(" Verison : 1.1 ".center(Lg, '*'))
    print('*'*Lg,'\n')

def epaper_Start():
    epd.init()
    epd.Clear(0xFF)

def epaper_Display():  
    epd.display(epd.getbuffer(Himage))
    epd.sleep()

def epaper_Exit():
    epd = epd2in9_V2.EPD()
    epd.init()
    epd.Clear(0xFF)
    epd2in9_V2.epdconfig.module_exit()

try:
    epd = epd2in9_V2.EPD()
    max_Width, max_Height = 296, 128            
    Himage = Image.new('1', (max_Width, max_Height), 255)
    draw = ImageDraw.Draw(Himage)

    displayMode = 0
    strX = [0, 123]
    strY = [0, -168]
    strZ = [1, 0]

    print_Logo()

    while True:

        xP, yP, zCol = strX[displayMode], strY[displayMode], strZ[displayMode]     
        # epaper_Start()
        draw_frame()
        rhrread_process()
        fnd_process()
        # epaper_Display()
        time_Chop()
        Himage.save(os.path.join(tempdir, 'Temp_WiHKger_epd2in9.bmp'))
               
        # print ('displayMode : ', displayMode)
        displayMode = displayMode + 1
        if displayMode >= 2:
            displayMode = 0

        time.sleep(delay)

except KeyboardInterrupt:   
    print("leaning...")
    # epaper_Exit()      
    print("Exit",'\n')
    exit()
