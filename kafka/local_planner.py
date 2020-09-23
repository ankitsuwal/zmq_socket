import cv2
import datetime
import numpy as np
import base64
# from flask import Flask, Response
from kafka import KafkaConsumer
import threading
import time
import sys
# Fire up the Kafka Consumer
topic1 = "send_by_ods"
topic2 = "send_by_rds"
# consumer1 = KafkaConsumer(topic1, bootstrap_servers=['localhost:9092'])
# consumer2 = KafkaConsumer(topic2, bootstrap_servers=['localhost:9092'])
rocket = 0
class LocalPlanner:
    """docstring for LocalPlanner"""
    def __init__(self):
        super(LocalPlanner, self).__init__()
        self.consumer1 = KafkaConsumer(topic1, bootstrap_servers=['localhost:9092'])
        self.consumer2 = KafkaConsumer(topic2, bootstrap_servers=['localhost:9092'])
    
    def start_consumers(self):
        # creating threads  
        consumer1_thread = threading.Thread(target=self.send_by_ods, args=(self.consumer1,))
        consumer1_thread.start()

        consumer2_thread = threading.Thread(target=self.send_by_rds, args=(self.consumer2,))
        consumer2_thread.start()

        # starting threads
        # wait until all threads finish
        # consumer1_thread.join()
        # consumer2_thread.join()
    
    def send_by_ods(self, o_consumer):
        print("1111111111111111111", o_consumer)
        for frame in o_consumer:
            try: 
                img = base64.b64decode(frame.value)
                npimg = np.fromstring(img, dtype=np.uint8)
                source = cv2.imdecode(npimg, 1)
                
                # edg_img = cv2.Canny(source, 50, 50)
                # encoded, buffer = cv2.imencode('.jpg', edg_img)
                
                # topic = frame.topic
                o_topic = frame.topic
                print("111: ", o_topic)
                cv2.imshow(o_topic, source)

                # cv2.imshow(topic2, source)
                # time.sleep(1)

                if cv2.waitKey(25) & 0xFF == ord('q'):
                        break
            except KeyboardInterrupt:
                cap.release()
                cv2.destroyAllWindows()

    def send_by_rds(self, r_consumer):
        print("2222222222222222222", r_consumer)
        for frame in r_consumer:
            try: 
                img = base64.b64decode(frame.value)
                npimg = np.fromstring(img, dtype=np.uint8)
                source = cv2.imdecode(npimg, 1)
                
                # edg_img = cv2.Canny(source, 50, 50)
                # encoded, buffer = cv2.imencode('.jpg', edg_img)
                
                # topic = frame.topic
                r_topic = frame.topic
                print("222: ", r_topic)
                cv2.imshow(r_topic, source)
                # time.sleep(1)
                # cv2.imshow(topic2, source)

                if cv2.waitKey(25) & 0xFF == ord('q'):
                        break
            except KeyboardInterrupt:
                cap.release()
                cv2.destroyAllWindows()

def get_video_stream():
    for frame in consumer1:
        try: 
            img = base64.b64decode(frame.value)
            npimg = np.fromstring(img, dtype=np.uint8)
            source = cv2.imdecode(npimg, 1)
            
            # edg_img = cv2.Canny(source, 50, 50)
            # encoded, buffer = cv2.imencode('.jpg', edg_img)
            
            # topic = frame.topic
            cv2.imshow(topic1, source)
            # cv2.imshow(topic2, source)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
        except KeyboardInterrupt:
            cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    # app.run(host='0.0.0.0', debug=True)
    obj = LocalPlanner()
    obj.start_consumers()
    # get_video_stream()

    