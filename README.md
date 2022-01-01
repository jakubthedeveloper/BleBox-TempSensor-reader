# BleBox-TempSensor-reader
Reads and prints information from [BleBox TempSensor](https://blebox.eu/produkt/tempsensor/)

## Configuration
Set tempSensor IP address in main.py, variable `tempSensorIpAddress`.

## Usage
```bash
python3 main.py
```

## Example output
```
------------
|  Device  |
------------
deviceName: My tempSensor
type: tempSensor
product: tempSensor
hv: 1.1
fv: 0.1016
universe: 0
apiLevel: 20210118
id: fa21bb5ad246
ip: 192.168.1.139
availableFv: None

  ---------------
  |  Sensor #1  |
  ---------------
  type: temperature
  id: 0
  value: 51.68°
  trend: ➚
  state: Active data
  elapsedTimeS: 1
```
