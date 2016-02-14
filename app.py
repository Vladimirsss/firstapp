
import requests
from urllib.request import Request, urlopen
import json


print("this is first app")
# put the ip address or dns of your apic-em controller in this url
url = 'https://api.ciscospark.com/v1/people/me'

#the username and password to access the APIC-EM Controller
#payload = {"username":"admin","password":"C!sc0123"}
payload = {}

#Content type must be included in the header
header = {
    "Authorization": "Bearer M2RkNzJjNGQtY2UwNS00NGJkLThiOTgtNmQ2Y2VjYzdjMDI0YWY3N2ZjZGEtYzUz",
    "Content-type": "application/json"}

print (header)
#Performs a POST on the specified url.
#response= requests.get(url,data=json.dumps(payload), headers=header, verify=False)
responseString= requests.get(url, headers=header)

# print the json that is returned
print("Response code: "+ str(responseString.status_code))

print(responseString.json())


#req = Request('https://msesandbox.cisco.com/api/contextaware/v1/maps/info/DevNetCampus/DevNetBuilding')
#req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc==')
#req.add_header('Accept', 'application/json')
#response = urlopen(req)

#responseString = response.read().decode("utf-8")

#jsonObject = json.loads(responseObject)

#print(jsonObject["displayName"])

#floors = jsonObject["Building"]["Floor"]
#for floor in floors:
#	print("Floor Number: " + str(floor["floorNumber"]))
#	aps = floor["AccessPoint"]
#	for ap in aps:
#		print(" " + ap["name"] + "/" + ap["ipAddress"] + "/")


#response.close()

print("<<<end>>>")
