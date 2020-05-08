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

if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

# socket = context.socket(zmq.PUB)
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt_string(zmq.SUBSCRIBE, str(''))
# socket.bind("tcp://*:%s" % port)
socket.connect ("tcp://localhost:%s" % port)
# print("Master: Entering into while loop: ", len(sys.argv))
topicfilter = "10001"
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)
dic_c1 = {}
# while True:
#     try:
#         string = socket.recv()
#         dic_c1[str(string[:5])] = string[6:]
#         print("C1: ", dic_c1)
#     except Exception as e:
#         print("error: ", e)
# print("C1: ", dic_c1)


#  ::::: ***** ::::: ***** ::::: *****  # 
#  below code: video reader
#  ::::: ***** ::::: ***** ::::: *****  #
while True:
    try: 
        # TODO: logic to receive data
        frame = socket.recv_string()
        img = base64.b64decode(frame)
        npimg = np.fromstring(img, dtype=np.uint8)
        source = cv2.imdecode(npimg, 1)
        cv2.imshow("c1_vc", source)
        if cv2.waitKey(25) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        cap.release()
        cv2.destroyAllWindows()