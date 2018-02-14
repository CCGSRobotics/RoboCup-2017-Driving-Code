import threading
import time
from definintions import *
print("threading setup")
class myThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.direction = "neutral"
        self.position = int(200)
        self.running = False
    def run(self):
        while self.direction != "":
            if self.direction == "decrease":
                if self.position > 200:
                    self.position -= 10
                #self.running = True
            elif self.direction == "increase":
                if self.position < 1000:
                    self.position += 10
                #self.running = True
            if self.direction != "neutral":
                moveJoint(5,self.position,900)

      #      # Alternative code to handle broken pipe errors
            '''try:
                moveJoint(5,self.position,200)
            except (BrokenPipeError, IOError):
                #print("Broken pipe error caught")
                pass'''
            time.sleep(0.08)
            
            

thread1 = myThread()
thread1.start()
print("threading ready")
