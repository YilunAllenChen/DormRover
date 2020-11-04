# Web streaming example
# Source code from the official PiCamera package
# http://picamera.readthedocs.io/en/latest/recipes2.html#web-streaming

import io
import picamera


cam = picamera.PiCamera()
cam_stream = io.BytesIO()

def vid_gen():  
    while True:
        cam.capture(cam_stream, 'jpeg')
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + cam_stream + b'\r\n')  # concat frame one by one and show result