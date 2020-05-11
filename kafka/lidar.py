# sudo systemctl start kafka
# You can only have one consumer per topic (unless it’s ok to have the job done several times)
import sys
import time
import cv2
from kafka import KafkaProducer
import numpy as np
import base64
import imutils
topic = "lidar"

# def publish_camera():
#     """
#     Publish camera video stream to specified Kafka topic.
#     Kafka Server is expected to be running on the localhost. Not partitioned.
#     """
#     # Start up producer
#     producer = KafkaProducer(bootstrap_servers='localhost:9092')
#     cap = cv2.VideoCapture(0)
#     start_time = time.time()
#     frame_count = 0
#     while cap.isOpened():
#         try: 
#             ret, frame = cap.read()
#             frame_count += 1
#             print("frame No: ", frame_count)
#             if not ret:
#                  print("error while reading video")
#             resized_img = imutils.resize(frame, height=200)
#             encoded, buffer = cv2.imencode('.jpg', resized_img)
#             producer.send(topic, base64.b64encode(buffer))

#             # cv2.imshow("camera_send", resized_img)
#             if cv2.waitKey(25) & 0xFF == ord('q'):
#                     break
#         except KeyboardInterrupt:
#             cap.release()
#             cv2.destroyAllWindows()

#     end_time = time.time()
#     print(end_time - start_time)
def lidar_exc_eng():
    """
        send lidar data to RDS algo and GUI to represend data
    """
    # producer = KafkaProducer(bootstrap_servers='localhost:9092')

    pass
def publish_lidar():
    """
        .
        .
    """
    # Start reading lidar data
    # TODO: logic to read lidar data
    # TODO: Send lidar data to lidar_exc_eng()
    pass

if __name__ == '__main__':
    """
        Producer will publish to Kafka Server a video file given as a system arg. 
        Otherwise it will default by streaming webcam feed.
    """
    print("publishing feed!")
    publish_lidar()