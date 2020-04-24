#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#
import os
import zmq
import base64

context = zmq.Context()

"""
# Socket to talk to server
# print("Connecting to hello world server…")
# socket = context.socket(zmq.REQ)
# socket.connect("tcp://localhost:5555")

# #  Do 10 requests, waiting each time for a response
# for request in range(10):
#     print("Sending request %s …" % request)
#     socket.send(b"Hello")

#     #  Get the reply.
#     message = socket.recv()
#     print("Received reply %s [ %s ]" % (request, message))
"""



# print("Connecting server to sending images from client2.\n\n")
# socket = context.socket(zmq.REQ)
# socket.connect("tcp://localhost:5555")
# path_to_dir = "/home/dell/work/ipc/img/"
# for val in os.listdir(path_to_dir):
#     try:
#         f = open(path_to_dir + val,'rb')
#         bytes = bytearray(f.read())
#         strng = base64.b64encode(bytes)
#         socket.send(strng)
#         message = socket.recv()
#         print("Received reply %s [ %s ]" % (val, message))
#     except Exception as e:
#         print("Client: ", e)
#     # f.close()
import sys
import zmq

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)
    
if len(sys.argv) > 2:
    port1 =  sys.argv[2]
    int(port1)

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from weather server...")
socket.connect ("tcp://localhost:%s" % port)

if len(sys.argv) > 2:
    socket.connect ("tcp://localhost:%s" % port1)

# Subscribe to zipcode, default is NYC, 10001
topicfilter = "10002"
# socket.setsockopt(zmq.SUBSCRIBE, topicfilter)
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)
# Process 5 updates
total_value = 0
for update_nbr in range(5):
    string = socket.recv()
    topic, messagedata = string.split()
    total_value += int(messagedata)
    print(">>>: ", topic, messagedata)

print("Average messagedata value for topic '%s' was %dF" % (topicfilter, total_value / update_nbr))