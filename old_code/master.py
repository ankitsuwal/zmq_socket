# python master.py port_c3> 3333
import zmq
import random
import sys
import time
# if you want to recv the data from pub_ultrasonic you have to 
# provide pub_ultrasonic port(1221) while runnning it
port = "1221"
# port1 = "3333"
if len(sys.argv) > 1:
    port1 =  sys.argv[1]
    int(port1)

# if len(sys.argv) > 2:
#     port1 =  sys.argv[2]
#     int(port1)
print("\n\n>>>>>>>>>>>>>>: ", port, port1, len(sys.argv))
# socket = context.socket(zmq.PUB)
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
# socket.bind("tcp://*:%s" % port)
socket.connect ("tcp://localhost:%s" % port)
#  connecting one more port 
if len(sys.argv) > 1:
    print("You are in second port")
    socket.connect ("tcp://localhost:%s" % port1)

print("Master: Entering into while loop: ", len(sys.argv))

topicfilter = "10000"
top = "100031"
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)
socket.setsockopt_string(zmq.SUBSCRIBE, top)

dic_master = {}
while True:
    try:
        string = socket.recv()
        dic_master[str(string[:5])] = string[6:]
        print("\n>>>>: ", string[:5], string[6:])
        # print("Master: ", dic_master)
    except Exception as e:
        print("error: ", e)
print("Master: ", dic_master)