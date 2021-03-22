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
import check


timex = 4
process.showme()
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument("--disable-gpu")
options.add_argument("--disable-translate");
options.add_argument("--disable-infobars")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--dns-prefetch-disable")
options.add_argument("enable-automation")


fstock_name = [] 
fstock_num = [] 
tstock_name = [] 
tstock_num = []  

mystock_name = [] 
mystock_num = ['0050', 
 '0056', 
 '1101', 
 '1102', 
 '1216', 
 '1301', 
 '1326', 
 '1527', 
 '1714', 
 '1717', 
 '2301', 
 '2308', 
 '2314', 
 '2317', 
 '2330', 
 '2344', 
 '2347', 
 '2368', 
 '2376', 
 '2377', 
 '2382', 
 '2408', 
 '2409', 
 '2449', 
 '2454', 
 '2633', 
 '2801', 
 '2812', 
 '2823', 
 '2834', 
 '2838', 
 '2880', 
 '2881', 
 '2882', 
 '2883', 
 '2884',       
 '2886', 
 '2887', 
 '2890', 
 '2891', 
 '2892', 
 '3231', 
 '3481', 
 '4938', 
 '5347', 
 '5876', 
 '5880', 
 '6412', 
 '9904', 
 '9914', 
 '9921',
 '9931'
]
url ='https://www.wantgoo.com/login/auth/apilogin?returnUrl=/stock/institutional-investor/foreign/double-long'


allVlue = 11
fstock_name = [] 
fstock_num = [] 

tstock_name = [] 
tstock_num = []  
    
fstock_name.clear()
fstock_num.clear()
    
tstock_name.clear()
tstock_num.clear()                           

times = "0000000"

def toGetTimeFile(times):

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    mainpath = "/home/pi/info/s1/"
    today = date.today()
    month = today.strftime("%b")
    day= today.strftime("%d")
    year = today.strftime("%Y")
    print(mainpath+year+"/"+month+"/"+day)
    fileName = open(mainpath+year+"/"+month+"/"+day+"/"+current_time+'-'+day+'-getprice.txt','w+')
    #fileName.write("Try to use file.write()\nHail HYDRA")
    return fileName


# init to login
def login(timex): 

    for i in range(1,1):               
                                    
        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/input[1]").send_keys(Keys.ESCAPE)
        #content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/input[1]").send_keys(Keys.ESCAPE)
        sleep(1)
        
        
    fstock_name.clear()
    fstock_num.clear()
        
    tstock_name.clear()
    tstock_num.clear()                    
    #content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/input[1]")
    content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/input[1]")

    content.send_keys("hsiao.jung@msn.com")
                            
    content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/input[1]")
    #content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[1]/div[3]/input[1]")
    content.send_keys("01447745")
                        
    content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[5]/button[1]")
    #content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[1]/div[5]/button[1]")

    content.click()
    print ("done to loging!")
    
# to get 外資 list3

def toGetFstock(fstock_name,fstock_num,timex,filename):

             
    fstock_name.clear()
    fstock_num.clear()
   

    url ='https://www.wantgoo.com/stock/institutional-investors/foreign/net-buy-sell-rank'
    driver.get(url) 
    sleep(5 * timex)  
    content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[4]/time[1]")
    print(content.text) # 把排版後的 html 印出來
    for i in range(1,51):
        converted_num = str(i) 
        #print(converted_num) 
        #ans="/html[1]/body[1]/div[2]/main[1]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[2]/a[1]" 
        #ans="/html[1]/body[1]/div[2]/main[1]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[2]/td[2]/a[1]"
        #ans="/html[1]/body[1]/div[2]/main[1]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[3]/td[2]/a[1]"
        ans = "/html[1]/body[1]/div[2]/main[1]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr["+converted_num+"]/td[2]/a[1]"
        #print (ans)
        content = driver.find_element_by_xpath(ans)
        #print(content.text) # 把排版後的 html 印出來
        links = content.get_attribute('href')
        #print (links)
        tmp = links.rfind('/')
        fstock_num.append (links[tmp+1:])
        #print(links) # 把排版後的 html 印出來
        fstock_name.append (content.text) 
    
    print("外資")
    print(fstock_num)
    print(fstock_name)
    print(len(fstock_name))
    print(len(fstock_num))

def toGetTstock(tstock_name,tstock_num,timex,filename):


            
    tstock_name.clear()
    tstock_num.clear()      
            
    url ='https://www.wantgoo.com/stock/institutional-investors/investment-trust/net-buy-sell-rank'
    driver.get(url) 
    sleep(5 * timex)  
    content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[4]/time[1]")
    print(content.text) # 把排版後的 html 印出來
    for i in range(1,51):
        converted_num = str(i) 
        #print(converted_num) 
        #ans="/html[1]/body[1]/div[2]/main[1]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[2]/a[1]" 
        #ans="/html[1]/body[1]/div[2]/main[1]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[2]/td[2]/a[1]"
        #ans="/html[1]/body[1]/div[2]/main[1]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[3]/td[2]/a[1]"
        ans = "/html[1]/body[1]/div[2]/main[1]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr["+converted_num+"]/td[2]/a[1]"
        #print (ans)
        content = driver.find_element_by_xpath(ans)
        links = content.get_attribute('href')
        #print (links)
        tmp = links.rfind('/')
        tstock_num.append (links[tmp+1:])
        #print(links) # 把排版後的 html 印出來
        tstock_name.append (content.text) 
        #print(content.text ) # 把排版後的 html 印出來   
        
    print("投信")
    print(tstock_name)
    print(tstock_num)
    print(len(tstock_name))
     
def toGetFstockParmeter(fstock_name,fstock_num,timex, allVlue,filename):



    foreignInvestment = np.zeros((len(fstock_num), allVlue), dtype=float)

    url ='https://www.wantgoo.com/stock/institutional-investors/foreign/net-buy-sell-rank'
    print('toGetFstockParmeter 投信  ========================================', file=filename)
    for i in range(0,len(fstock_num)):
    
        url ="https://www.wantgoo.com/stock/"+fstock_num[i]+"/technical-chart"
        #print(url)
        
        driver.get(url) 
        driver.maximize_window()  
        sleep(3*timex)                          
        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[1]/ul[1]/li[1]/button[1]")
        driver.execute_script("arguments[0].click();", content)#using this by avoid to can not apoach the buttom
        #content.click()    
        sleep(1) 
        

        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[2]/ul[1]/li[2]/span[1]/span[1]")
        if (content.text != '--') :
            contentNow = float(content.text)
        #print(contentNow) # 把排版後的 html 印出來
                                                
        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/span[1]/ul[1]/li[2]/label[1]/span[1]")
        content5 = 0;
        if (content.text != '--') :
            content5 = float(content.text)
        #print(content5) # 把排版後的 html 印出來

        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/span[1]/ul[1]/li[4]/label[1]/span[1]")
        content20 = 0;
        if (content.text != '--') :
            content20 = float(content.text)
        #print(content20) # 把排版後的 html 印出來


        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/span[1]/ul[1]/li[5]/label[1]/span[1]")
        content60 = 0;
        if (content.text != '--') :
            content60 = float(content.text)
        #print(content60) # 把排版後的 html 印出來


        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[3]/span[1]/ul[1]/li[2]/span[1]")
        kdk = 0
        if (content.text != '--') :
            kdk =float(content.text)
        #print(kdk) # 把排版後的 html 印出來



        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[3]/span[1]/ul[1]/li[3]/span[1]")
        kdd =0
        if (content.text != '--') :
            kdd = float(content.text)
        #print(kdd) # 把排版後的 html 印出來
        
        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[1]/ul[1]/li[2]/button[1]")
        #content.click()
        driver.execute_script("arguments[0].click();", content)
        
        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[3]/span[1]/ul[1]/li[2]/span[1]")
        wkdk = 0
        if (content.text != '--') :
            wkdk = float(content.text)
        
        if (content5 != 0 and content20 != 0 and content60 != 0 ):
            content560 = ((content5 - content60)/content60)*100
            content2060 = ((content20 - content60)/content60)*100
            content520 =    ((content5 - content20)/content20)*100
            contentNow_5 = ((contentNow - content5)/content5)*100
            content560 = round(content560, 2)
            content520 = round(content520, 2)
            contentNow_5 = round(contentNow_5, 2)
            content2060 = round(content2060, 2)
        else :
            content560 = 999
            content2060 = 999
            content520 = 999
            contentNow_5 = 999
            content560 = 999
            content520 = 999
            contentNow_5 = 999
            content2060 = 999
        # Totol vaule all be put to val for Numpy arrary
        
        
        vals = [contentNow_5,content520,content560,content2060,kdk,kdd,wkdk,contentNow,content5,content20,content60]
        print(i,'=', fstock_name[i], vals)
        foreignInvestment[i,] = vals
        print(i,'=', fstock_name[i], vals, file=filename)
        

    return foreignInvestment

def toGetTstockParmeter(tstock_name,tstock_num,timex, allVlue,filename):

    # 创建一个 50 x 8 的数组且所有值全为 0

    TrustInvestment   = np.zeros((len(tstock_num), allVlue), dtype=float)
    print('toGetTstockParmeter 外資 ========================================', file=filename)
    for i in range(0,len(tstock_num)):
        #url ='https://www.wantgoo.com/stock/2330/technical-chart'
        url ="https://www.wantgoo.com/stock/"+tstock_num[i]+"/technical-chart"
        #print(url)
        
        driver.get(url) 
        driver.maximize_window()  
        sleep(3*timex)                             
        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[1]/ul[1]/li[1]/button[1]")
        driver.execute_script("arguments[0].click();", content)#using this by avoid to can not apoach the buttom
        #content.click()    
        sleep(1) 
        

        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[2]/ul[1]/li[2]/span[1]/span[1]")
        if (content.text != '--') :
            contentNow = float(content.text)
        #print(contentNow) # 把排版後的 html 印出來
                                                
        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/span[1]/ul[1]/li[2]/label[1]/span[1]")
        content5 = 0;
        if (content.text != '--') :
            content5 = float(content.text)
        #print(content5) # 把排版後的 html 印出來

        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/span[1]/ul[1]/li[4]/label[1]/span[1]")
        content20 = 0;
        if (content.text != '--') :
            content20 = float(content.text)
        #print(content20) # 把排版後的 html 印出來


        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/span[1]/ul[1]/li[5]/label[1]/span[1]")
        content60 = 0;
        if (content.text != '--') :
            content60 = float(content.text)
        #print(content60) # 把排版後的 html 印出來


        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[3]/span[1]/ul[1]/li[2]/span[1]")
        kdk = 0
        if (content.text != '--') :
            kdk =float(content.text)
        #print(kdk) # 把排版後的 html 印出來

        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[3]/span[1]/ul[1]/li[3]/span[1]")
        kdd =0
        if (content.text != '--') :
            kdd = float(content.text)
        #print(kdd) # 把排版後的 html 印出來
        
        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[1]/ul[1]/li[2]/button[1]")
        #content.click()
        driver.execute_script("arguments[0].click();", content)
        
        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[3]/span[1]/ul[1]/li[2]/span[1]")
        wkdk = 0
        if (content.text != '--') :
            wkdk = float(content.text)
        
        if (content5 != 0 and content20 != 0 and content60 != 0 ):
            content560 = ((content5 - content60)/content60)*100
            content2060 = ((content20 - content60)/content60)*100
            content520 =    ((content5 - content20)/content20)*100
            contentNow_5 = ((contentNow - content5)/content5)*100
            content560 = round(content560, 2)
            content520 = round(content520, 2)
            contentNow_5 = round(contentNow_5, 2)
            content2060 = round(content2060, 2)
        else :
            content560 = 999
            content2060 = 999
            content520 = 999
            contentNow_5 = 999
            content560 = 999
            content520 = 999
            contentNow_5 = 999
            content2060 = 999
        # Totol vaule all be put to val for Numpy arrary
        
        
        vals = [contentNow_5,content520,content560,content2060,kdk,kdd,wkdk,contentNow,content5,content20,content60]
        print(i,'=', tstock_name[i], vals)
        TrustInvestment[i,] = vals
        print(i,'=', tstock_name[i], vals, file=filename)

    print('Debug req1')
    print(TrustInvestment)
    return TrustInvestment

def toGetMystockParmeter(timex,filename):


    mystock = np.zeros((len(mystock_num), allVlue), dtype=float)
    mystock_name.clear
    '''
    print(mystock_name)
    print(type(mystock_name))
    print(len(mystock_num))
    '''
    print('toGetMystockParmeter 自選 ========================================', file=filename)
    for i in range(0,(len(mystock_num))):
    
        url ="https://www.wantgoo.com/stock/"+mystock_num[i]+"/technical-chart"
        #print(url)
        
        driver.get(url) 
        #driver.maximize_window()  
        sleep(20)
        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[1]/ul[1]/li[1]/button[1]")
        driver.execute_script("arguments[0].click();", content)#using this by avoid to can not apoach the buttom
        #content.click()  
        sleep(2) 
        #print("1start to get name....")  
        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[1]/div[1]/h3[1]")
       
        mystock_name.append (content.text)
        name = content.text
        #print(content.text) 

        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[2]/ul[1]/li[2]/span[1]/span[1]")
        #print("11start to get today price....")  
        #print(content.text)  
        if (content.text == '' or content.text == '--' or content.text == None)  :
            print("failed !!!!!!!! ") 
            driver.close()
            driver.quit()
            exit();
        else :
            #print("PASS check!??? !!!!!!!! see next ascii =  "+ ascii(content.text)) 
            contentNow = float(content.text)
 

        #print(contentNow) # 把排版後的 html 印出來
        #print("111 start to get aveavages of 5")  
        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/span[1]/ul[1]/li[2]/label[1]/span[1]")
        #print(content.text)
        content5 = float(content.text)
        #print(content5) # 把排版後的 html 印出來
        #print("1111 start to get aveavages of 20")  
        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/span[1]/ul[1]/li[4]/label[1]/span[1]")
        #print(content.text)    
        content20 = float(content.text)
        #print(content20) # 把排版後的 html 印出來

        #print("11111  start to get aveavages of 60")    
        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/span[1]/ul[1]/li[5]/label[1]/span[1]")
        #print(content.text)    
        content60 = float(content.text)
        #print(content60) # 把排版後的 html 印出來


        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[3]/span[1]/ul[1]/li[2]/span[1]")
        #print(content.text)
        kdk =float(content.text)
        #print(kdk) # 把排版後的 html 印出來



        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[3]/span[1]/ul[1]/li[3]/span[1]")
        #print(content.text)
        kdd = float(content.text)
        #print(kdd) # 把排版後的 html 印出來
        
        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[1]/ul[1]/li[2]/button[1]")
        driver.execute_script("arguments[0].click();", content)#using this by avoid to can not apoach the buttom
        #content.click()  
        
        content = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/main[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[3]/span[1]/ul[1]/li[2]/span[1]")
        #print(content.text)
        wkdk = float(content.text)
        #print(wkdk) # 把排版後的 html 印出來

        content560 = ((content5 - content60)/content60)*100
        content2060 = ((content20 - content60)/content60)*100
        content520 = ((content5 - content20)/content20)*100
        contentNow_5 = ((contentNow - content5)/content5)*100
        content560 = round(content560, 2)
        content2060 = round(content2060, 2)
        content520 = round(content520, 2)
        contentNow_5 = round(contentNow_5, 2)
        # Totol vaule all be put to val for Numpy arrary
        
        vals = [contentNow_5,content520,content560,content2060,kdk,kdd,wkdk,contentNow,content5,content20,content60]
 

        vals = [contentNow_5,content520,content560,content2060,kdk,kdd,wkdk,contentNow,content5,content20,content60]
        print(i,'=', mystock_name[i], vals)
        mystock[i,] = vals
        print(i,'=', mystock_name[i], vals, file=filename)
    
    return mystock


def check_2060_vaule(ft,tt,tstock_name,tstock_num,fstock_name,fstock_num,timex, allVlue,mt,mystock_name,mystock_num,filename):


    TrustInvestment = tt
    foreignInvestment =ft
    mystock = mt
    comparefor520 = 2.7
    comparefor560 = 2.1
    print('check_2060_vaule  ========================================', file=filename)


    print('投信.....comparefor520.....')
    print('投信  .....comparefor520......', file=filename)
    for i in range(0,len(tstock_num)):

        if TrustInvestment[i, 1]  < comparefor520 and TrustInvestment[i, 1] > 0 :          
            print('<'+' =',comparefor520 ,tstock_name[i] ,TrustInvestment[i, 1])
            print('<'+' =',comparefor520 ,tstock_name[i] ,TrustInvestment[i, 1], file=filename)

            
    print('外資.......comparefor520...')
    print('外資  .....comparefor520......', file=filename)
    for i in range(0,len(fstock_num)):

        if foreignInvestment[i, 1]  < comparefor520  and foreignInvestment[i, 1] > 0:          
            print('<'+' =',comparefor520 ,fstock_name[i] ,foreignInvestment[i, 1])
            print('<'+' =',comparefor520 ,fstock_name[i] ,foreignInvestment[i, 1], file=filename)
            

    

    print('投信.......comparefor560...')
    print('投信  .....comparefor560......', file=filename)
    for i in range(0,len(tstock_num)):
        
        if TrustInvestment[i, 2]  < comparefor560 and  TrustInvestment[i,2] > 0:          
            print('<'+' =',comparefor560 ,tstock_name[i] ,TrustInvestment[i, 2])
            print('<'+' =',comparefor560 ,tstock_name[i] ,TrustInvestment[i, 2], file=filename)      
    print('外資.......comparefor560...')
    print('外資  .....comparefor560......', file=filename)

    for i in range(0,len(fstock_num)):
        
        if foreignInvestment[i, 2]  < comparefor560 and  foreignInvestment[i,2] > 0:    
            print('<'+' =',comparefor560 ,fstock_name[i] ,foreignInvestment[i, 2])
            print('<'+' =',comparefor560 ,fstock_name[i] ,foreignInvestment[i, 2], file=filename)
    print('自選.........comparefor520....')
    print('自選.........comparefor520....',file=filename)
    '''
    print(mystock_name)
    print(type(mystock_name))
    print(mystock_num)
    print(mystock)
    '''
    for i in range(0,len(mystock_num)):

        if mystock[i, 1]  < comparefor520 and mystock[i, 1] > 0:     
            print('<'+' =' ,comparefor520 ,mystock_name[i],mystock[i,1] )
            print('<'+' =' ,comparefor520 ,mystock_name[i],mystock[i,1] , file=filename)
    print('自選.........comparefor560....')
    print('自選.........comparefor560....',file=filename)
    for i in range(0,len(mystock_num)):
        
        if mystock[i, 2]  < comparefor560 and mystock[i, 2] > 0 :
            print('<'+' =' ,comparefor560 ,mystock_name[i],mystock[i,2] )
            print('<'+' =' ,comparefor560 ,mystock_name[i],mystock[i,2] , file=filename)

check.ifCreate() 
check.ifalreadyGet()
driver = webdriver.Chrome(chrome_options=options, executable_path=r'/home/pi/work/stock/getPrice/i386/usr/bin/chromedriver')
##driver = webdriver.Chrome(chrome_options=options, executable_path=r'/home/pi/work/stock/getPrice/chromedriver_linux64/chromedriver')
###driver=webdriver.Chrome(executable_path='/home/pi/work/stock/getPrice/chromedriver_linux64/chromedriver')
driver.get(url) 
driver.maximize_window()  
sleep(2)  
login(timex)
ret = check.iftodaybuy(timex,driver)
if (ret == 1): 
    filename = toGetTimeFile(times)
    toGetTstock(tstock_name,tstock_num,timex,filename)
    toGetFstock(fstock_name,fstock_num,timex,filename)
    toGetTstock(tstock_name,tstock_num,timex,filename)
    ft = toGetFstockParmeter(fstock_name,fstock_num,timex,allVlue,filename)
    tt = toGetTstockParmeter(tstock_name,tstock_num,timex,allVlue,filename)
    mt = toGetMystockParmeter(timex,filename)
    check_2060_vaule(ft,tt,tstock_name,tstock_num,fstock_name,fstock_num,timex, allVlue,mt,mystock_name,mystock_num,filename)
    ##########  this is for test =>  check_2060_vaule(0,0,0,0,0,0,0, 0,mt,mystock_name,mystock_num,filename)
    filename.close()

else:
    print("Wantgoo has not updated web for this info, SKIP !")   


driver.close()
driver.quit()    


