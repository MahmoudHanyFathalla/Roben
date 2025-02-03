from queue import Queue
import queue
from time import time, sleep
from tkinter import *
from PIL import Image, ImageTk
import cv2
import threading
from queue import Queue

# Create an instance of TKinter Window or frame
win = Tk()

UN_AV_IMG = cv2.imread("unav.jpg", cv2.IMREAD_COLOR)



# Set the size of the window
win.geometry("1200x1200")

# Create a Label to capture the Video frames
labels = (Label(win, width = 400, height = 400),
        Label(win, width = 400, height = 400),
        Label(win, width = 400, height = 400))



labels[0].place(x = 0 , y= 0)
labels[1].place(x = 500 , y= 0)
labels[2].place(x = 500 , y= 500)



# global threads

def show_frames():
    camera_caps =[cv2.VideoCapture(0), cv2.VideoCapture(1), cv2.VideoCapture(2)]
    cam_iterator = 0
    while True:
        cameras_frame = camera_caps[0].read(), camera_caps[1].read(), camera_caps[2].read()
        
            # frames(i,cameras_frame)
        if cameras_frame[cam_iterator][0]:
            # Get the latest frame and convert into Image
            cv2image= cv2.cvtColor(cameras_frame[cam_iterator][1],cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            # Convert image to PhotoImage
            imgtk = ImageTk.PhotoImage(image = img)
            labels[cam_iterator].imgtk = imgtk
            labels[cam_iterator].configure(image=imgtk)
                # Repeat after an interval to capture continiously
            win.update_idletasks()
            win.update()
        else:
            camera_caps[cam_iterator] = cv2.VideoCapture(cam_iterator)
            print("An exception occurred") 
            # flag_handler(flag)
        cam_iterator = (cam_iterator + 1) if (cam_iterator + 1) < 3 else 0


show_frames()


