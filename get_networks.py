import requests
import json

jsonfile = "networks.json"

urlbegin = "https://api.meraki.com/api/v0/organizations/"
orgid = "630040"
urlend = "/networks"

url = urlbegin + orgid + urlend

headers = {
    "X-Cisco-Meraki-API-Key" : "994fdf310fd5e9d2c3c738b1b0d0de8b29c8827a"
}
r = requests.get(url = url, headers=headers)
data = r.json()

dataArray = "networks = ["+str(data)+"]"

print(data)

#with open(jsonfile, "w", encoding="utf-8") as outfile:
#    json.dump(data, outfile,ensure_ascii=False)
    
f = open(jsonfile, "w")    
f.write("networks ="+str(data))