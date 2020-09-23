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
from flask import Flask
from flask import Response
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


def generate():
    global output_frame
    while True:
        if output_frame is None:
            continue
        (flag, encoded_image) = cv2.imencode(".jpg", output_frame)
        if not flag:
            continue
        img = bytearray(encoded_image)
        length = str(len(img)).encode()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n'
               b'Cache-Control: no-cache, no-store, must-revalidate\r\n'
               b'Pragma: no-cache\r\n'
               b'Expires: 0\r\n'
               b'Cache-Control: public, max-age=0\r\n'
               b'Content-Length: ' + length + b'\r\n'
                                              b'\r\n' + img + b'\r\n')


# if you want to recv the data from pub_ultrasonic you have to
# provide pub_ultrasonic port(1221) while runnning it
port = "1234"
# port1 = "3333"
if len(sys.argv) > 1:
    print("1111111111: ", len(sys.argv))
    port1 = sys.argv[1]
    int(port1)

if len(sys.argv) > 2:
    print("222222222: ", len(sys.argv))
    port2 = sys.argv[2]
    int(port2)
# print("\n\n>>>>>>>>>>>>>>: ", port, port1, len(sys.argv))
# socket = context.socket(zmq.PUB)
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt_string(zmq.SUBSCRIBE, str(''))

context = zmq.Context()
socket1 = context.socket(zmq.SUB)
socket1.setsockopt_string(zmq.SUBSCRIBE, str(''))
# socket.bind("tcp://*:%s" % port)
# socket.connect("tcp://localhost:%s" % port)
#  connecting one more port 

if len(sys.argv) > 1:
    print("You are in second port")
    socket.connect("tcp://localhost:%s" % port1)
if len(sys.argv) > 2:
    print("You are in third port")
    socket1.connect("tcp://localhost:%s" % port2)

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
''''''

#  ::::: ***** ::::: ***** ::::: *****  # 
#  below code: video reader
#  ::::: ***** ::::: ***** ::::: *****  #
count = 0


def capture_frames():
    global output_frame
    while True:
        try:
            # TODO: logic to receive data
            topic, frame = socket.recv_multipart()
            topic1, frame1 = socket1.recv_multipart()

            # frame = socket.recv_string()
            # count += 1
            # print("count: ", count)
            img = base64.b64decode(frame)
            img1 = base64.b64decode(frame1)
            npimg = np.fromstring(img, dtype=np.uint8)
            npimg1 = np.fromstring(img1, dtype=np.uint8)
            source = cv2.imdecode(npimg, 1)
            source1 = cv2.imdecode(npimg1, 1)
            topic = topic.decode("utf-8")
            topic1 = topic1.decode("utf-8")
            # print('>>>>>>: ', topic)
            if topic == "camera":
                cv2.imshow("camera_1", source)
            # if topic == "ods":
            #     cv2.imshow("ods_1", source)
            # if topic1 == "rds":
            #     cv2.imshow("rds_1", source1)
            output_frame = np.concatenate((source, source1), axis=1)
            cv2.imshow("Master", output_frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        except KeyboardInterrupt:
            # cap.release()
            cv2.destroyAllWindows()


@app.route('/video_feed')
def video_feed():
    return Response(generate(), mimetype="multipart/x-mixed-replace; boundary=frame")

import threading
if __name__ == '__main__':

    t = threading.Thread(target=capture_frames, args=())
    t.start()
    time.sleep(3)
    app.run(host='192.168.1.27', port=int(8001), threaded=True)
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
