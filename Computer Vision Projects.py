#!/usr/bin/env python
# coding: utf-8

# # Detecting Color space using HSV color

# In[1]:


import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    frame1 = cv2.flip(frame,1)
    hsv_frame = cv2.cvtColor(frame1,cv2.COLOR_BGR2HSV)
    
    #Red color detection:
    low_red = np.array([0,50,50])
    high_red = np.array([10,255,255])
    red_mask = cv2.inRange(hsv_frame,low_red,high_red)
    red = cv2.bitwise_and(frame1,frame1,mask=red_mask)
    
    #Blue color detection:
    low_blue = np.array([94,80,2])
    high_blue = np.array([126,255,255])
    blue_mask = cv2.inRange(hsv_frame,low_blue,high_blue)
    blue = cv2.bitwise_and(frame1,frame1,mask=blue_mask)
    
    
    #Green color detection:
    low_green = np.array([25,52,72])
    high_green = np.array([102,255,255])
    green_mask = cv2.inRange(hsv_frame,low_green,high_green)
    green = cv2.bitwise_and(frame1,frame1,mask=green_mask)
    
    cv2.imshow('Frame',frame1)
    cv2.imshow('Red_mask',red)
    #cv2.imshow('Blue_mask',blue)
    #cv2.imshow('Green_mask',green)
    
    if cv2.waitKey(1) & 0xff == 27:
        break
        
        
cap.release()
cv2.destroyAllWindows()


# In[4]:


import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    frame1 = cv2.flip(frame,1)
    hsv_frame = cv2.cvtColor(frame1,cv2.COLOR_BGR2HSV)
    
    #Red color detection:
    low_red = np.array([161,155,84])
    high_red = np.array([179,255,255])
    red_mask = cv2.inRange(hsv_frame,low_red,high_red)
    red = cv2.bitwise_and(frame1,frame1,mask=red_mask)
    
    
    cv2.imshow('Frame',frame1)
    cv2.imshow('Red_mask',red_mask)
    
    
    if cv2.waitKey(1) & 0xff == 27:
        break
        
cap.release()
cv2.destroyAllWindows()
    


# In[ ]:


import numpy as np
imprt

