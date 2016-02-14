
import requests
from urllib.request import Request, urlopen
import json
import time


print("<<<start>>>")

myroomid = "Y2lzY29zcGFyazovL3VzL1JPT00vYjE4YzJlMjAtY2ZjMS0xMWU1LWJmY2YtZTE4YTBkMzMwYTg1"
header = {
    "Authorization": "Bearer M2RkNzJjNGQtY2UwNS00NGJkLThiOTgtNmQ2Y2VjYzdjMDI0YWY3N2ZjZGEtYzUz",
    "Content-type": "application/json"}

#url = 'https://api.ciscospark.com/v1/people/me'

#response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)
#responseString= requests.get(url, headers=header)
#print("Response code: "+ str(responseString.status_code))

#ro=responseString.json()
#print(ro["displayName"])

#imageURL = "http://hamble.net/WP/wp-content/uploads/2012/05/airhamble2.jpg"
#localtime = time.asctime( time.localtime(time.time()) )
#messsageText = str(localtime) + "> New Message"
#payload = {
#    "roomId":myroomid,
#    "text": messsageText,
#    "files":[imageURL]
#}

#responseString=requests.post('https://api.ciscospark.com/v1/messages',data=json.dumps(payload),headers=header)


requestURL="https://api.ciscospark.com/v1/messages"+"?"+"roomId="+str(myroomid)+"&"+"max=1"

#print(requestURL)
responseString=requests.get(requestURL,headers=header)

print("POST response:"+str(responseString.status_code))
ro=responseString.json()

#msgdetails = json.loads(responseString)
print(ro)
#print(ro["text"])

#print("Message: "+ msgdetails["text"])


#floors = jsonObject["Building"]["Floor"]
#for floor in floors:
#	print("Floor Number: " + str(floor["floorNumber"]))
#	aps = floor["AccessPoint"]
#	for ap in aps:
#		print(" " + ap["name"] + "/" + ap["ipAddress"] + "/")


#response.close()

print("<<<end>>>")
