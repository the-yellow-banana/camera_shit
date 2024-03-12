# import the opencv library 
import cv2 

##device number which the camera is being inputted to 
cam_input = 0
# define a video capture object
vid = cv2.VideoCapture(cam_input) 

def Display_rawIR():
    while(True): 
      
        # Capture the video frame 
        # by frame 
        ret, frame = vid.read() 

        ##attempt to denoise it 
        frame = cv2.fastNlMeansDenoising(frame, None,  h = 10, templateWindowSize = 13, searchWindowSize = 21) 

        # Display the resulting frame 
        cv2.imshow('rawIR_frame', frame) 
            

        # the 'q' button is set as the 
        # quitting button you may use any 
        # desired button of your choice 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    # After the loop release the cap object 
    vid.release() 
    # Destroy all the windows 
    cv2.destroyAllWindows() 

if __name__ == '__main__':
    Display_rawIR()
  
