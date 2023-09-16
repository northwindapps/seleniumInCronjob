#use selenium driver
from dotenv import dotenv_values
from flask import Flask, request, jsonify
from flask_cors import CORS

config = dotenv_values(".env")

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


application= Flask(__name__)
CORS(application)
@application.get("/")
def get_hello():
    response_data = {"message": "hi"}
    return jsonify(response_data)

@application.get("/current_price")
def get_price():
    try:
        stock_name = request.args.get('stock_name')
        currency = request.args.get('currency')
        other = request.args.get('other')
        type = request.args.get('type')
        now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))

        options = Options()
        # options.headless = True
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

        url = "https://www.google.com/search?q="

        query=stock_name + '+stock price' 

        if other != None:
            query=query + '+' + other

        url = url + query

        print(url)

        driver.get(url)

        if type == '0':
            print("crypto")
            pc_price_tag = driver.find_element(By.CLASS_NAME, 'pclqee')

        elif type == '1':
            print("stock")
            pc_price_tag = driver.find_element(By.XPATH, "//span[@jsname='vWLAgc']")
        else:
            print("Invalid choice.")
            pc_price_tag = None

        print(pc_price_tag.get_attribute('innerHTML'))

        # if is_float(pc_price_tag.get_attribute('innerHTML')):
        response_data = {"current_value": pc_price_tag.get_attribute('innerHTML')}
        # else:
            # response_data = {"current_value": None}
        return jsonify(response_data)

    except TimeoutException:
        print("Timeout exception occurred. Page took too long to load.")
        response_data = {"current_value": None}
        return jsonify(response_data)
    except NoSuchElementException:
        print("Element not found. Check if the element selector is correct.")
        response_data = {"current_value": None}

        pc_price_tags = driver.find_elements(By.TAG_NAME,'span')
        for element in pc_price_tags:
            print(element)

        return jsonify(response_data)
    except TypeError as e:
        print("Caught a TypeError:", e)
        response_data = {"current_value": None}
        return jsonify(response_data)
    except Exception as e:
        print("An error occurred:", e)
        response_data = {"current_value": None}
        return jsonify(response_data)

    finally:
        # Close the browser when done
        driver.quit()

def is_float(string):
    try:
        float_value = float(string)
        return True
    except ValueError:
        return False
    
if __name__ == "__main__":
    application.run(host="0.0.0.0", port='8000')
