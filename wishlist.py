from dotenv import dotenv_values
config = dotenv_values(".env")

from selenium import webdriver

#exception
from selenium.common.exceptions import NoSuchElementException

#keys to enter input data into fields 
from selenium.webdriver.common.keys import Keys

#time module to put some delay in the process
import time 

import json

import datetime

import pytz 

#from selenium.webdriver.remote import mobile

from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
#options.add_argument("headless")
#options.add_argument("no-sandbox")
#options.add_argument("window-size=420,380")
#options.add_argument('--ignore-certificate-errors')
#options.add_argument("--remote-debugging-port=9222")
#options.add_argument("enable-automation")
#options.add_argument("--disable-gpu")
#options.add_argument("--disable-dev-shm-usage")
#driver = webdriver.Chrome(options=options)
#driver = webdriver.Chrome('/usr/bin/chromedriver',options=options)

driver = webdriver.Chrome(options=options)

#initialize the driver

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
driver.get("https://auctions.yahoo.co.jp/openwatchlist/jp/show/mystatus?select=watchlist&watchclosed=0")

time.sleep(2) #2 second time delay

# https://stackoverflow.com/questions/54862426/python-selenium-get-href-value/54862902
elems = driver.find_elements_by_css_selector(".ItemTable__itemTitle [href]")
elems2 = driver.find_elements_by_css_selector(".ItemTable__itemTitle")
allNames = [elem.text for elem in elems2]
allLinks = [elem.get_attribute('href') for elem in elems]

elems3 = driver.find_elements_by_css_selector(".ptsLinkItem [src]")
allImgs = [elem.get_attribute('src') for elem in elems3]


jsonList = []
for idx, val in enumerate(allNames):
    jsonList.append({"name" : allNames[idx],  "url": allLinks[idx], "photo": allImgs[idx]})

with open('/home/bitnami/htdocs/app/itemList.json','w',encoding='utf-8') as f: json.dump(jsonList,f,ensure_ascii= False, indent=4)

print("itemList updated")
print(datetime.datetime.now(pytz.timezone('Asia/Tokyo')))

# save them into a json file
driver.close()
driver.quit()
