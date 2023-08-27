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

app = Flask(__name__)
CORS(app)
@app.get("/current_price")
def get_price():
    stock=name = request.args.get('stock_name')
    currency = request.args.get('currency')
    other = request.args.get('other')
    now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))

    options = Options()
    # options.headless = True
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)


    #open facebook.com with chrome
    driver.get("https://www.google.com/search?q=btc+price+in+usd&sca_esv=560417221&sxsrf=AB5stBhndKHAq6_Xhd6IkMGECmUprMSxew%3A1693108649528&ei=qcnqZIHzH5Xq-AbU34iQCQ&ved=0ahUKEwjB6_uc-fuAAxUVNd4KHdQvApIQ4dUDCA8&uact=5&oq=btc+price+in+usd&gs_lp=Egxnd3Mtd2l6LXNlcnAiEGJ0YyBwcmljZSBpbiB1c2QyChAAGIAEGEYYggIyBRAAGIAEMgUQABiABDIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeSMwUUKEHWIwScAF4AZABAJgBmQGgAcgGqgEDMC43uAEDyAEA-AEBwgIKEAAYRxjWBBiwA8ICChAAGIoFGLADGEPCAgcQABiKBRhDwgIKEAAYgAQYFBiHAuIDBBgAIEGIBgGQBgo&sclient=gws-wiz-serp")

    # email_input_box = driver.find_element(By.ID, 'login_handle')
    # print(email_input_box)

    # login_button = driver.find_element(By.XPATH, '//button[text()="次へ"]')
    # login_button.click()
    # print(login_button)

    pc_price_tag = driver.find_element(By.CLASS_NAME, 'pclqee')

    print(pc_price_tag.get_attribute('innerHTML'))

    response_data = {"current_value": pc_price_tag.get_attribute('innerHTML')}
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)