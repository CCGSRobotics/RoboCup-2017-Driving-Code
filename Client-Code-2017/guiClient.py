#!/usr/bin/env python
import time
# import sys

def start_pos():
    defarm = [200, 200, 512]
    moveJoint(7,512,100)
    moveJoint(6,200,100)
    moveJoint(5,200,100)
    thread1.position = 200

defarm = [200, 200, 512]

# Create a socket(SOCK_STREAM means a TCP socket)

from lib_threading1 import *


def forward():
    LWheels(200/40)
    RWheels(200/40)

def backward():
    LWheels(-(200/40))
    RWheels((200/40))

def rForward():
    if defarm[2] - (100/4000) > 0:
        defarm[2] -= 100/4000
        moveJoint(7,defarm[2],999)
    else:
        defarm[2] = 0
        moveJoint(7,0,100)

def rBackward():
    if defarm[1] + 5 < 800:
        defarm[1] += 5
        moveJoint(6,defarm[1],999)
    else:
        defarm[1] = 800
        moveJoint(6,800,100)

def R1():
    RWheels(400)

def L1():
    LWheels(-400)

def R2():
    RWheels(-(100*4))

def L2():
    LWheels(100*4)

def A():
    defarm = [1000,512,512]
    moveJoint(7,512,100)
    moveJoint(6,512,100)
    moveJoint(5,1000,100)
    thread1.position = 1000

def X():
    defarm = [512,512,512]
    moveJoint(7,512,100)
    moveJoint(6,512,100)
    moveJoint(5,512,100)
    thread1.position = 512

def Y():
    defarm = [800,805,512]
    moveJoint(7,512,100)
    moveJoint(6,805,100)
    moveJoint(5,800,100)
    thread1.position = 800

def B():
    if CWorking:
        if camerasrt:
            stopcam()
            camerasrt = False
        else:
            startcam()
            camerasrt = True

def restart():
    start_pos()
    LWheels(0)
    RWheels(0)
    defarm = [200, 200, 512]
