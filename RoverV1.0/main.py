from time import sleep
import sys
import webserver
import motorFunctions
from machine import Pin, PWM
import servo
import _thread
import globalVar

# stop all motors at startup 
motorFunctions.drive(0)

driveSpeed = 200


print("locked and loaded")
while True:
  try:
    while False:
        print("alive")
        sleep(2)
    conn, addr = webserver.s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    #print('Content = %s' % request)
    speed = request.find('/?speed=faster')
    backwardsDrive = request.find('/?backwardsDrive=drivebackwards')
    left = request.find('/?left=turnLeft')
    right = request.find('/?right=turnRight')
    stop = request.find('/?stop=stopNow')
    autoStart = request.find('/?autoStart=autoOn')
    autoStop = request.find('/?autoStop=autoOff')
    servoRight = request.find('/?servoRight=right')
    servoLeft = request.find('/?servoLeft=left')
    servoUp = request.find('/?servoUp=up')
    servoDown = request.find('/?servoDown=down')
    servoForward = request.find('/?servoForward=forward')
    servoBackward = request.find('/?servoBackward=backward')
    grabOpen = request.find('/?grabOpen=open')
    grabClose = request.find('/?grabClose=close')
    
    if servoLeft ==6:
      print("SERVO LEFT!")
      servo.rotate_Left()
    if servoRight ==6: 
      print("SERVO RIGHT!")
      servo.rotate_Right()
    if servoUp == 6:
      print("SERVO UP!")
      servo.up()
    if servoDown == 6:
      print("SERVO DOWN!")
      servo.down()
    if grabOpen == 6:
      print("GRAB OPEN!")
      servo.grab.duty(servo.grabOpenMax)
    if grabClose == 6:
      print("GRAB CLOSE!")
      servo.grab.duty(servo.grabDropMax)
    if servoForward == 6:
      print("SERVO FORWARD!")
      servo.forward()
    
    if servoBackward == 6:
      print("SERVO BARCKWARD!")
      servo.backward()
    
    if autoStart == 6: #start autopilot
      print("autopilot on")
      globalVar.killThread = 0
      _thread.start_new_thread(motorFunctions.autopilot,())
           
    if autoStop == 6: #stop autopilot
      print("autopilot off")
      globalVar.killThread = 1
      motorFunctions.drive(0)
    
    if speed == 6:
      motorFunctions.set_phase(1)
      driveSpeed = driveSpeed + 100
      print('FASTER')
      
      if driveSpeed >= 900:
        motorFunctions.drive(1023)
        print("MAX SPEED")
      else:    
        motorFunctions.drive(driveSpeed)
        print("motor speed: ", driveSpeed)

    if backwardsDrive == 6:
      motorFunctions.set_phase(0)
      driveSpeed = driveSpeed + 100
      print('FASTER')
      
      if driveSpeed >= 900:
        motorFunctions.drive(1023)
        print("MAX SPEED")
      else:    
        motorFunctions.drive(driveSpeed)
        print("motor speed: ", driveSpeed)

    if right == 6:
      print("TURN RIGHT")
      motorFunctions.turnRight() 
    if left == 6:
      print("TURN LEFT")
      motorFunctions.turnLeft() 
      
    if stop == 6:
      print("STOP!")
      motorFunctions.drive(0)
      driveSpeed = 200 # reset initial drive speed

    response = webserver.web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()     
    
  except KeyboardInterrupt:
      print("Ctrl + C pressed!")
      motorFunctions.drive(0)
      sys.exit()
