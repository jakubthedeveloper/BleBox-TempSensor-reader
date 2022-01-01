import requests
import json

tempSensorIpAddress = "192.168.1.139" # Change to an IP address of your bleBox tempSensor
url = "http://" + tempSensorIpAddress + "/state"
resp = requests.get(url)

if resp.status_code != 200:
  print("Invalid status: " + str(resp.status_code))
  quit()

data = json.loads(resp.content)

sensors = data.get('tempSensor')

for sensorKey in sensors:
  for sensor in sensors[sensorKey]:
    for key in sensor:
      print(key + ": " + str(sensor.get(key)))
    print("-----")
