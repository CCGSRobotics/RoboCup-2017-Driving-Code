from connect import *
print("definitions setup")
def LWheels(speed):
    negative = False
    speed = int(speed)
    if (speed > 10 and speed < 999) or (speed < -10 and speed > -999):
        if speed < -10:
            speed *= -1
            negative = True
        while len(str(speed)) < 4:
            speed = "0" + str(speed)
        if negative:
            negative = False
            speed = "-" + speed
        sock.sendall(bytes("1" + str(speed) + "\n", "utf-8"))
        sock.sendall(bytes("3" + str(speed) + "\n", "utf-8"))
    elif speed == 0:
        sock.sendall(bytes("30000\n", "utf-8"))
        sock.sendall(bytes("10000\n", "utf-8"))
        
def RWheels(speed):
    negative = False
    speed = int(speed)
    if (speed > 10 and speed < 999)or (speed < -10 and speed > -999):
        if speed < -10:
            speed *= -1
            negative = True
        while len(str(speed)) < 3:
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
def moveJoint(ID, position, speed):
    position = int(position)
    speed = int(speed)
    while len(str(speed)) < 4:
        speed = "0" + str(speed)
    while len(str(position)) < 4:
        position = "0" + str(position)
    sock.sendall(bytes(str(ID) + str(position) + str(speed) + "\n", "utf-8"))
def SwitchON():
   sock.sendall(bytes("ON\n", "utf-8"))
def SwitchOFF():
    sock.sendall(bytes("OFF\n", "utf-8"))


print("definitions made")
