
from selenium import webdriver

#exception
from selenium.common.exceptions import NoSuchElementException

#keys to enter input data into fields 
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

#time module to put some delay in the process
import time 

#json
import json

import datetime

import pytz 

from selenium.webdriver.remote import mobile

from selenium.webdriver.chrome.options import Options

from selenium.common.exceptions import TimeoutException, NoSuchElementException


try:
    #stock_name = request.args.get('stock_name')
    stock_name = 'appl'
    stock_type = 1
    #currency = request.args.get('currency')
    #other = request.args.get('other')
    #stock_type = request.args.get('type')
    #now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))

    options = Options()
    #options.headless = True
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--verbose')
    options.add_argument('--headless')
    options.binary_location = '/usr/bin/google-chrome'
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    #options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)

    url = "https://www.google.com/search?q="

    query=stock_name + '+stock price' 

    #if other != None:
    #    query=query + '+' + other

    url = url + query

    print(url)

    driver.get(url)

    if stock_type == 0:
        print("crypto")
        pc_price_tag = driver.find_element(By.CLASS_NAME, 'pclqee')

    elif stock_type == 1:
        print("stock")
        pc_price_tag = driver.find_element(By.XPATH, "//span[@jsname='vWLAgc']")
    else:
        print("Invalid choice.")
        pc_price_tag = None
    
    if pc_price_tag != None:
        print(pc_price_tag.get_attribute('innerHTML'))
    driver.quit()
except Exception as e:
    print("An error occurred:", e)


finally:
    print('finally')
    # Close the browser when done
    #driver.quit()
