# Web streaming example
# Source code from the official PiCamera package
# http://picamera.readthedocs.io/en/latest/recipes2.html#web-streaming

import io
import picamera


cam = picamera.PiCamera()
cam_stream = io.BytesIO()

def vid_gen():
    while True:
        frame = cam.capture('a.jpg','jpeg')
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('a.jpg').read() + b'\r\n')