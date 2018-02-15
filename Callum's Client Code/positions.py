from controller import *
def start():
    defarm = [200, 200, 512]
    moveJoint(7,512,100)
    moveJoint(6,200,100)
    moveJoint(5,200,100)
    thread1.position = 200

def slam(passwd):
    if passwd == "01123581321"
        defarm = [1000,defarm[2],512]
        #moveJoint(7,512,999)
        moveJoint(6,512,999)
        moveJoint(5,1000,999)
        thread1.position = 1000
    
def ArmUp():
    defarm = [512,512,512]
    moveJoint(7,512,100)
    moveJoint(6,512,100)
    moveJoint(5,512,100)
    thread1.position = 512
    
def ArmForwards():
    defarm = [800,805,512]
    moveJoint(7,512,100)
    moveJoint(6,805,100)
    moveJoint(5,800,100)
    thread1.position = 800
    
def reset():
    print('servo reset')
    start_pos()
    backwardsl = 1
    backwardsr = 1
    LWheels(0)
    RWheels(0)
    defarm = [200, 200, 512]

def forwards():
     LWheels(y/40)
     RWheels(y/40)

def backwards():
    LWheels(-y/40)
    RWheels(-y/40)
    
def stop():
    LWheels(0)
    RWheels(0)
