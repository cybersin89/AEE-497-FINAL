# -*- coding: utf-8 -*-
"""
Created on Thu May 23 09:38:24 2019

@author: etemo_000
"""

def get_neighbor(i):
    a=[]
    j=0
    while j<81:
        if distance[i][j]<250.:
            a.append(j)
        j=j+1
    a=np.array(a)
    return a

def define_route():
    new_dist=[]
    dist=get_dist(p)
    for i in range(81):
        p[i+1]=np.random.rand(neighbor[i])
        new_dist.append(get_dist(p))
    for i in range(81):
        if new_dist[i]<dist:
            dist=new_dist[i]
            
            
                
                
     
    
#def get_better():
#    d=[]
#    d.append(get_dist())
#    k=1000
#    d.append(get_dist())
#    for i in range(k):
#        if d[1]>=d[0]:
#            d[1]=get_dist()
#        else:
#            d[0]=d[1]
#        k=k-1
#    return d

#def get_better():
#    count=0
#    while count==0:
#        for i in range(p)
#        plaka=np.delete(plaka,int(n-1))
#        l=list(plaka)
        
        

x,y,distance,plaka=coords_dists(xy,length)
p=path(plaka,h)
i=0
neighbor=[]
while i<81: 
    neighbor.append(get_neighbor(i))
    i=i+1
neighbor=np.array(neighbor)
#neighbor=get_neighbor(i)
#plt.xlim(35,44)
#plt.ylim(24,46)
#plt.plot(x,y,'o')
#print(p)
#print(dist)
#shortest_dist=get_better()
