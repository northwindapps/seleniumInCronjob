import requests

try:
    # Replace these variables with your own values
    api_key = "AUN1ZO2ZXPC9N0JW"
    stock_symbol = "AAPL"
    interval = "1min"

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


except Exception as e:
    print("An error occurred:", e)


finally:
    print('finally')
    # Close the browser when done
    #driver.quit()
