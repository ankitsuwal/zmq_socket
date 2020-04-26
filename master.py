# python master.py port_c3> 3333
import sys
import zmq
import cv2
import time
import zlib
import socket
import random
import numpy as np
import base64
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
# print("\n\n>>>>>>>>>>>>>>: ", port, port1, len(sys.argv))
# socket = context.socket(zmq.PUB)
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt_string(zmq.SUBSCRIBE, str(''))
# socket.bind("tcp://*:%s" % port)
socket.connect ("tcp://localhost:%s" % port)
#  connecting one more port 
if len(sys.argv) > 1:
    print("You are in second port")
    socket.connect ("tcp://localhost:%s" % port1)

print("Master: Entering into while loop: ", len(sys.argv))

topicfilter = "10000"
top = "100031"
# socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)
# socket.setsockopt_string(zmq.SUBSCRIBE, top)

dic_master = {}
# while True:
#     try:
#         string = socket.recv()
#         dic_master[str(string[:5])] = string[6:]
#         print("\n>>>>: ", string[:5], string[6:])
#         # print("Master: ", dic_master)
#     except Exception as e:
#         print("error: ", e)
# print("Master: ", dic_master)


#  ::::: ***** ::::: ***** ::::: *****  # 
#  below code: video reader
#  ::::: ***** ::::: ***** ::::: *****  #
while True:
    try: 
        # TODO: logic to receive data
        topic, frame = socket.recv_multipart()
        # frame = socket.recv_string()
        img = base64.b64decode(frame)
        npimg = np.fromstring(img, dtype=np.uint8)
        source = cv2.imdecode(npimg, 1)
        topic = topic.decode("utf-8")
        if topic == "camera":
            cv2.imshow("camera", source)
        elif topic == "ods":
            cv2.imshow("ods", source)
        # cv2.imshow("Master", source)
        if cv2.waitKey(25) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        cap.release()
        cv2.destroyAllWindows()


# #  ::::: ***** ::::: ***** ::::: *****  # 
# #  below code: lidar txt file transfering
# #  ::::: ***** ::::: ***** ::::: *****  #
# file = open('recv.txt', 'wb')
# while True:
#     try:
#         string = socket.recv()
#         print(string)
#         file.write(string)
#     except Exception as e:
#         print("recv: ", e)
