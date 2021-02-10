import numpy as np
import sys
from astropy.io import fits
import matplotlib.pyplot as plt
#A=list(np.loadtxt(str(sys.argv[1]),dtype=str))
with open("list.txt") as f:
        A = f.readlines()
f.close()
u=0

def bright(i,j,da,me):
    if (da[i][j]<me*4):
        return False
    else:
        tab=[]
        #tab=[da[i][j],da[i-1][j],da[i+][j],da[i][j+1],da[i][j-1],da[i-1][j-1],da[i+1][j+1],da[i-1][j+1],da[i+1][j-1]]
        for a in range(-2,1):
            for b in range(-2,1):
                tab.append(da[i+a][j+b])

        if (max(tab)-min(tab)>da[i][j]*0.1):
            return False
        else:
            return True

for nazwa in A:

    plik1=fits.open(nazwa[:-1])
    da=plik1[0].data
    plik1.close()
    wyn=[]
    me=np.median(da)
    print(me)
    for i in np.linspace(48,2000,977):
        for j in np.linspace(48,2000,977):
            if (bright(int(i),int(j),da,me)==True):
                    K=[str(i),str(j),str(da[int(i)][int(j)])]
                    wyn.append(K)
    plik=open(nazwa[:-5]+"txt","w")
    for c in range(0,len(wyn)):
        plik.write(wyn[c][0]+" "+wyn[c][1]+" "+wyn[c][2]+"\n")
    plik.close()
    u=u+1
