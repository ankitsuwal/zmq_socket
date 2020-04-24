
import zmq
import random
import sys
import time
# if you want to recv the data from pub_ultrasonic you have to 
# provide pub_ultrasonic port(1221) while runnning it
port = "1221"
if len(sys.argv) > 1:
    port1 =  sys.argv[1] # 3333
    int(port1)
# if len(sys.argv) > 2:
#     port1 =  sys.argv[2]
#     int(port1)
# print("\n\n>>>>>>>>>>>>>>: ", port, port1, len(sys.argv))

# Socket to talk to server
context1 = zmq.Context()
socket1 = context1.socket(zmq.PUB)
socket1.bind("tcp://*:%s" % port1)

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect ("tcp://localhost:%s" % port)
# print("Master: Entering into while loop: ", len(sys.argv))
topicfilter = "10003"
send_topicfilter = "100031"
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)
dic_c3 = {}
# print(dir(socket1))
while True:
    try:
    	# receiving oprations
        string = socket.recv()
        dic_c3[str(string[:5])] = string[6:]
        print("C3: ", dic_c3)
        # sendig opration
        topic = random.randrange(100,105)
        messagedata = "UltraSonic data in string form " + str(topic)
        # print(">>>>>: %s %s" % (send_topicfilter, messagedata))
        # socket1.send_string("%s %s" % (str(topic), messagedata))
        socket1.send_string("%s %s" % (send_topicfilter, messagedata))
    except Exception as e:
        print("error: ", e)
print("C3: ", dic_c3)