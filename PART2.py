# -*- coding: utf-8 -*-
"""
Created on Thu May 23 09:37:11 2019

@author: etemo_000
"""

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