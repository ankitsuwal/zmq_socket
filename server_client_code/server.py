#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

# import zmq
# import time
# import base64

# context = zmq.Context()
# socket = context.socket(zmq.REP)
# socket.bind("tcp://*:5555")

"""
# while True:
#     #  Wait for next request from client
#     message = socket.recv()
#     print("Received request: %s" % message)

#     #  Do some 'work'
#     time.sleep(3)

#     #  Send reply back to client
#     socket.send(b"World")
"""

# print("Connecting server to receive images.\n\n")
# count = 0
# while True:
#     try:
#         message = socket.recv()
#         count += 1
#         print(">>>>: ", count)
#         fname = str(count) +"_img.jpg"
#         f = open(fname, 'wb')
#         ba = bytearray(base64.b64decode(message))
#         f.write(ba)
#         time.sleep(2)
#         socket.send(b"Aknowledgement")
#     except Exception as e:
#         print("Server : ", e)
#     # f.close()

import zmq
import random
import sys
import time

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)
print("entering into while loop: ", len(sys.argv))
while True:
    try:
        topic = random.randrange(9999,10005)
        messagedata = random.randrange(1,215) - 80
        print(">>>>>: %d %d" % (topic, messagedata))
        socket.send_string("%d %d" % (topic, messagedata))
        time.sleep(1)
    except Exception as e:
        print("error: ", e)