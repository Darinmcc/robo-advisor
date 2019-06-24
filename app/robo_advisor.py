# app/robo_advisor.py

import requests # to make requests for https package - need to install request package in virtual environme
from dotenv import load_dotenv

import json #use to convert json string to dictionary #module don't need to install in virtual part of python
import datetime #module
import calendar # module
import csv # module
import os # module

load_dotenv() #> loads contents of the .env file into the script's environment


def to_usd(my_price):
    return "${0:,.2f}".format(my_price)




#
# INFO INPUTS
#
print("Welcome to Robo Advisor!")
print("------------------------")
symbol = input("Enter stock symbol:")
uppersymbol = symbol.upper()
#breakpoint()
if symbol.isalpha() != True:
    print("Not a valid stock symbol. Please re-run")
    exit()
elif len(symbol) > 4:
    print("Not a valid stock symbol. Please re-run")
    exit()

api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={uppersymbol}&apikey={api_key}" # variable for Url

response = requests.get(request_url) #< response variable - sends get requests, specify the URL for the request - see documentation
risk_options = ["cautious", "balanced", "aggressive"]
risk_profile = input("Please enter your risk tolerance: 'cautious', 'balanced', 'aggressive'      ")
if risk_profile not in risk_options:
    print("Risk profile should be: 'cautious', 'balanced', or 'aggressive'. Please try again")
    exit()

#print(type(response)) <data type - class 'requests.models.Response
#print(response.status_code) <200 - successful #status code attribute - https lets us know how successful the request was, and 
#print(response.text) <actual body of response. #string need to convert to dictionary
#print(type(response.text)) <class 'str'

parsed_response =json.loads(response.text) # variable, parse str to dict

#parsed_reponse - type() = dict, parsed_reponse.keys() = top keys
#parsed_response["Meta Data"].keys()

#
#INFO OUTPUTS
#

now = datetime.datetime.now().replace(microsecond=0)
AMPM = now.strftime("%p")

last_refreshed =parsed_response["Meta Data"]["3. Last Refreshed"]

tsd =parsed_response["Time Series (Daily)"]
#assumes latest day is first, consider sorting
#dates[0]
dates =list(tsd.keys())
last_close = dates[0]
latest_close = tsd[last_close]["4. close"]

high_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))
recent_high = max(high_prices)


low_prices = []

for date in dates:
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))
recent_low = min(low_prices)

#max_high = [high for high in parsed_response["Time Series (Daily)"][f"{last_tradedate}"]["2. high"] ]

latest_close_usd = to_usd(float(latest_close))
recent_high_usd = to_usd(float(recent_high))
recent_low_usd = to_usd(float(recent_low))




csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")
 #don't change csv file path or __file__ variable
 #file starts in app directory

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": date, 
            "open": daily_prices["1. open"], 
            "high": daily_prices["2. high"], 
            "low": daily_prices["3. low"], 
            "close": daily_prices["4. close"], 
            "volume": daily_prices["5. volume"]})

#timestamp, open, high, low, close, volume
#2018-06-04, 101.2600, 101.8600, 100.8510, 101.6700, 27172988

print("-------------------------")
print(f"SELECTED SYMBOL: {uppersymbol}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print(f"REQUEST AT: {now} {AMPM}")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {latest_close_usd}")
print(f"RECENT HIGH: {recent_high_usd}")
print(f"RECENT LOW: {recent_low_usd}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

#def weekday(good_date):
    #if good_date == 5:
        #return prev_day
    #elif good_date == 6:
        #return two_days
    #else:
        #return today
#today = datetime.date.today()
#prev_day = datetime.date.today()-datetime.timedelta(1)
#two_days = datetime.date.today()-datetime.timedelta(2)
#today_year = today.year
#today_month = today.month
#today_day = today.day
#print(calendar.weekday(2019,6,26))
#weekdaynum = calendar.weekday(today_year,today_month,today_day)
#last_tradedate = weekday(weekdaynum)