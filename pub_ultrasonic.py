import cv2
import zmq
import sys
import time
import base64
import socket
import random
import imutils
port = "1221"
# if len(sys.argv) > 1:
#     port =  sys.argv[1]
#     int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)
# print("entering into while loop: ", len(sys.argv))
counter = 1000

#  ::::: ***** ::::: ***** :::::  # 
#  below code: message transfer
#  ::::: ***** ::::: ***** :::::  # 

# while True:
#     try:
#         topic = random.randrange(10000,10005)
#         messagedata = "UltraSonic data in string form " + str(topic)
#         print(">>>>>: %d %s" % (topic, messagedata))
#         socket.send_string("%s %s" % (str(topic), messagedata))
#         time.sleep(1)
#     except Exception as e:
#         print("error: ", e)

#  ::::: ***** ::::: ***** ::::: *****  # 
#  below code: web cam video transfer
#  ::::: ***** ::::: ***** ::::: *****  #
cap = cv2.VideoCapture(0)
# print(dir(socket))
import json
while cap.isOpened():
    try: 
        ret, frame = cap.read()
        if not ret:
             print("error while reading video")
        resized_img = imutils.resize(frame, height=400)
        encoded, buffer = cv2.imencode('.jpg', resized_img)
        socket.send_multipart([b"camera", base64.b64encode(buffer)])
        # cv2.imshow("cv2_send", resized_img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        cap.release()
        cv2.destroyAllWindows()
        
#  ::::: ***** ::::: ***** ::::: *****  # 
#  below code: lidar txt file transfering
#  ::::: ***** ::::: ***** ::::: *****  #
# file = open('/home/dell/work/ipc_framework/lidar/0000000108.txt', 'rb')
# # data = file.read(4096)
# # 
# lines = file.readlines() 
# try:
#     for line in lines:
#         print(type(line), line)
#         # import pdb;pdb.set_trace()
#         socket.send_string(str(line))
#         # time.sleep(1)
# except Exception as e:
#     print(">>>: ", e)
