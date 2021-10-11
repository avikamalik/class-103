import cv2
import time

def take_snapshot():
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(1)
    result = True
    if videoCaptureObject.isOpened():
        
        while(result):
            time.sleep(2)
            #read the frames while the camera is on
            ret,frame = videoCaptureObject.read()
           # breakpoint()


            #cv2.imwrite() method is used to save an image to any storage device
            cv2.imwrite("NewPicture1.png",frame)
            result = False

    # releases the camera
    videoCaptureObject.release()
    #closes all the window that might be opened while this process
    cv2.destroyAllWindows()

take_snapshot()
        
    