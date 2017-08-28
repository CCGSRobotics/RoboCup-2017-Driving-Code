import subprocess
import socket

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("192.168.100.1", 80))
    return s.getsocketname()[0]


def startCamera():
    print("starting camera buffer...")
    subprocess.call("netcat -l -p 5000 | mplayer -fps 120 -cache 2048 -")
    print("send request to start feed")

def stopCamera():
    print("stopping camera...")
    subprocess.call("killall -9 mplayer")
    subprocess.call("killall -9 netcat")
    print("send request to stop camera feed")


startCamera()
