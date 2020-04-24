import zmq
import random
import sys
import time

port = "1221"
# if len(sys.argv) > 1:
#     port =  sys.argv[1]
#     int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)
print("entering into while loop: ", len(sys.argv))
counter = 1000
while True:
    try:
        topic = random.randrange(10000,10005)
        # messagedata = random.randrange(1,215) - 80
        # counter += 1
        # topic = "UltraSonic"
        messagedata = "UltraSonic data in string form " + str(topic)
        print(">>>>>: %d %s" % (topic, messagedata))
        # socket.send_string("%d %d" % (topic, messagedata))
        # socket.send_string("%s %s" % (topic, messagedata))
        socket.send_string("%s %s" % (str(topic), messagedata))
        time.sleep(1)
    except Exception as e:
        print("error: ", e)