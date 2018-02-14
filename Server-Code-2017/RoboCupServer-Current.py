import socketserver as SocketServer
import sys
from GPIO import *
#SwitchOFF()
from emuBot import *

wheelMode(1)
wheelMode(2)
wheelMode(3)
wheelMode(4)
jointMode(5)
jointMode(6)
jointMode(7)
SwitchON() #Added for testing.

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        while 1:
            #sc.flush()
            self.data = self.request.recv(2014).decode('utf-8').strip()
            new = self.data.split('\n')
            for i in new:
                if i != "":
                    if i == "ON":
                        SwitchON()
                    elif i == "OFF":
                        SwitchOFF()
                    else:
                        ID = int(i[0])
                        if ID < 5:
                            try:
                                moveWheel(ID, int(i[1:]))
                            except: pass
                        else:
                            moveJoint(ID, int(i[1:-4]), i[-4:])
               # else:
                #    print(i)
                
if __name__ == "__main__":
    HOST, PORT = "", 9999
    
SocketServer.TCPServer.allow_reuse_address = True
server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

print('Servre Started')
server.serve_forever()



