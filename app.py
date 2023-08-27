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


app = Flask(__name__)
CORS(app)
@app.get("/current_price")
def get_price():
    try:
        stock_name = request.args.get('stock_name')
        currency = request.args.get('currency')
        other = request.args.get('other')
        print(stock_name)
        print(currency)
        now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))

        options = Options()
        # options.headless = True
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

        driver.get("https://www.google.com/search?q=btc+price+in+usd&sca_esv=560417221&sxsrf=AB5stBhndKHAq6_Xhd6IkMGECmUprMSxew%3A1693108649528&ei=qcnqZIHzH5Xq-AbU34iQCQ&ved=0ahUKEwjB6_uc-fuAAxUVNd4KHdQvApIQ4dUDCA8&uact=5&oq=btc+price+in+usd&gs_lp=Egxnd3Mtd2l6LXNlcnAiEGJ0YyBwcmljZSBpbiB1c2QyChAAGIAEGEYYggIyBRAAGIAEMgUQABiABDIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeSMwUUKEHWIwScAF4AZABAJgBmQGgAcgGqgEDMC43uAEDyAEA-AEBwgIKEAAYRxjWBBiwA8ICChAAGIoFGLADGEPCAgcQABiKBRhDwgIKEAAYgAQYFBiHAuIDBBgAIEGIBgGQBgo&sclient=gws-wiz-serp")


        pc_price_tag = driver.find_element(By.CLASS_NAME, 'pclqee2')

        print(pc_price_tag.get_attribute('innerHTML'))

        response_data = {"current_value": pc_price_tag.get_attribute('innerHTML')}
        return jsonify(response_data)

    except TimeoutException:
        print("Timeout exception occurred. Page took too long to load.")
        response_data = {"current_value": None}
        return jsonify(response_data)
    except NoSuchElementException:
        print("Element not found. Check if the element selector is correct.")
        response_data = {"current_value": None}
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)