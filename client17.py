#!/usr/bin/env python

import time
from controller import *


from lib_threading1 import *

for event in gamepad.read_loop():
    x = event.code
    # print(x)
    y = event.value
    z = event.type

    # Messages send via socket must be encoded as a byte string
    to_send = bytes(str(x) + ':' + str(y) + ':' + str(z) + '\n', 'utf-8')

    # print(to_send) # debugging
    sock.sendall(to_send)


