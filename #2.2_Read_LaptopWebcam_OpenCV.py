import cv2

#videocapture object for webcam capture (0=built-in cam, 1,2, etc for external)
vid_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
vid_capture.set(3,320) #Width
vid_capture.set(4,240) #Height
vid_capture.set(10,10) #Brightness
vid_capture.set(11,10) #Contrast
vid_capture.set(12,50) #Saturation
vid_capture.set(13,10) #Hue


if (vid_capture.isOpened() == False):
	print("Error processing image sequence")

else:
  # Get frame rate information
  fps = int(vid_capture.get(cv2.CAP_PROP_FPS)) #or cv2.CAP_PROP_FPS instead of 5
  print("Frame Rate : ",fps,"frames per second")  
 
  # Get frame count
  frame_count = vid_capture.get(7) #or cv2.CAP_PROP_FRAME_COUNT instead of 5
  print("Frame count : ", frame_count)

while(vid_capture.isOpened()):
  # vCapture.read() methods returns a tuple, first element is a bool 
  # and the second is frame
 
  ret, frame = vid_capture.read()
  
  if ret == True:
    cv2.imshow('My laptop webcam',frame)
    k = cv2.waitKey(20)
    #If you press q stop
    if k == ord('q'):
      break
  else:
     break

# Release the objects
vid_capture.release()
cv2.destroyAllWindows()