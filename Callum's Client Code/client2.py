#!usr/bin/env python

# In this risk version of the project, I'm assuming that the servo motors turn anticlockwise as the value increases.

# This is Callum's edition of the client code.
import time
from controller import *
import lib_threading1
import positions as position
import definitions2

# Controls
LEFT_TRG = 2
RIGHT_TRG = 5
RB = 310 # I'm unsure whether this is the actual event code
LB = 311 # I'm unsure whether this is the actual event code
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

# Arm Angles
arm_angles = [200,200,512] # [shoulder, arm twist, hand twist]. Limits of these values are 1023.

# Other Vars
left_wheel_number_instructions = 0
right_wheel_number_instructions = 0 # These two variables are to ensure the robot doesn't take too many processes and lags as a result.
forwardsI = 0
switchONN = True
drivername = input()
left_trigger_direction = 1
right_trigger_direction = 1 # Possible values for LB,RB = 1 (forwards), -1 (backwards) - multipliers for servo speed.

for event in gamepad:
    # Ensuring we have a valid instruction. event.code = 0 and event.value = 0 will fail this condition.
    if event.code != 0 or event.value != 0:
        if event.code == LEFT_TRG:
            # If it is possible to move the left wheels
            left_wheel_number_instructions = 1 if definitions2.leftWheelsMove(event.value,left_trigger_direction,left_wheel_number_instructions) else left_wheel_number_instructions + 1
        elif event.code == RIGHT_TRG:
            # Move the right wheels
            right_wheel_number_instructions = 1 if definitions2.rightWheelsMove(event.value,right_trigger_direction,left_wheel_number_instructions) else right_wheel_number_instructions + 1
        elif event.code == LB:
            left_trigger_direction = definitions2.bumperChangeDirection(event.value,left_trigger_direction)
        elif event.code == RB:
            right_trigger_direction = definitions2.bumperChangeDirection(event.value,right_trigger_direction)
        elif event.code == A:
            position.slam(input()) # We need to get the password ;)
            
        
        
