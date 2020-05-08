import sys
import time
import cv2
from kafka import KafkaProducer
import numpy as np
import base64
import imutils
topic = "camera"

def publish_camera():
    """
    Publish camera video stream to specified Kafka topic.
    Kafka Server is expected to be running on the localhost. Not partitioned.
    """
    # Start up producer
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    cap = cv2.VideoCapture(0)
    start_time = time.time()
    frame_count = 0
    while cap.isOpened():
        try: 
            ret, frame = cap.read()
            frame_count += 1
            print("frame No: ", frame_count)
            if not ret:
                 print("error while reading video")
            resized_img = imutils.resize(frame, height=400)
            encoded, buffer = cv2.imencode('.jpg', resized_img)
            producer.send(topic, base64.b64encode(buffer))

            # cv2.imshow("camera_send", resized_img)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
        except KeyboardInterrupt:
            cap.release()
            cv2.destroyAllWindows()

    end_time = time.time()
    print(end_time - start_time)

if __name__ == '__main__':
    """
    Producer will publish to Kafka Server a video file given as a system arg. 
    Otherwise it will default by streaming webcam feed.
    """
    print("publishing feed!")
    publish_camera()