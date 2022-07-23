from PIL import ImageGrab
import datetime
import numpy as np
import cv2
from win32api import GetSystemMetrics
def Screen_Record():
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
    time_stamp = datetime.datetime.now(). strftime('%Y-%m-%d %H-%M-%S')
    file_new = f'{time_stamp}.mp4'
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    captured_video = cv2.VideoWriter(file_new, fourcc, 20.0, (width, height))
    webcam=cv2.VideoCapture(0)
    while True:
        image = ImageGrab.grab(bbox=(0, 0, width, height))
        image_np = np.array(image)
        img_next = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
        cv2.waitKey(10)
        if cv2.waitKey(10)==ord('w'):
            while True:
                image = ImageGrab.grab(bbox=(0, 0, width, height))
                image_np = np.array(image)
                img_next = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
                _,frame=webcam.read()
                fr_height,fr_width, _=frame.shape
                img_next[0:fr_height,0:fr_width, :]=frame[0:fr_height,0:fr_width, :]
                cv2.imshow('Screen Recoder', img_next)
                captured_video.write(img_next)
                cv2.waitKey(10)
                if cv2.waitKey(10) == ord('q'):
                    break
        else:
            cv2.imshow('Screen Recoder', img_next)
            captured_video.write(img_next)
            cv2.waitKey(10)
            if cv2.waitKey(10) == ord('q'):
                 break
ch=input("Do You Want to start the screen recorder if yes then press y : ")
print()
if(ch=="y"):
    Screen_Record()
    
