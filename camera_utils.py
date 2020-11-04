'''
Backend of the DormRover project. Interaction with C library powered by ctypes
'''
from picamera import PiCamera
import io
from threading import Condition

camera = PiCamera()

class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

def vid_gen():
    while True:
        with output.condition:
            output.condition.wait()
            frame = output.frame
        yield (
            b'--FRAME\r\n'
            b'Content-Type: image/jpeg\r\n'
            b'Content-Length' + len(frame) + '\r\n\r\n' + 
            frame + b'\r\n'
        )

output = None

with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
    output = StreamingOutput()
    camera.start_recording(output, format='mjpeg')


    # cleanup step. Integrate into backend?
    # finally:
    #     camera.stop_recording()