#from connect import *
print("definitions setup")
def LWheels(speed):
    negative = False
    speed = int(speed)

    # I don't understand this condition here. Why are you excluding -10,9,...,-1,1,...,9,10?
    if (speed > 10 and speed < 999) or (speed < -10 and speed > -999):
        if speed < -10:
            speed *= -1
            negative = True
            
        while len(str(speed)) < 4:
            speed = "0" + str(speed) # Are you trying to add a '0' to the beginning of the speed?
            
        if negative:
            negative = False
            speed = "-" + speed
        #sock.sendall(bytes("1" + str(speed) + "\n", "utf-8"))
        #sock.sendall(bytes("3" + str(speed) + "\n", "utf-8"))
        return bytes("1" + str(speed),"utf-8"),bytes("3" + str(speed),"utf-8")
    elif speed == 0:
        #sock.sendall(bytes("30000\n", "utf-8"))
        #sock.sendall(bytes("10000\n", "utf-8"))
        return bytes("30000\n","utf-8"),bytes("10000\n","utf-8")

# From what I can see, you cannot get the input as an integer.
# The left and right wheels are already pretty optimised, so there wasn't really much I could do.
def CallumLeftWheels(speed):
    r1 = 10000
    r2 = 30000
    speed = int(speed)

    # This line should kill the program if the speed has more than 4 digits.
    assert speed > -10000 and speed < 10000
    
    if speed > -1:
        r1 += speed
        r2 += speed
        r1 = str(r1)
        r2 = str(r2)
    else:
        r1 = "1-"
        r2 = "3-"
        speed = str(speed)
        
        for i in range(4-(len(speed)-1)):
            r1 += "0"
            r2 += "0"
            
        r1 += str(abs(int(speed)))
        r2 += str(abs(int(speed)))
        
    sock.sendall(bytes(r1 + "\n", "utf-8"))
    sock.sendall(bytes(r2 + "\n", "utf-8"))

def CallumRightWheels(speed):
    r1 = 20000
    r2 = 40000
    speed = int(speed)

    # This line should kill the program if the speed has more than 4 digits.
    assert speed > -10000 and speed < 10000
    
    if speed > -1:
        r1 += speed
        r2 += speed
        r1 = str(r1)
        r2 = str(r2)
    else:
        r1 = "2-"
        r2 = "4-"
        speed = str(speed)
        
        for i in range(4-(len(speed)-1)):
            r1 += "0"
            r2 += "0"
            
        r1 += str(abs(int(speed)))
        r2 += str(abs(int(speed)))
        
    sock.sendall(bytes(r1 + "\n", "utf-8"))
    sock.sendall(bytes(r2 + "\n", "utf-8"))
    
def RWheels(speed):
    negative = False
    speed = int(speed)
    if (speed > 10 and speed < 999) or (speed < -10 and speed > -999):
        if speed < -10:
            speed *= -1
            negative = True
        while len(str(speed)) < 3: # Why 3 this time?
            speed = "0" + str(speed)
        speed = str(speed)
        if negative:
            negative = False
            speed = "-" + speed
        sock.sendall(bytes("2" + str(speed) + "\n", "utf-8"))
        sock.sendall(bytes("4" + str(speed) + "\n", "utf-8"))
    elif speed == 0:
        sock.sendall(bytes("40000\n", "utf-8"))
        sock.sendall(bytes("20000\n", "utf-8"))

# This function was also well done, so there really wasn't much I could do.
def moveJoint(ID, position, speed):
    position = int(position)
    speed = int(speed)
    
    while len(str(speed)) < 4:
        speed = "0" + str(speed)
        
    while len(str(position)) < 4:
        position = "0" + str(position)
        
    sock.sendall(bytes(str(ID) + str(position) + str(speed) + "\n", "utf-8"))

def CallumMoveJoint(ID, position, speed):
    #position = int(position)
    #speed = int(speed) These should already be strings right?
    
    while len(speed) < 4:
        speed = "0" + speed
        
    while len(position) < 4:
        position = "0" + position
        
    sock.sendall(bytes(ID + position + speed + "\n", "utf-8"))
    
def SwitchON():
   sock.sendall(bytes("ON\n", "utf-8"))
   
def SwitchOFF():
    sock.sendall(bytes("OFF\n", "utf-8"))


print("definitions made")
