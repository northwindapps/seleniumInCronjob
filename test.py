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
# f = open("./schedule.json", "r")
# f = json.loads("./schedule.json")
# content = f.read()
# print(f)
# jList = json.loads(content)

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
#open facebook.com with chrome
driver.get("https://login.yahoo.co.jp/config/login?.src=www&.done=https://www.yahoo.co.jp/")
#access facebook login email input
email_input_box = driver.find_element("id", "login_handle")
print(email_input_box.get_attribute("placeholder"))
#clear the placeholders data
email_input_box.clear()
