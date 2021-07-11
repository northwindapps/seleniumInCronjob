#use selenium driver
from dotenv import dotenv_values
config = dotenv_values(".env")

from selenium import webdriver

#exception
from selenium.common.exceptions import NoSuchElementException

#keys to enter input data into fields 
from selenium.webdriver.common.keys import Keys

#time module to put some delay in the process
import time 

#json
import json

import datetime

import pytz 

from selenium.webdriver.remote import mobile

from selenium.webdriver.chrome.options import Options

now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))

YEAR = str(now.year)
MONTH = str(now.month)
DATE = str(now.day)
HOUR = str(now.hour) 
MINUTE = str(now.minute)
# now.weekday
BIDDATE = YEAR + '-'

if(len(MONTH) == 1):
    BIDDATE += '0' + MONTH + '-'
else:
    BIDDATE +=  MONTH + '-'

if(len(DATE) == 1):
    BIDDATE += '0' + DATE + '-'
else:
    BIDDATE +=  DATE + '-'

if(len(HOUR) == 1):
    BIDDATE += '0' + HOUR + ':'
else:
    BIDDATE +=  HOUR + ':'

if(len(MINUTE) == 1):
    BIDDATE += '0' + MINUTE
else:
    BIDDATE +=  MINUTE

print('BIDDATE',BIDDATE)


#TODO read json data,retrieve item list
f = open("./schedule.json", "r")
# f = json.loads("./schedule.json")
content = f.read()
# print(f)
jList = json.loads(content)

bidNameList = []
bidPriceList = []
bidUrlList = []
bidDateList = []

for idx, val in enumerate(jList):
    commafree = jList[idx]["price"]
    commafree = commafree.replace(',','')
    bidNameList.append(jList[idx]["name"])
    bidPriceList.append(commafree)
    bidUrlList.append(jList[idx]["url"])
    bidDateList.append(jList[idx]["date"])
    if(bidDateList[idx] == BIDDATE):
        print('MATCH')

        print(bidPriceList[idx])
        print(bidDateList[idx])
        print(bidUrlList[idx])

# TODO Date,price,url Checking
for idx, val in enumerate(bidDateList):
    if(bidDateList[idx] == BIDDATE and bidPriceList[idx].isdecimal() == True and len(bidUrlList[idx]) > 0 ):
        options = Options()
        options.headless = True

        driver = webdriver.Chrome(options=options)

        #open facebook.com with chrome
        driver.get("https://login.yahoo.co.jp/config/login?.src=www&.done=https://www.yahoo.co.jp/")

        #My Facebook credentials
        my_email = config["EMAIL"]
        my_password= config["PASS"]

        #access facebook login email input
        email_input_box = driver.find_element_by_name("login")

        #clear the placeholders data
        email_input_box.clear()

        #fill login credentials
        email_input_box.send_keys(my_email)

        time.sleep(2)

        #access facebook login button
        login_button = driver.find_element_by_name("btnNext")

        #hit the login button
        login_button.click()

        time.sleep(2) #2 second time gap between filling email and password

        #access facebook login password input
        password_input_box = driver.find_element_by_name("passwd")

        password_input_box.clear()

        password_input_box.send_keys(my_password)

        time.sleep(2) #2 second time delay

        login_button2 = driver.find_element_by_name("btnSubmit")
        #hit the login button
        login_button2.click()




        # my watch list https://auctions.yahoo.co.jp/openwatchlist/jp/show/mystatus?select=watchlist&watchclosed=0
        #open facebook.com with chrome
        driver.get(bidUrlList[0])

        time.sleep(2) #2 second time delay

        #modal
        try:
            login_button3 = driver.find_element_by_id("js-prMdl-close")           
            #hit the login button
            login_button3.click()
            time.sleep(2) 
        except NoSuchElementException:
            print('nosuch element')


        bid_button = driver.find_element_by_xpath("//a[text()='入札する']").click();
        time.sleep(1) 

        bidprice_input_box = driver.find_element_by_name("Bid")

        bidprice_input_box.clear()

        bidprice_input_box.send_keys(bidPriceList[0])

        time.sleep(2) #2 second time delay

        bid_confirm_button = driver.find_element_by_xpath("//input[@value='確認する']").click();
        time.sleep(1) 

        # https://stackoverflow.com/questions/38534241/how-to-locate-a-span-with-a-specific-text-in-selenium-using-java
        bid_submit_button = driver.find_element_by_xpath("//span[.='入札する']").click();
        time.sleep(1) 

        driver.close()
        driver.quit()
        print('bidfile read')
    	
print(datetime.datetime.now(pytz.timezone('Asia/Tokyo')))
