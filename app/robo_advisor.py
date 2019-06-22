# app/robo_advisor.py

import requests # to make requests for https package - need to install request package in virtual environme
import json #use to convert json string to dictionary #module don't need to install in virtual part of python
import datetime

now = datetime.datetime.now().replace(microsecond=0)

AMPM = now.strftime("%p")

#
# INFO INPUTS
#
request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo" # variable for Url

response = requests.get(request_url) #< response variable - sends get requests, specify the URL for the request - see documentation

#print(type(response)) <data type - class 'requests.models.Response

#print(response.status_code) <200 - successful #status code attribute - https lets us know how successful the request was, and 

#print(response.text) <actual body of response. #string need to convert to dictionary

#print(type(response.text)) <class 'str'

parsed_response = json.loads(response.text) # variable, parse str to dict

#breakpoint()

#parsed_reponse - type() = dict, parsed_reponse.keys() = top keys
#parsed_response["Meta Data"].keys()



#
#INFO OUTPUTS
#

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]






print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print(f"REQUEST AT: {now} {AMPM}")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")