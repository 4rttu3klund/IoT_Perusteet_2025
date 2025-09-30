### Burglary alarm
import machine
import utime

sensor = machine.Pin(28, machine.Pin.IN)

print("Waiting for motion...")

while True:
    if sensor.value() == 1:
        print("Motion detected!")
        utime.sleep(5)