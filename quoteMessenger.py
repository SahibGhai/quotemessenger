import requests
import json
import random
from dotenv import load_dotenv
import pytextnow as ptn
import os

load_dotenv()

#Set credentials
USERNAME = os.getenv("USERNAME")
SID = os.getenv("SID")
CSRF = os.getenv("CSRF")
PHONE = os.getenv("PHONE")

client = ptn.Client(USERNAME, sid_cookie=SID, csrf_cookie=CSRF)


#Function to connect to the internet
def connect_to_internet():
	print("Please connect to the internet, if it still does not work please check the endpoint.")

#Function to parse JSON info and send request
def jsonManagement():
	URL = "https://type.fit/api/quotes"
	request = requests.get(URL) #Send request

	#Start parsing process
	jsonl = len(json.loads(request.text)) #serializes into python type list and gets len
	jsonS = json.loads(request.text) #serializes into python type list
	randQuote = jsonS[random.randint(0,jsonl)]["text"] #find rand index and then get value of text key from dictionary
	return randQuote

#Function to send message
def sendMessage(quote):
	client.send_sms(PHONE, quote) #Send message


#Error Handling
try:
	quote = jsonManagement() #Set variable for sendMessage parameter to the return value from jsonManagement
	sendMessage(quote)

except:
	connect_to_internet()
