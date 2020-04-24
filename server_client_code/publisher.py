#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import zmq
import time
import base64
import random
import sys

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)
print("entering into while loop: ", len(sys.argv))
count = 0 
while True:
    try:
        # message = socket.recv()
        count += 1
        fname = str(count) + "_img.jpg"
        f = open(fname, 'wb')
        ba = bytearray(base64.b64decode(message))
        f.write(ba)
        time.sleep(2)
    except Exception as e:
        print("error: ", e)