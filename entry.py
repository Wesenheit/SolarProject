import numpy as np
import sys
from astropy.io import fits
import matplotlib.pyplot as plt
#A=list(np.loadtxt(str(sys.argv[1]),dtype=str))
with open("list.txt") as f:
        A = f.readlines()
f.close()
u=0

def bright(i,j,da):
    if (da[i][j]<500):
        return False
    else:
        tab=[]
        #tab=[da[i][j],da[i-1][j],da[i+][j],da[i][j+1],da[i][j-1],da[i-1][j-1],da[i+1][j+1],da[i-1][j+1],da[i+1][j-1]]
        for a in range(-3,2):
            for b in range(-3,2):
                tab.append(da[i+a][i+b])

        if (max(tab)-min(tab)>100):
            return False
        else:
            return True

for nazwa in A:

    plik1=fits.open(nazwa[:-1])
    da=plik1[0].data
    plik1.close()
    wyn=[]
    for i in np.linspace(0,2048,513):
        for j in np.linspace(0,2048,513):
            if (bright(i,j,da)==True):
                    K=[str(i),str(j)]
                    wyn.append(K)
    plik=open(str(sys.argv[2])+str(u)+".txt","w")
    for c in range(0,len(wyn)):
        plik.write(wyn[c][0]+" "+wyn[c][1]+"\n")
    plik.close()
    u=u+1
