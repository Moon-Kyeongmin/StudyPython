import time
import picamera

# camera=picamera.PiCamera()
# try:
#     camera.start_preview()
#     time.sleep(10)
#     camera.stop_preview()
# finally:
#     camera.close()

with picamera.PiCamera() as camera:
    camera.resolution=(640,480)
    camera.start_preview()
    camera.start_recording('foo.h264')
    camera.wait_recording(5)
    camera.stop_recording()
    camera.stop_preview()
