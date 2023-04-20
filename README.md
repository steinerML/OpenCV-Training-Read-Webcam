# OpenCV Read from webcam.
Reading from laptop webcam using OpenCV.
## Contents:

In this the case I was reading from the laptop webcam using OpenCV.
I have used the following functions/methods:

| Function        |Action                                                                        | 
|----------------:|------------------------------------------------------------------------------|
|cv2.VideoCapture()   | Creates a video capture object, which would help stream or display the video.|


## Test Video used: 
In this case I haven't included the video due to privacy reasons.


## Summary:

```python
#Creates capture object, reading video from webcam
vid_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
```

