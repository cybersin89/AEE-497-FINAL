# -*- coding: utf-8 -*-
"""
Created on Thu May 23 09:36:04 2019

@author: etemo_000
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


h=6
file1='Coordinates.xlsx'
xy = pd.read_excel(file1)
file2='distancematrix.xlsx'
length=pd.read_excel(file2,header=2)

def coords_dists(xy,length):
    
    coord=np.array(xy)  #coordinates of all cities
    x,y=coord[:,0],coord[:,1]
    #plt.plot(x,y,'o')  #check point1
    length.drop(['İL ADI'],axis=1,inplace=True)#distances between each city
    distance1=np.array(length)
    plaka=distance1[:,0]
    distance=np.delete(distance1,0,1)
    for i in range(81):
        distance[i][i]=999999
    plaka=np.array(plaka)
        
    return x,y,distance,plaka