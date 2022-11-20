import requests, json
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
@param: type -> limit or market entry
@param: time_in_force -> moment to create the order
"""
def create_order(symbol,qty,side,type,time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }


# function to get all the orders made
def get_orders():
    request = requests.get(ORDERS_URL, headers=HEADERS)
    return json.loads(request.content)