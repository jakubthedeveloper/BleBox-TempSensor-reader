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
      value = sensor.get(key)
      if key == "trend":
        if value == 0:
          value = "No data"
        elif value == 1:
          value = "➙"
        elif value == 2:
          value = " ➘"
        elif value == 3:
          value = "➚"      
      elif sensor.get("type") == "temperature" and key == "value":
        value = str(value / 100) + "°"
      elif key == "state":
        if value == 1:
          value = "Measurement in progress"
        elif value == 2:
          value = "Active data"
        elif value == 3:
          value = "Error"
        else:
          value = "Unknown"
      else:      
        value = str(value)
      
      print("  " + key + ": " + value)
    print("")
  sensorNumber += 1

