# Web streaming example
# Source code from the official PiCamera package
# http://picamera.readthedocs.io/en/latest/recipes2.html#web-streaming

import io
# import picamera
# camera = picamera.PiCamera()
# def vid_gen():
#     while True:
#         cam_stream = io.BytesIO()
#         frame = cam.capture(cam_stream, 'jpeg')
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + cam_stream.getvalue() + b'\r\n')


from camera_pi import Camera

def vid_gen():
    camera = Camera()
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
