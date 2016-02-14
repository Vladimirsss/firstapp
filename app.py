
import requests
from urllib.request import Request, urlopen
import json


print("<<<start>>>")

# put the ip address or dns of your apic-em controller in this url
url = 'https://api.ciscospark.com/v1/people/me'

#Content type must be included in the header
header = {
    "Authorization": "Bearer M2RkNzJjNGQtY2UwNS00NGJkLThiOTgtNmQ2Y2VjYzdjMDI0YWY3N2ZjZGEtYzUz",
    "Content-type": "application/json"}

#response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)
responseString= requests.get(url, headers=header)
print("Response code: "+ str(responseString.status_code))

ro=responseString.json()
print(ro["displayName"])

header = {
    "Authorization": "Bearer M2RkNzJjNGQtY2UwNS00NGJkLThiOTgtNmQ2Y2VjYzdjMDI0YWY3N2ZjZGEtYzUz",
    "Content-type": "application/json"}

payload = {
    "roomId":"Y2lzY29zcGFyazovL3VzL1JPT00vYjE4YzJlMjAtY2ZjMS0xMWU1LWJmY2YtZTE4YTBkMzMwYTg1",
    "text":"message from myApp"
}

responseString=requests.post('https://api.ciscospark.com/v1/messages',data=json.dumps(payload),headers=header)

print("POST response:"+str(responseString.status_code))
ro=responseString.json()
print("Created: "+str(ro["created"]))


#floors = jsonObject["Building"]["Floor"]
#for floor in floors:
#	print("Floor Number: " + str(floor["floorNumber"]))
#	aps = floor["AccessPoint"]
#	for ap in aps:
#		print(" " + ap["name"] + "/" + ap["ipAddress"] + "/")


#response.close()

print("<<<end>>>")
