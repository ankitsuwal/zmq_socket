import os
import base64
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
# socket = context.socket(zmq.REQ)
print("Collecting updates from weather server...")
socket.connect ("tcp://localhost:%s" % port)

if len(sys.argv) > 2:
    socket.connect ("tcp://localhost:%s" % port1)
path_to_ = "/home/dell/work/ipc/images/"
# Subscribe to zipcode, default is NYC, 10001
# topicfilter = "10001"
# socket.setsockopt(zmq.SUBSCRIBE, topicfilter)
# socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

# Process 5 updates
# total_value = 0
# for update_nbr in range(10):
#     string = socket.recv()
#     topic, messagedata = string.split()
#     total_value += int(messagedata)
#     print(topic, messagedata)

# print("Average messagedata value for topic '%s' was %dF" % (topicfilter, total_value / update_nbr))
for val in os.listdir(path_to_):
    try:
        f = open(path_to_ + val,'rb')
        bytes = bytearray(f.read())
        strng = base64.b64encode(bytes)
        socket.send(strng)
        # message = socket.recv()
        # print("Received reply %s [ %s ]" % (val, message))
    except Exception as e:
        print("Client: ", e)
    # f.close()