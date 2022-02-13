#!/usr/bin/python3
# -*- coding:utf-8 -*-
# WiHKger_e-paper epd2in9_V2

import os
import sys
import time
import datetime
from PIL import Image, ImageFont, ImageDraw
from data_folder import epd2in9_V2

# icon setting
test_icon = 'RPi.bmp'

L_icon_size = 80, 80
S_icon_size = 55, 55

# rotate_Display = 0 # Normal position
# rotate_Display = 1 # Mirror position
rotate_Display = 2  # Ratate 180°
# rotate_Display = 4  # Normal position

# Folder directory
basedir = os.path.dirname(os.path.realpath(__file__))
icondir = os.path.join(basedir, 'icons')
fontdir = os.path.join(basedir, 'fonts')
tempdir = os.path.join(basedir, 'temp')

# Font setting
font_cn15 = ImageFont.truetype(os.path.join(fontdir, 'Font.ttc'), 15)
font_cn18 = ImageFont.truetype(os.path.join(fontdir, 'Font.ttc'), 18)
font_cn48 = ImageFont.truetype(os.path.join(fontdir, 'Font.ttc'), 48)

def draw_frame():
    draw.rectangle((0, 0, 296, 128), fill=zCol)
    draw.rounded_rectangle((5 + xP, 5, 168 + xP, 123), fill=1, outline=0, width=2, radius=15)
    draw.rounded_rectangle((173 + yP, 5, 291 + yP, 123), fill=1, outline=0, width=2, radius=15)

def epaper_Start():
    epd = epd2in9_V2.EPD()
    epd.init()
    epd.Clear(0xFF)
    epd.display(epd.getbuffer(Himage))
    epd.sleep()

def epaper_Exit():
    epd = epd2in9_V2.EPD()
    epd.init()
    epd.Clear(0xFF)
    epd2in9_V2.epdconfig.module_exit()

try:
    displayMode = 1
    strX = [0, 123]
    strY = [0, -168]
    strZ = [1, 0]

    max_Width, max_Height = 296, 128            
    Himage = Image.new('1', (max_Width, max_Height), 255)
    draw = ImageDraw.Draw(Himage) 

    xP, yP, zCol = strX[displayMode], strY[displayMode], strZ[displayMode]

    draw_frame()
    rhrread_logo = Image.open(os.path.join(icondir, test_icon))         
    rhrread_logo = rhrread_logo.resize(L_icon_size)
    Himage.paste(rhrread_logo, (85 + xP, 35))

    draw.text((15 + xP, 10), 'Test icon', font=font_cn18, fill=0)
    draw.text((15 + xP, 40), test_icon, font=font_cn18, fill=0)

    current_W, current_H = 118, 118 
    fnd_logo = Image.open(os.path.join(icondir, test_icon))         
    fnd_logo = fnd_logo.resize(S_icon_size) 
    S_logo_W, S_logo_H = S_icon_size
    Himage.paste(fnd_logo, (int((current_W-S_logo_W)/2+175+yP), 27))

    Himage.save(os.path.join(tempdir, 'Temp_test_icon.bmp'))

    strTimeChop = time.strftime('%Y/%m/%d %H:%M')
    print('Last Update : ' + strTimeChop,'\n')

    # epaper_Start()

except KeyboardInterrupt:   
    print("leaning...")
    # epaper_Exit()      
    print("Exit",'\n')
    exit()
