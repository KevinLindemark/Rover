import machine
from time import sleep
import globalVar
servoPin1 = machine.Pin(23) # rotate
servoPin2 = machine.Pin(22) # forward
servoPin3 = machine.Pin(21) # grab
servoPin4 = machine.Pin(19) # updown
rotation = machine.PWM(servoPin1,freq=50)
forwardbackward = machine.PWM(servoPin2,freq=50)
grab = machine.PWM(servoPin3,freq=50)
updown = machine.PWM(servoPin4,freq=50)

# Servo duty ranges
upMax = 70
downMax = 90
leftMax = 120
rightMax = 20
grabOpenMax = 40
grabDropMax = 120
forwardMin = 75
forwardMax = 120

def rotate_Right():
    if globalVar.rotate <= rightMax + 5:
        globalVar.rotate = rightMax
        rotation.duty(rightMax)
    else:
        globalVar.rotate = globalVar.rotate - 5
        rotation.duty(globalVar.rotate)
    print(globalVar.rotate)
 
def rotate_Left():
    if globalVar.rotate >= leftMax - 5:
        globalVar.rotate = leftMax
        rotation.duty(leftMax)
    else:
        globalVar.rotate = globalVar.rotate + 5
        rotation.duty(globalVar.rotate)
    print(globalVar.rotate)
    
def up():
    if globalVar.upAndDown <= upMax + 5:
        globalVar.upAndDown = upMax
        updown.duty(upMax)
    else:
        globalVar.upAndDown = globalVar.upAndDown - 5
        updown.duty(globalVar.upAndDown)
    print("Servo up", globalVar.upAndDown)
    
def down():
    if globalVar.upAndDown >= downMax - 5:
        globalVar.upAndDown = downMax
        updown.duty(downMax)
    else:
        globalVar.upAndDown = globalVar.upAndDown + 5
        updown.duty(globalVar.upAndDown)
    print("Servo down", globalVar.upAndDown)
    
def forward():
    if globalVar.forwardAndBackward >= forwardMax - 5:
        globalVar.forwardAndBackward = forwardMax
        forwardbackward.duty(forwardMax)
    else:
        globalVar.forwardAndBackward = globalVar.forwardAndBackward + 5
        forwardbackward.duty(globalVar.forwardAndBackward)
    print(globalVar.forwardAndBackward)
    
def backward():
    if globalVar.forwardAndBackward <= forwardMin + 5:
        globalVar.forwardAndBackward = forwardMin
        forwardbackward.duty(forwardMin)
    else:
        globalVar.forwardAndBackward = globalVar.forwardAndBackward - 5
        forwardbackward.duty(globalVar.forwardAndBackward)
    print(globalVar.forwardAndBackward)
    
class ServoControl:
    def __init__(self, rotate, forward, grab, updown):
        self.rotate = rotate
        self.forward = forward
        self.grab = grab
        self.updown = updown
       
    # function to set value of rotate
    def set_leftRight(self, servoRotateVal):
        self.rotate +=servoRotateVal
        print(f"servoRotateVal setter method called with val {servoRotateVal}")
        if self.rotate <= leftMax:
            self.rotate = leftMax
            rotation.duty(leftMax)
        else:
            rotation.duty(self.rotate)
        if self.rotate >= rightMax:
            self.rotate = rightMax
            rotation.duty(rightMax) 
        else:
            rotation.duty(self.rotate) 
    # function to set value of forward
    def set_forwardBackward(self, servoForwardBackwardVal):
        self.forward = servoForwardBackwardVal
        print(f"servoForwardBackwardVal setter method called with val {servoForwardBackwardVal}")
        forward.duty(self.forward)
    # function to set value of grab
    def set_ServoGrab(self, ServoGrabVal):
        self.grab = ServoGrabVal
        print(f"servoGrab setter method called with val {ServoGrabVal}")
        grab.duty(self.grab)
    # function to set value of grab
    def set_UpDown(self, ServoUpDownVal):
        self.updown = ServoUpDownVal
        print(f"servoGrab setter method called with val {ServoUpDownVal}")   
        updown.duty(self.updown)
