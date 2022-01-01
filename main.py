import requests
import json

tempSensorIpAddress = "192.168.1.139" # Change to an IP address of your bleBox tempSensor

# Get device info

url = "http://" + tempSensorIpAddress + "/api/device/state"
resp = requests.get(url)

if resp.status_code != 200:
  print("Invalid status: " + str(resp.status_code))
  quit()
  

data = json.loads(resp.content)

device = data.get('device')

print("------------")
print("|  Device  |")
print("------------")

for key in device:
  print(key + ": " + str(device.get(key)))
print("")

# Get sensors from the device  
  
url = "http://" + tempSensorIpAddress + "/state"
resp = requests.get(url)

if resp.status_code != 200:
  print("Invalid status: " + str(resp.status_code))
  quit()

data = json.loads(resp.content)

sensors = data.get('tempSensor')

sensorNumber = 1
for sensorKey in sensors:
  label = "|  Sensor #" + str(sensorNumber) + "  |"
  print("  " + "-" * len(label))
  print("  " + label)
  print("  " + "-" * len(label))

  for sensor in sensors[sensorKey]:
    for key in sensor:
      print("  " + key + ": " + str(sensor.get(key)))
    print("")
  sensorNumber += 1
