#!/usr/bin/env python3


import smtplib
import numpy as np
import requests
import json
import os
import stat


st = os.stat('Bitcoin Price Schedule.py')
os.chmod('Bitcoin Price Schedule.py', st.st_mode | stat.S_IEXEC)

# put here your webhook_url obtained from the steps above
webhook_url = " https://hooks.slack.com/services/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"

# url for bitcoin stock info
btc_url = "https://query1.finance.yahoo.com/v7/finance/quote?&symbols=BTC-USD&fields=extendedMarketChange,\
extendedMarketChangePercent,extendedMarketPrice,extendedMarketTime,regularMarketChange,regularMarketChangePercent,\
regularMarketPrice,regularMarketTime,circulatingSupply,ask,askSize,bid,bidSize,dayHigh,dayLow,regularMarketDayHigh,\
regularMarketDayLow,regularMarketVolume,volume"


response = requests.get(btc_url)
data = response.json()
btc_price = data["quoteResponse"]["result"][0]["regularMarketPrice"]

payload = {
    "channel": "#random",
    "username": "BTC PRICE",
    "text": f"${btc_price:,.2f}",
    "icon_emoji": ":dollar:"
}
requests.post(webhook_url, data=json.dumps(payload))

# setting up the desired message you want to see once the stock is at a certain level
sender_email = "example@gmail.com"
rec_email = "example@gmail.com"

password = " "

# message you want sent to you
message = "BTC stock is currently at " + "%.6f" % btc_price

# enter the price you want to sell at
target_sell_price = 38000

if btc_price > target_sell_price:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)  # logs into your email account
    print("Login Success")  # confirms that you have logged in

    server.sendmail(sender_email, rec_email, message)  # sends the email with your custom message
    print("Email was sent")  # confirms that the email was sent

else:
    print('Failed to login')