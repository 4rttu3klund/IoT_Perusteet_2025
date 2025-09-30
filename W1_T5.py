### Weather station
import machine
import time
import dht

sensor = dht.DHT22(machine.Pin(15))

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temperature: {:.1f}°C".format(temp))
        print("Humidity: {:.1f}%".format(hum))
    except OSError as e:
        print("Sensor error:", e)
    time.sleep(2) 