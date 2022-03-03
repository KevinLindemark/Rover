from machine import Pin, PWM
import machine
from time import sleep
from hcsr04 import HCSR04
import _thread
import globalVar

leftSonic = HCSR04(trigger_pin=33, echo_pin=25, echo_timeout_us=10000)
rightSonic = HCSR04(trigger_pin=18, echo_pin=5, echo_timeout_us=10000)

#buzzer
#beeper = PWM(Pin(32), freq=440, duty=0)
#beeper.deinit()

print("init motors")
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
D1_phaseA.value(1)
D1_phaseB = Pin(D1_PHA_B, Pin.OUT)
D1_phaseB.value(1)
D2_phaseA = Pin(D2_PHA_A, Pin.OUT)
D2_phaseA.value(1)
D2_phaseB = Pin(D2_PHA_B, Pin.OUT)
D2_phaseB.value(1)

frequency = 500

#D1_A RIGHT BACK
D1_RB_EN = PWM(Pin(D1_EN_A, Pin.OUT), frequency)

#D1_B RIGHT FRONT
D1_RF_EN = PWM(Pin(D1_EN_B, Pin.OUT), frequency)

#D2_A LEFT FRONT
D2_LF_EN = PWM(Pin(D2_EN_A, Pin.OUT), frequency)

#D2_B LEFT BACK
D2_LB_EN = PWM(Pin(D2_EN_B, Pin.OUT), frequency)

def turnLeft():          
    D1_phaseA.value(1)
    D1_phaseB.value(1)
    D2_phaseA.value(0)
    D2_phaseB.value(0)

    D1_RB_EN.duty(500)
    D1_RF_EN.duty(500)
    D2_LF_EN.duty(500)
    D2_LB_EN.duty(500)
    
def turnRight():
    D1_phaseA.value(0)
    D1_phaseB.value(0)
    D2_phaseA.value(1)
    D2_phaseB.value(1)

    D1_RB_EN.duty(500)
    D1_RF_EN.duty(500)
    D2_LF_EN.duty(500)
    D2_LB_EN.duty(500)

def drive(dutyVal):
    D1_RB_EN.duty(dutyVal)
    D1_RF_EN.duty(dutyVal)
    D2_LF_EN.duty(dutyVal)
    D2_LB_EN.duty(dutyVal)

# set phase on all motors to reverse motor direction
def set_phase(val):
    D1_phaseA.value(val)
    D1_phaseB.value(val)
    D2_phaseA.value(val)
    D2_phaseB.value(val)
    
    #if val == 0:
        #beeper.duty(500)
    #else:
       #beeper.deinit()

def autopilot():
    while True:
      if globalVar.killThread == 1:
          _thread.exit()
          globalVar.killThread = 0
          
      D1_phaseA.value(1)
      D1_phaseB.value(1)
      D2_phaseA.value(1)
      D2_phaseB.value(1)
      
      distLeft = leftSonic.distance_mm()
      distRight = rightSonic.distance_mm()
      # get difference between distances
      a = (distLeft - distRight) * 3.8
      #print(a)
        
      if a > 250:
          print("Too much right")
          if a > 1023:# roll over protection

              print("right motors RO: ",1023)
              
              D1_phaseA.value(1)
              D1_phaseB.value(1)
              D2_phaseA.value(0)
              D2_phaseB.value(0)
              
              D1_RB_EN.duty(500)
              D1_RF_EN.duty(500)
              D2_LF_EN.duty(500)
              D2_LB_EN.duty(500)
              sleep(0.05)
                      
          else:    
              print("right motors: ",a)
              D1_RB_EN.duty(int(a*1))
              D1_RF_EN.duty(int(a*1))
              D2_LF_EN.duty(int(a*0.15))
              D2_LB_EN.duty(int(a*0.15))
           
      if a < -250:
          print("Too much left")
          if a < -1023:# roll over protection
              print("Left motors RO: ",1023)
              
              D1_phaseA.value(0)
              D1_phaseB.value(0)
              D2_phaseA.value(1)
              D2_phaseB.value(1)
              
              D1_RB_EN.duty(500)
              D1_RF_EN.duty(500)
              D2_LF_EN.duty(500)
              D2_LB_EN.duty(500)
              sleep(0.05)
             
              
          else:
              print("Left motors: ",a)
              D1_RB_EN.duty(int(a*0.15))
              D1_RF_EN.duty(int(a*0.15))
              D2_LF_EN.duty(int(a*1))
              D2_LB_EN.duty(int(a*1))
          
      if a > -250 and a < 250:
          print("Middle of the line")
          print("Right and left motors: ",300)
          D1_RB_EN.duty(300)
          D1_RF_EN.duty(300)
          D2_LF_EN.duty(300)
          D2_LB_EN.duty(300)
      #print(a)
      sleep(0.1)
