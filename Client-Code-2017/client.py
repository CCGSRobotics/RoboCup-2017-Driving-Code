#!/usr/bin/env python
import time
from controller import *
#from connect import *
print("controller ready")
def start_pos():
    defarm = [200, 200, 512]
    moveJoint(7,512,100)
    moveJoint(6,200,100)
    moveJoint(5,200,100)
    thread1.position = 200

defarm = [200, 200, 512]

Li = 0
Ri = 0
ForwardsI = 0

SwitchONN = True
alf = ""
backwardsl = 1
backwardsr = 1

from lib_threading1 import *
print("Vroom Vroom!")
for event in gamepad.read_loop():
    try:
        x = event.code
        y = event.value
        z = event.type
        if x != 0 or y != 0:
            print(x,y,z)
            pass
        
            if x == 2:
                if Li == 3 or y <= 0:
                    if y > 0:
                        LWheels(y*4*backwardsl)
                    else:
                        LWheels(0)
                    Li = 1
                else:
                    Li = Li + 1
            elif x == 5:
                if Ri == 3 or y <= 0:
                    if y > 0:
                        RWheels(-(y*4*backwardsr))
                    else:
                        RWheels(0)
                    Ri = 1
                else:
                    Ri = Ri + 1    
            elif x == 310:
                if y == 1:
                    if backwardsl > 0:
                        backwardsl = -1
                    else:
                        backwardsl = 1
            elif x == 311:
                if y == 1:
                    if backwardsr > 0:
                        backwardsr = -1
                    else:
                        backwardsr = 1
            elif x == 0:
                
                if ForwardsI == 3 or y <= 0:
                    if y > 0:
                        LWheels(y/40)
                        RWheels(y/40)
                    elif y < 0:
                        LWheels(y/40)
                        RWheels(y/40)
                    
                    else:
                        LWheels(0)
                        RWheels(0)
                    ForwardsI = 1
                else:
                    ForwardsI = ForwardsI + 1  
                    
                
            elif x == 1:
                y = event.value
                if y > 0:
                    LWheels(-(y/40))
                    RWheels((y/40))
                else:
                    LWheels(-(y/40))
                    RWheels((y/40))
                    
            elif x == 3:
                y = event.value
                if y > 0:
                    if defarm[2] - (y/4000) > 0:
                       defarm[2] -= y/4000 
                       moveJoint(7,defarm[2],999)
                    else:
                       defarm[2] = 0
                       moveJoint(7,0,100)
                else:
                    if defarm[2] - (y/4000) < 1100:
                       defarm[2] -= y/4000 
                       moveJoint(7,defarm[2],999)
                    else:
                       defarm[2] = 1100
                       moveJoint(7,1100,100)
            elif x == 4:
                if y > 0:
                    if defarm[1] + 5 < 800:
                       defarm[1] += 5
                       moveJoint(6,defarm[1],999)
                    else:
                       defarm[1] = 800
                       moveJoint(6,800,100)
                else:
                    if defarm[1] - 5 > 200:
                       defarm[1] -= 5
                       moveJoint(6,defarm[1],999)
                    else:
                       defarm[1] = 200
                       moveJoint(6,200,100)
            elif x == 318:
                if y == 1:
                    thread1.direction = "decrease"
                else:
                   thread1.direction = "neutral"
            elif x == 317:
                if y == 1:
                        thread1.direction = "increase"
                else:
                        thread1.direction = "neutral"
            elif x == 307:
                defarm = [512,512,512]
                moveJoint(7,512,100)
                moveJoint(6,512,100)
                moveJoint(5,512,100)
                thread1.position = 512
            elif x == 308:
                defarm = [800,805,512]
                moveJoint(7,512,100)
                moveJoint(6,805,100)
                moveJoint(5,800,100)
                thread1.position = 800
            elif x == 304:
                if alf == "seb":
                    defarm = [1000,defarm[2],512]
                    #moveJoint(7,512,999)
                    moveJoint(6,512,999)
                    moveJoint(5,1000,999)
                    thread1.position = 1000
                pass
            elif x == 315:
                print('servo reset')
                start_pos()
                backwardsl = 1
                backwardsr = 1
                LWheels(0)
                RWheels(0)
                defarm = [200, 200, 512]
            elif x == 314:
                print('quitting')
                break
            elif x ==305:
                if SwitchONN and y != 0:
                    SwitchOFF()
                    SwitchONN = False
                    print("OFF")
                elif y != 0:
                    SwitchON()
                    SwitchONN = True
                    print("ON")
               # if y == 1:
                    #if simpletrack.direction != "running":
                     #   simpletrack.direction = "running"
                    #else:
                     #   simpletrack.direction = "asdfg"
                
                try:
                    print('trying')
                    if CWorking:
                        if y == 1:
                            if camerasrt:
                                stopcam()
                                camerasrt = False
                            else:
                                startcam()
                                camerasrt = True
                except:
                    if y == 1:
                        pass
                        print("Du bist ein Dummkopf!") # Tristan said to keep this. It means "You are a idiot"
                    else:
                        pass
            else:
                print(x)
                #pass
    except BrokenPipeError as e:
        print(e)

thread1.direction = ""
