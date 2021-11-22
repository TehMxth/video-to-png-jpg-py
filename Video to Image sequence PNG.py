# Importing all necessary libraries 
import cv2 
import os 

vidpath = "D:/Desktop/"
vidname = "Video.mp4"

# Read the video from specified path 
cam = cv2.VideoCapture(vidpath+vidname) 
  
try: 
      
    # creating a folder named data 
    if not os.path.exists(str(vidpath+'/data')): 
        os.makedirs(str(vidpath+'/data')) 
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 
  
# frame 
currentframe = 0
length = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
  
while(True): 
      
    # reading from frame 
    ret,frame = cam.read() 
  
    if ret: 
        # if video is still left continue creating images 
        name = vidpath + '/data/frame' + str(currentframe) + '.png'
        print ('Creating...' + name + " " + str(int(currentframe)/length*100)[:5] + "%")
  
        # writing the extracted images 
        cv2.imwrite(name, frame) 
  
        # increasing counter so that it will 
        # show how many frames are created 
        currentframe += 1
    else: 
        break
  
# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows()
print('Done')