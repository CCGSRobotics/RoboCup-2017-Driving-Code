#!/usr/bin/env python
import time
from controller import *
import positions as position
#from connect import *
print("controller ready")

# def arm not de farm
defarm = [200, 200, 512]
# [Shoulder, armTwist, handTwist]

Left_wheel_read_controls = 0
Right_wheel_read_controls = 0
ForwardsI = 0
SwitchONN = True
drivername = str(input())
change_left_trigger_direction = 1
change_right_trigger_direction  = 1 # Possible values for LB,RB = 1,-1, multipliers for servos speed.

# Controls
LEFT_TRG = 2
RIGHT_TRG = 5
R1 = 310
L1 = 311
LCLICK = 317
RCLICK = 318
RVERT = 4
RHORIZ = 3
LVERT = 1
LHORIZ = 0
START = 315
A = 304
B = 305
Y = 308
X = 307


from lib_threading1 import * # Place this line at the top.

print("Vroom Vroom!")
for event in gamepad.read_loop():
    try:
        x = event.code
        y = event.value
        z = event.type
        if x != 0:
            #print(x,y,z)
            #pass
        
            if x == LEFT_TRG:
                # Function to move the left wheel
                if Left_wheel_read_controls == 3 or y <= 0:
                    if y > 0:
                        LWheels(y*4*backwardsl) # backwardsl? Shouldn't it be "left_trigger_direction"?
                    else:
                        LWheels(0)
                    Left_wheel_read_controls = 1
                else:
                    Left_wheel_read_controls = Left_wheel_read_controls + 1
            elif x == RIGHT_TRG:
                # Move the right wheels
                if Right_wheel_read_controls == 3 or y <= 0:
                    if y > 0:
                        RWheels(-(y*4*change_right_trigger_direction ))
                    else:
                        RWheels(0)
                    Right_wheel_read_controls = 1
                else:
                    Right_wheel_read_controls = Right_wheel_read_controls + 1    
            elif x == LB:
                # Possible mistake - Need to confirm if these are the right buttons.
                if y == 1:
                    if change_right_trigger_direction> 0:
                        change_right_trigger_direction= -1
                    else:
                        change_right_trigger_direction= 1
            elif x == RB:
                # Same Here
                if y == 1:
                    if change_right_trigger_direction  > 0:
                        change_right_trigger_direction  = -1
                    else:
                        change_right_trigger_direction  = 1
            elif x == LHORIZ:
                if ForwardsI == 3 or y <= 0:
                    if y != 0:
                        forwards()
                    else:
                        stop()
                    ForwardsI = 1
                    
                else:
                    ForwardsI = ForwardsI + 1  
                    
                
            elif x == LVERT:
                # Move the robot forward
                y = event.value
                if y > 0:
                    LWheels(-(y/40))
                    RWheels((y/40))
                else:
                    LWheels(-(y/40))
                    RWheels((y/40))
                    
            elif x == RHORIZ:
                # Move the joint
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
            elif x == RVERT:
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
                # Arm movement
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
                ArmUp()
            elif x == 308:
                ArmForwards()
            elif x == 304:
                if alf == "seb":
                    # Boost the machine forward some distance at the expense of the physical state of the robot.
                    # Maybe we should set another password for this incase will shiet happens.
                    position.slam()
            elif x == 315:
                # Reset the position of the robot.
                reset()
            elif x == 314:
                # Stop the program
                print('quitting')
                break
            elif x == 305:
                if SwitchONN and y != 0:
                    SwitchOFF()
                    SwitchONN = False
                    print("OFF")
                elif y != 0:
                    SwitchON()
                    SwitchONN = True
                    print("ON")
                
                try:
                    print('trying')
                    if CWorking and y == 1:
                        if camerasrt:
                            stopcam()
                            camerasrt = False
                        else:
                            startcam()
                            camerasrt = True
                except:
                    if y == 1:
                        pass
                        print("Du bist ein Dummkopf!") # Tristan said to keep this. It translates to "You are a idiot"
                        print("PUTAIN!")
            else:
                print(x)
                #pass
    # When the Robot somehow runs into a problem and disconnects from the server (running computer)
    except BrokenPipeError as e:
        print(e)

thread1.direction = ""
