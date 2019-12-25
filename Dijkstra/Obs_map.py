# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 14:08:08 2019

@author: sanke
"""

import numpy as np
import cv2
def x_worldToImageCoordinate(x_world,resolution):
    x_image=int(x_world*resolution)
    return x_image
    
def y_worldToImageCoordinate(y_world, resolution):
    y_image=int((150-y_world)*resolution)
    return y_image

  
def create_map(resolution):
    mag=1/resolution
    r=int(mag*150)
    s=int(mag*250)
    array=np.ones([r,s])
    """
    array=cv2.circle(array, (int(mag*x_worldToImageCoordinate(190)),int(mag*y_worldToImageCoordinate(130))), int(mag*15), (0, 0, 0), -1)
    array=cv2.ellipse(array,(int(mag*x_worldToImageCoordinate(140)),int(mag*y_worldToImageCoordinate(120))),(int(mag*15),int(mag*6)),0,0,360,0,-1)
    array=cv2.rectangle(array,(int(mag*x_worldToImageCoordinate(50)),int(mag*y_worldToImageCoordinate(112.5))),(int(mag*x_worldToImageCoordinate(100)),int(mag*y_worldToImageCoordinate(67.5))),(0,0,0),-1)
    pts = mag*np.array([[x_worldToImageCoordinate(125),y_worldToImageCoordinate(56)],[x_worldToImageCoordinate(150),y_worldToImageCoordinate(15)],[x_worldToImageCoordinate(173),y_worldToImageCoordinate(15)],[x_worldToImageCoordinate(193),y_worldToImageCoordinate(52)],[x_worldToImageCoordinate(170),y_worldToImageCoordinate(90)],[x_worldToImageCoordinate(163),y_worldToImageCoordinate(52)]], np.int32)
    pts = pts.reshape((-1,1,2))
    """
    array=cv2.circle(array, (int(x_worldToImageCoordinate(190,mag)),int(y_worldToImageCoordinate(130,mag))), int(mag*15), (0, 0, 0), -1)
    array=cv2.ellipse(array,(int(x_worldToImageCoordinate(140,mag)),int(y_worldToImageCoordinate(120,mag))),(int(mag*15),int(mag*6)),0,0,360,0,-1)
    array=cv2.rectangle(array,(int(x_worldToImageCoordinate(50,mag)),int(y_worldToImageCoordinate(112.5,mag))),(int(x_worldToImageCoordinate(100,mag)),int(y_worldToImageCoordinate(67.5,mag))),(0,0,0),-1)
    pts = np.array([[x_worldToImageCoordinate(125,mag),y_worldToImageCoordinate(56,mag)],[x_worldToImageCoordinate(150,mag),y_worldToImageCoordinate(15,mag)],[x_worldToImageCoordinate(173,mag),y_worldToImageCoordinate(15,mag)],[x_worldToImageCoordinate(193,mag),y_worldToImageCoordinate(52,mag)],[x_worldToImageCoordinate(170,mag),y_worldToImageCoordinate(90,mag)],[x_worldToImageCoordinate(163,mag),y_worldToImageCoordinate(52,mag)]], np.int32)
    pts = pts.reshape((-1,1,2))
    array=cv2.fillPoly(array,pts =np.int32([pts]),color=(0,0,0))
    
   
    #cv2.namedWindow('Project',cv2.WINDOW_NORMAL)
    #cv2.resizeWindow('Project',750,450)
    with open('path.txt') as f:
        path = [tuple(map(int, i.split('\t'))) for i in f]
    #print(path)
    
    for i in range(len(path)-1):
        array=cv2.line(array,(x_worldToImageCoordinate(path[i][0],mag),y_worldToImageCoordinate(path[i][1],mag)),(x_worldToImageCoordinate(path[i+1][0], mag),y_worldToImageCoordinate(path[i+1][1], mag)),(0,0,0),1)
        #display=cv2.resize(array,(750,450), cv2.INTER_AREA)
        cv2.imshow('Project', array)
        cv2.namedWindow('Project',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Project',760,460)
        cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    
    return array

create_map(1)
"""def xyz(resolution):
    img=create_map()
    width = int(img.shape[1]/resolution)
    height = int(img.shape[0]/resolution)
    dim = (width, height)
# resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    res_fix=cv2.resize(resized,(750,450), interpolation=cv2.INTER_AREA)
    cv2.imshow("Resized image", res_fix)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
xyz(5)
"""


