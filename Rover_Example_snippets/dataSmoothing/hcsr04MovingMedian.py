from hcsr04 import HCSR04
import machine
from time import sleep
from random import randrange
import statistics

sensor1 = HCSR04(trigger_pin=33, echo_pin=25, echo_timeout_us=10000)
sensor2 = HCSR04(trigger_pin=18, echo_pin=5, echo_timeout_us=10000)

sensor1DistList = [0,0,0,0,0,0,0,0,0,0]
sensor1OldDist = 0

sensor2DistList = [0,0,0,0,0,0,0,0,0,0]
sensor2OldDist = 0

while True:
    try:
        #print("Sensor1 cm:", sensor1.distance_cm(), "Sensor2 cm:", sensor2.distance_cm())
        sleep(0.1)
        
        #Get distance in CM from sensor1 and sensor2
        dist1 = sensor1.distance_cm()
        dist2 = sensor2.distance_cm()
        
        # remove first item in sensor1DistList and add the newest reading to the end
        sensor1DistList.pop(0)
        sensor1DistList.append(dist1)
        print(sensor1DistList)
        
        # remove first item in sensor2DistList and add the newest reading to the end
        sensor2DistList.pop(0)
        sensor2DistList.append(dist2)
        #print(sensor2DistList)
        
        # Printing median of sensor1DistList and sensor3DistList
        if statistics.median(sensor1DistList) > 0 and statistics.median(sensor1DistList) < 400 or statistics.median(sensor2DistList) > 0 and statistics.median(sensor2DistList) < 400:
            print("Median of sensor1DistList is : % s " % (statistics.median(sensor1DistList)), "Median of sensor2DistList is : % s " % (statistics.median(sensor2DistList)))
        else:
            print("Out of range")
            
    except KeyboardInterrupt:
        print("Ctrl-C")
        machine.reset()

