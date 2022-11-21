import requests, json
import pandas as pd
import alpha_vantage.timeseries as TimeSeries
import alplha_vantage.techindicators as TechIndicators
import matplotlib.pyplot as plt
"""
The sintaxis of the "./Credentials/credentials.csv" might change
if you are using Linux, MAC OS or Windows.


Windows = "./Credentials/credentials.csv"
MAC OS = "../Credentials/credentials.csv"
Linux = "../Credentials/credentials.csv"

REMEMBER!
Create a file called "credentials.csv" in the Credentials folder
to acces your account
"""
credentials = open("./Credentials/credentials.csv","r")

# These are the variables that will allow to connect with the API
API_KEY=credentials.readline()
SECRET_KEY=credentials.readline()
BASE_URL='https://paper-api.alpaca.markets'
ACCOUNT_URL='{}/v2/account'.format(BASE_URL)
ORDERS_URL='{}/v2/orders'.format(BASE_URL)
HEADERS={'APCA-API-KEY-ID':API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}

credentials.close()


# function to connect to the account
def get_account():
    request = requests.get(ACCOUNT_URL,headers=HEADERS)
    return json.loads(request.content)

"""
Function to place an order into the broker using the API

@param: symbol -> The company we want to buy
@param: qty -> amount of units
@param: side -> buy or sell
@param: type -> limit (specific price) or market price
@param: time_in_force -> moment to create the order
@param: limit_price -> when it reaches that price it takes profit
@param: stop_loss -> when it reaches that price it assumes a loss
"""
def create_order(symbol,qty,side,type,time_in_force,limit_price,stop_loss):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force,
        "take_profit": {"limit_price": limit_price},
        "stop_loss":{"stop_loss": stop_loss},
    }
    request = requests.post(ORDERS_URL, json=data, headers=HEADERS)
    return json.loads(request.content)


# function to get all the orders made
def get_orders():
    request = requests.get(ORDERS_URL, headers=HEADERS)
    return json.loads(request.content)

"""
Function to get the information of the bars for the specific company's

@param: temp -> temporality wanted to analyze
@param: symbols -> The companies you wany to analyze
@param: qty -> amount of bars you want to analyze
"""
def get_bars(temp,symbols,qty):
    data = "{}/bars/{}?symbols={}&limit={}".format(BASE_URL,temp,symbols,qty)
    request = requests.get(data, headers=HEADERS)
    json_data = json.dumps(request.content,indent=4)
    return json_data

"""
Function to convert the json information of the bars into a data frame
to analyze with pandas

@param: jsonBars -> the Json with the information
@param: qty -> amount of bars that want to be analyzed
"""
def get_bars_dataFrame(jsonBars,qty):
    dataFrame = pd.read_json(jsonBars)
    return dataFrame.head(qty)