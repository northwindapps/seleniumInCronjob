
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

    url = "https://www.seinfeldscripts.com/TheMarineBiologist.htm"

    # query=stock_name + '+stock price' 

    #if other != None:
    #    query=query + '+' + other

    # url = url + query

    print(url)

    driver.get(url)

    # if stock_type == 0:
    #     print("crypto")
    #     pc_price_tag = driver.find_element(By.CLASS_NAME, 'pclqee')

    # elif stock_type == 1:
    #     print("stock")
    #     pc_price_tag = driver.find_element(By.XPATH, "//span[@jsname='vWLAgc']")
    # else:
    #     print("Invalid choice.")
    p_elements = driver.find_elements(By.TAG_NAME,'p')

    speakers = [];
    lines = [];

    # Extract text from each <p> element and print it
    for p_element in p_elements:
        p_text = p_element.text
        parts = p_text.split(":")
        # Trim whitespace from the resulting strings
        parts = [part.strip() for part in parts]
        # Create a list from the parts
        result_list = parts
        if result_list and len(result_list) == 2 and not all(item == '' for item in result_list):
            speakers.append(result_list[0])
            lines.append(result_list[1])

    # Create a list of dictionaries
    data = [{'speaker': s, 'line': l} for s, l in zip(speakers, lines)]

    # Specify the JSON file name
    json_file_name = 'conversation.json'

    # Write the data to a JSON file
    with open(json_file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f'Data written to {json_file_name}')

except Exception as e:
    print("An error occurred:", e)


finally:
    print('finally')
    # Close the browser when done
    #driver.quit()
