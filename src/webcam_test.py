# Video capture test script
import cv2
import time

if __name__ == '__main__':
    print ("Video Capture Test Script for SetBot")
    vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    while (True):
        ret, frame = vid.read()
#        if (not ret):
#            continue
            
        frame = cv2.resize(frame, (540, 380), fx = 0, fy = 0,
                         interpolation = cv2.INTER_CUBIC)
          

        # conversion of BGR to grayscale is necessary to apply this operation
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     
        # adaptive thresholding to use different threshold
        # values on different regions of the frame.
        Thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                               cv2.THRESH_BINARY_INV, 11, 2)
     
        cv2.imshow('frame', frame)
        cv2.imshow('Thresh', Thresh)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
#        time.sleep(0)
    
    vid.release()
    cv2.destroyAllWindows()
    