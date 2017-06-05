import socketserver
import sys
from emuBot import *

topLeftServo = 4 # 4 
topRightServo = 2 # 2 
bottomLeftServo = 5 # 3
bottomRightServo = 1 # 1

def RWheels(speed):
    moveWheel(bottomRightServo,int(speed))
    moveWheel(topRightServo,int(speed))

def LWheels(speed):
    moveWheel(bottomLeftServo,int(speed))
    moveWheel(topLeftServo,int(speed))

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        i = 1
        
        defarm = [200, 200, 512]

        while True:
            self.data = self.request.recv(2014).decode('utf-8').strip()
            # print(self.data)

            pieces = self.data.split('\n')
            # print(pieces)

            for piece in pieces:

                if piece == '502000200': continue

                try:
                    values = list(map(int, piece.split(':')))
                except:
                    continue
                # print(values)

                try:
                    x, y, z = values
                except:
                    continue
                
                if x == 2:
                    if y > 0:  
                        LWheels(y*4)
                    else:
                        LWheels(0)
                elif x == 5:
                    if y > 0:  
                        RWheels(-(y*4))
                    else:
                        RWheels(0)
                elif x == 310:
                    if y == 1:
                        LWheels(-400)
                    elif y == 0:
                        LWheels(0)
                elif x == 311:
                    if y == 1:
                        RWheels(400)
                    elif y == 0:
                        RWheels(0)
                elif x == 0:
                    if y > 0:
                        LWheels(y/40)
                        RWheels(y/40)
                    elif y < 0:
                              LWheels(y/40)
                              RWheels(y/40)
                elif x == 1:
                    if i == 4 :
                        if y > 0:
                            LWheels(-(y/40))
                            RWheels((y/40))
                        else:
                            LWheels(-(y/40))
                            RWheels((y/40))
                        i = 0
                    else:
                        i = i + 1
                elif x == 3:
                    if y > 0:
                        if defarm[2] - (y/3300) > 0:
                           defarm[2] -= y/3300
                           moveJoint(7,defarm[2],999)
                        else:
                           defarm[2] = 0
                           moveJoint(7,0,999)
                    else:
                        if defarm[2] - (y/3300) < 999:
                           defarm[2] -= y/3300
                           moveJoint(7,defarm[2],999)
                        else:
                           defarm[2] = 999
                           moveJoint(7,999,999)
                elif x == 4:
                    if y > 0:
                        if defarm[1] - (y/3300) > 200:
                           defarm[1] -= (y/3300)
                           moveJoint(6,defarm[1],999)
                        else:
                           defarm[1] = 200
                           moveJoint(6,200,100)
                    else:
                        if defarm[1] - (y/3300) < 800:
                           defarm[1] -= (y/3300)
                           moveJoint(6,defarm[1],999)
                        else:
                           defarm[1] = 800
                           moveJoint(6,800,100)
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
                    defarm = [1000,512,512]
                    moveJoint(7,512,100)
                    moveJoint(6,512,100)
                    moveJoint(5,1000,100)
                    thread1.position = 1000
                elif x == 315:
                    print('servo reset')
                    start_pos()
                    LWheels(0)
                    RWheels(0)
                    defarm = [200, 200, 512]
                elif x == 314:
                    print('quiting')
                elif x ==305:
                    if CWorking:
                        if y == 1:
                            if camerasrt:
                                stopcam()
                                camerasrt = False
                            else:
                                startcam()
                                camerasrt = True
                else:
                    print(x)
                
if __name__ == "__main__":
    HOST, PORT = "", 9999
                           
socketserver.TCPServer.allow_reuse_address = True
server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
print('Server started.')
server.serve_forever()
