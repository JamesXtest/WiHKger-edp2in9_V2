# WiHKger 2.9" e-Paper version  
### Weather info for HongKonger  香港人專用嘅天氣資訊站

![Imgur](https://i.imgur.com/f2gQdKo.png)

+ 資訊來源係香港天文台官方嘅api, 預設地區為香港天文台。  
可以喺程式內改為你住嗰區（如九龍城、深水埗、觀塘…等）。   
(新增) 可使用的地區名稱請以 dist_finder.py 查閱。 
詳情請參考以下資料,  
https://www.hko.gov.hk/tc/weatherAPI/doc/files/HKO_Open_Data_API_Documentation_tc.pdf

+ 硬件最基本只需 Raspberry pi + Wareshare 2.9" e-Paper Module(epd2in9_V2)。  
已經喺 pi zero 及 4B 上測試可以正常運作。

+ Font 預設用 Wareshare 跟嘅 Font.ttc, 不過對繁體嘅支援唔係咁好，建議改用其他字體。    
字體用 TTF, TTC 都可以。放入 fonts folder 後，喺程式內將 Font.ttc 改名就用得。

+ 天氣 icon 請自行 download。  
可以用 test_icon.py 測試 icon，加入icons folder 後喺程式度改 icon 名即可。  
效果如下，  
![Imgur](https://i.imgur.com/HWlhPfk.png)

  注意要有齊全部29個 icons 先好 run 個 program，因為天文台有29種通知，唔齊嘅話會hang機。 
  
  Icon 請改名為xx.bmp（例如:50.bmp, 51.bmp, …), 放入icons folder。  
  關於 icon 改名請參考以下網址：  
  https://www.weather.gov.hk/textonly/v2/explain/wxicon_c.htm

+ 預設只會喺 temp folder 顯示圖片。  
刪除 `epaper_Start()` 及 `epaper_Exit()` 前面嘅 `#` 即可於 e-Paper 顯示。  
可以用 <kbd>Ctrl</kbd>+<kbd>C</kbd> 退出。

+ 因為 e-Paper 嘅特性係會顯示最後嘅畫面，就算斷咗電都唔會消失。   
要清除畫面可以用 Cleaner_epd2in9_V2.py。

+ e-Paper 另一特性係容易消印，長期顯示同一畫面會令到啲像素不能回復。  
所以設置咗 display mode, 每 30min 自動 update data，同時更新 e-Paper, 改變底色及轉換位置。  
更改 `delay = ` 後面嘅 value 可以改變更新時間。

+ 建議做返個機殼, 果塊 e-Paper 十分脆弱, 不適宜裸機使用。
+ YouTube : 
https://youtu.be/byxogmUsSgY

---
#### Hardware requirements 

+ Raspberry pi with python 3.7 or above. (tested on pi zero & 4B)
+ Waveshare 2.9" e-Paper Module(epd2in9_V2)  

#### Installation 
1. Basic installation of Raspberry pi.
2. Enable SPI interface in Raspberry pi.
3. Connect hardware and install libraries as per below website,  
https://www.waveshare.com/wiki/2.9inch_e-Paper_Module

    + Install BCM2835 libraries  
    + Install WiringPi libraries  
    + Install Python3 libraries

> Notice:   
> Pillow may need to upgrade to 8.2 or above. 
> ```python3
> python3 -m pip install pillow --upgrade
> ```
     
4. Driver for e-Paper 2.9" e-Paper Module(epd2in9_V2) was included in data_folder,  
 replace the driver if you got a different model of e-Paper.

5. Download icon, rename and place into icons folder.   
    + Test icon by test_icon.py. 
    + Check the picture in temp folder.   
    + You can cleanup the epaper by running Cleaner_epd2in9_V2.py.

> Notice:
> The icon must be named in xx.bmp (eg. 50.bmp).  
> Name the icon follow the information from below website,  
> https://www.hko.gov.hk/textonly/v2/explain/wxicon_e.htm

6. Replace the font inside fonts folder if necessary.  

7. Edit WiHKger_epd2in9_V2.py as below,  
    + Choose your district by changing the position of `#` before `dist = ` & `rainfall_dist = `  
    + (New) Use dist_finder.py to find out all available district area name.
    + Take out the `#` before `epaper_Start()` & `epaper_Exit()` to let the e-Paper work.   
You can use  <kbd>Ctrl</kbd>+<kbd>C</kbd> to exit the program.

8. Finally, suggest to make a case or a frame to protect the e-Paper module.   
It seems really crackly.

