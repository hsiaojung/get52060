
from selenium import webdriver
import numpy as np
from time import sleep
from bs4 import BeautifulSoup
import errno
import os
import subprocess
from platform import system
from subprocess import PIPE
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common import utils
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import process
from datetime import date
from datetime import datetime
import sys


# init to login
def iftodaybuy(timex,driver): 
   
       
    url ='https://www.wantgoo.com/stock/institutional-investors/investment-trust/net-buy-sell-rank'
    driver.get(url) 
    sleep(timex-2)  
    content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[4]/time[1]")
    pageLastUpdateTime = content.text # 把排版後的 html 印出來
    pageLastUpdateTimeList = pageLastUpdateTime.split('/')

    dd = int(day)
    webdd = int(pageLastUpdateTimeList[2])
    print("dd =", dd)
    print("webdd =", webdd)

    if (dd != webdd):
        print("Wantgoo has not updated web for this info")
        return 0
    else :
        print("Wantgoo has updated web for this info")   
        return 1





# init to login
def ifalreadyGet(): 
   
    mainpath = "/home/pi/info/s1/"
    today = date.today()
    month = today.strftime("%b")
    day= today.strftime("%d")
    year = today.strftime("%Y")
    print(mainpath+year+"/"+month+"/"+day)

    dir = os.listdir(mainpath+year+"/"+month+"/"+day)

    # Checking if the list is empty or not 
    if len(dir) == 0: 
        print("Empty directory") 
    else: 
        print("Not empty directory") 


# init to login
def ifCreate(): 

    #Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec 
    today = date.today()
    month = today.strftime("%b")
    day= today.strftime("%d")
    year = today.strftime("%Y")
    print("year =", year)
    print("month =", month)
    print("day =", day)
    print("/home/pi/info/s1/2021/"+month)

    if os.path.isdir("/home/pi/info/s1/"+year):
        print("年檔案存在。")
    else:
        os.makedirs("/home/pi/info/s1/"+year)

    if os.path.isdir("/home/pi/info/s1/"+year+"/"+month):
        print("月檔案存在。")
    else:
        os.makedirs("/home/pi/info/s1/"+year+"/"+month)

    if os.path.isdir("/home/pi/info/s1/"+year+"/"+month+"/"+day):
        print("日檔案存在。")
    else:
        os.makedirs("/home/pi/info/s1/"+year+"/"+month+"/"+day)
