# Rover
Micropython Rover with ESP32

The motorTestPWM folder contains a working motor test for the rover. It will continuesly run all motors from low duty (300) to max duty (1023), and then stop all motors for 3 seconds and repeat. 


The dataSmoothing folder contains an example of how to setup moving median for smoothing of sensordata (Remove outliers). Upload all 3 files to ESP32 and run the 
hcsr04MovingMedian.py file. The example needs hcsr04 sensors attatched.


