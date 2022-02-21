from machine import Pin, PWM
from time import sleep
D1_STBY = 4
D1_EN_A = 16
D1_EN_B = 15
D1_PHA_A = 17
D1_PHA_B = 0

D2_STBY = 14
D2_EN_A = 12
D2_EN_B = 26
D2_PHA_A = 13
D2_PHA_B = 27

d1 = Pin(D1_STBY, Pin.OUT)
d1.value(1)

d2 = Pin(D2_STBY, Pin.OUT)
d2.value(1)

D1_phaseA = Pin(D1_PHA_A, Pin.OUT)
D1_phaseA.value(0)
D1_phaseB = Pin(D1_PHA_B, Pin.OUT)
D1_phaseB.value(0)
D2_phaseA = Pin(D2_PHA_A, Pin.OUT)
D2_phaseA.value(0)
D2_phaseB = Pin(D2_PHA_B, Pin.OUT)
D2_phaseB.value(0)

frequency = 5000
#D1_A RIGHT BACK
D1_enableA = Pin(D1_EN_A, Pin.OUT)
D1_enableA.value(1)
#D1_enableA = PWM(Pin(D1_EN_A, Pin.OUT), frequency)

#D1_B RIGHT FRONT
D1_enableB = Pin(D1_EN_B, Pin.OUT)
D1_enableB.value(1)
#D1_enableB = PWM(Pin(D1_EN_B, Pin.OUT), frequency)

#D2_A LEFT FRONT
D2_enableA = Pin(D2_EN_A, Pin.OUT)
D2_enableA.value(1)
#D2_enableA = PWM(Pin(D2_EN_A, Pin.OUT), frequency)

#D2_B LEFT BACK
D2_enableB = Pin(D2_EN_B, Pin.OUT)
D2_enableB.value(1)
#D2_enableB = PWM(Pin(D2_EN_B, Pin.OUT), frequency)

"""
while True: 
    for i in range(0, 1023):
        D1_enableB.duty(i)
        D1_enableA.duty(i)
        D2_enableB.duty(i)
        D2_enableA.duty(i)
        sleep(0.01)
        print(f"Duty{i}")
"""