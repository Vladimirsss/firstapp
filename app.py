
# import requests library
import requests

#import json library
import json

print("this is first app")
# put the ip address or dns of your apic-em controller in this url
url = 'https://api.ciscospark.com/v1/people/me'

#the username and password to access the APIC-EM Controller
#payload = {"username":"admin","password":"C!sc0123"}
payload = {}

#Content type must be included in the header
header = {"Authorisation": "Bearer M2RkNzJjNGQtY2UwNS00NGJkLThiOTgtNmQ2Y2VjYzdjMDI0YWY3N2ZjZGEtYzUz"}
header = {"content-type": "application/json"}

#Performs a POST on the specified url.
response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)

# print the json that is returned
print("Response: " + response.text)
