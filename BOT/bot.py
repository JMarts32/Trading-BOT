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
ACCOUNT_URLS='{}/v2/account'.format(BASE_URL)
ORDERS_URL='{}/v2/orders'.format(BASE_URL)
HEADERS={'APCA-API-KEY-ID':API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}

credentials.close()


# function to connect to the account
