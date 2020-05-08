import cv2
import datetime
import numpy as np
import base64
# from flask import Flask, Response
from kafka import KafkaConsumer

# Fire up the Kafka Consumer
topic = "camera"

consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'])

def get_video_stream():
    for frame in consumer:
        try: 
            img = base64.b64decode(frame.value)
            npimg = np.fromstring(img, dtype=np.uint8)
            source = cv2.imdecode(npimg, 1)
            
            edg_img = cv2.Canny(source, 50, 50)
            # encoded, buffer = cv2.imencode('.jpg', edg_img)
            
            topic = frame.topic
            cv2.imshow("RDS", edg_img)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
        except KeyboardInterrupt:
            cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    # app.run(host='0.0.0.0', debug=True)
    get_video_stream()