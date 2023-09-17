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

@application.get("/current_price_b")
def get_price_plan_b():
    try:
        # Replace these variables with your own values
        api_key = "AUN1ZO2ZXPC9N0JW"
        # stock_symbol = "AAPL"
        interval = "1min"
        stock_symbol = request.args.get('stock_name')


        # Construct the API URL
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_symbol}&interval={interval}&apikey={api_key}"

        # Make the API request
        response = requests.get(url)

        # Parse the JSON response
        data = response.json()

        # Extract the current stock price (assuming you want the most recent data point)
        latest_data_point = data["Time Series ({})".format(interval)]
        latest_price = latest_data_point[list(latest_data_point.keys())[0]]["4. close"]

        print(f"The current price of {stock_symbol} is ${latest_price}")
        response_data = {"current_value": latest_price}
        return jsonify(response_data)

    except Exception as e:
        print("An error occurred:", e)
        response_data = {"current_value": None}
        return jsonify(response_data)
    
    finally:
        print('finally')
        # Close the browser when done
        #driver.quit()



@application.get("/current_price")
def get_price():
    try:
        stock_name = request.args.get('stock_name')
        currency = request.args.get('currency')
        other = request.args.get('other')
        stock_type = request.args.get('type')
        now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
        options = Options()
        options.add_argument('--disable-gpu')
        options.add_argument('--verbose')
        options.add_argument('--headless')
        options.binary_location = '/usr/bin/google-chrome'
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        
        url = "https://www.google.com/search?q="
        #query=stock_name + '+stock price' 
        #url = url + query

        #print(url)

        #driver.get(url)

        if stock_type == '0':
            print("crypto")
            query=stock_name + '+price usd'
            url = url + query
            driver.get(url)
            pc_price_tag = driver.find_element(By.CLASS_NAME, 'pclqee')

        elif stock_type == '1':
            print("stock")
            query=stock_name + '+stock price'
            url = url + query
            print(url)
            driver.get(url)
            pc_price_tag = driver.find_element(By.XPATH, "//span[@jsname='vWLAgc']")
        else:
            print("Invalid choice.")
            pc_price_tag = None

        if pc_price_tag != None:
            #print(pc_price_tag.get_attribute('innerHTML'))

            # if is_float(pc_price_tag.get_attribute('innerHTML')):
            response_data = {"current_value": pc_price_tag.get_attribute('innerHTML')}
        else:
            response_data = {"current_value": None}
        
        driver.quit()
        return jsonify(response_data)

    except TimeoutException:
        print("Timeout exception occurred. Page took too long to load.")
        driver.quit()
        response_data = {"current_value": None}
        return jsonify(response_data)
    except NoSuchElementException:
        print("Element not found. Check if the element selector is correct.")
        driver.quit()
        response_data = {"current_value": None}
        return jsonify(response_data)
    except TypeError as e:
        print("Caught a TypeError:", e)
        driver.quit()
        response_data = {"current_value": None}
        return jsonify(response_data)
    except Exception as e:
        print("An error occurred:", e)
        driver.quit()
        response_data = {"current_value": None}
        return jsonify(response_data)

    finally:
        # Close the browser when done
        if 'driver' in locals():
            driver.quit()
            print('driver quit')
        print('end')

def is_float(string):
    try:
        float_value = float(string)
        return True
    except ValueError:
        return False
    
if __name__ == "__main__":
    application.run(host="0.0.0.0", port='80')
