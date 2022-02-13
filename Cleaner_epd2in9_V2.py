#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Cleaner epd2in9_V2 V_1.0

from data_folder import epd2in9_V2

def epaper_Exit():
    epd = epd2in9_V2.EPD()
    epd.init()
    epd.Clear(0xFF)
    epd2in9_V2.epdconfig.module_exit()

print('Cleaning...')
epaper_Exit()
print('Exit!','\n')
exit()