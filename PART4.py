# -*- coding: utf-8 -*-
"""
Created on Sat May 18 22:41:24 2019

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
    
def path(plaka,h):
    
    p=[]
#    plaka=np.delete(plaka,int(h))
    l=list(plaka)
    np.random.shuffle(l)
#    p.append(h)
    for i in range(81):
        p.append(l[i])
    p.append(p[0])
    p=np.array(p)
    p=p.astype(int)
    return p

def get_dist(p):
    m=[]
    dist=0
   
    for i in range(81):
        m.append(distance[int(p[i]-1)][int(p[i+1]-1)])
        dist=dist+m[i]
    return dist

def drawing(route):
    for i,j in zip(route[:-1],route[1:]):
        plt.plot([x[i-1],x[j-1]],[y[i-1],y[j-1]],'-o')
        plt.plot(x[h-1],y[h-1],'*')
    plt.show()
    

def crossover(route1,route2):
    
    route1 =route1[:-1]
    route2 = route2[:-1]
    s     = np.random.randint(0,n)
    route3 = np.hstack((route1[:s], route2[s:]))
    
    unique, counts = np.unique(route3, return_counts=True)
    d = dict(zip(unique, counts))
    replacewith=[]
    for i in d:
        if d[i]==2:
            replacewith.append(i)
        
    if len(set(route3))!=len(set(route2)):
        missing = list(set(route1)-set(route3))
        for i,j in zip(replacewith,missing):
            if np.random.rand()>.5:
                index=np.where(route3==i)[0][0]
            else:
                index=np.where(route3==i)[0][1]            
            route3[index]=j
    #mutation
    if np.random.rand()>0.1:
        a,b = np.random.randint(0,n,2)
        route3[a], route3[b] = route3[b], route3[a]
        
    route3 = np.append(route3,route3[0])
    return route3
    

def initial_population(n):
    
    population = []
    for i in range(n):
        p = path(plaka,h)
        population.append(p)
    population=np.array(population)
    population = sort_population(population)    
    return population


def populations_distances(population): 
    perf = []
    for i in population:
        perf.append(get_dist(i))
    return np.array(perf)


def sort_population(population):

    performance = populations_distances(population)
    i = np.argsort(performance)
    return population[i]


def multi(population,n):
    
    population=population[:n]
    newpop = []
    for i in population:
        for j in population:
            newpop.append(crossover(i,j))
    newpop = np.array(newpop)
    newpop = sort_population(newpop)
    return newpop
    

### main program ###
x,y,distance,plaka=coords_dists(xy,length)
n= len(x)
population  = initial_population(100)
shortest_dist = get_dist(population[0])
shortest_route = population[0]
i = 0
try:
      while i<10000:
          i += 1
          print('possible route', i, 'is with distance %5.2f'% get_dist(population[0]))
          drawing(population[0])
         
          population = multi(population,10)
          if get_dist(population[0]) < shortest_dist:
                shortest_dist = get_dist(population[0])
                shortest_route = population[0]
except KeyboardInterrupt:
      a =[h]
      a=np.array(a)
      if shortest_route[0] != a[0]:
            z=shortest_route[0]
            shortest_route = np.delete(shortest_route,0)
            shortest_route= np.delete(shortest_route,-1)
            shortest_route[np.where(shortest_route==a[0])]=z
            b=list(a)
            c=list(shortest_route)
            s=b+c+b
            s=np.array(s)
            shortest_route=s
            
      pass
print("best route=>",(shortest_route), '\nwith found min distance=',shortest_dist)
    
        
