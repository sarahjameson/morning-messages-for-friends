# A selection of good morning texts to send
good_morning_messages = [
    "Good morning friend!",
    "I hope you have a great day!",
    "You got this!",
    "You're amazing!",
    "Hot to trot ;-)"
]

# Import
import os
from twilio.rest import Client
import schedule
import random
import time

# Variables
phone =  "+3530831022401"
twilio_number = "+12244123664"
good_morning_message = random.choice(good_morning_messages)

# API details for sending message
def send_message(message=good_morning_message):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    client.messages.create(to=phone,from_=twilio_number,body=message)


# Use a schedule for message so that it arrives every morning
schedule.every().day.at("06:30").do(send_message)

# Ensures while there is a scheduled event, it will keep running
while True:
    schedule.run_pending()
    time.sleep(2)

