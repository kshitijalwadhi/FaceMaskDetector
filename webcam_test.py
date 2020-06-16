from imutils.video import VideoStream
import imutils
import cv2
import time


# when using camera
vs = VideoStream(src=0).start()
time.sleep(2.0)


while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    cv2.imshow("frame", frame)
    key = cv2.waitKey(1) & 0xFF
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
