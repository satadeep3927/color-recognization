import cv2 as opencv
capture = opencv.VideoCapture(0)
while(1):
    r, f = capture.read()
    opencv.imshow('frame',f)
    if opencv.waitKey(1) & 0xFF== 27:
        break
capture.release()
opencv.destroyAllWindows() 