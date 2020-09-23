import zmq
import random
import sys
import time
# if you want to recv the data from pub_ultrasonic you have to 
# provide pub_ultrasonic port(1221) while runnning it
port = "1221"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

# socket = context.socket(zmq.PUB)
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
# socket.bind("tcp://*:%s" % port)
socket.connect("tcp://localhost:%s" % port)
print("Master: Entering into while loop: ", len(sys.argv))
topicfilter = "10002"
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)
dic_c2 = {}
while True:
    try:
        string = socket.recv()
        dic_c2[str(string[:5])] = string[6:]
        print("C2: ", dic_c2)
    except Exception as e:
        print("error: ", e)
print("C2: ", dic_c2)
