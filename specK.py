import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
with open("list.txt") as f:
    A = f.readlines()
f.close()
radius=10 #in pix
c=0
for nazwa in A:
    file="spectro_obspm_fullprofile_Cak_3D_"+nazwa[18:]
    dat=fits.open(file[:-1])
    da=dat[0].data
    dat.close()
    print(len(da[:,1,3]))
    bright_spots=np.loadtxt("spectro_obspm_Cak_"+nazwa[18:-5]+"txt")
    regions=[]
    avable=[]
    for i in range(0,len(bright_spots)):
        avable.append(i)
    while (len(avable)>0):
        u=[avable[0]]
        x=bright_spots[avable[0]][0]
        y=bright_spots[avable[0]][1] 
        flag=0
        del avable[0]
        while(flag==0):    
            flag=1
            #x=bright_spots[avable[0]][0]
            #y=bright_spots[avable[0]][1]
            for i in range(0,len(avable)):
                if ((x-bright_spots[avable[i]][0])**2+(y-bright_spots[avable[i]][1])**2<radius**2):
                        u.append(avable[i])
                        del avable[i]
                        flag=0
                        break
            x=bright_spots[u[-1]][0]
            y=bright_spots[u[-1]][1]
            if (flag==1):
                regions.append(u)
    print(regions)
    u=0
    for reg in regions:
        if (len(reg)>2):
            spec=np.zeros(94)
            for i in range(0,len(reg)):
                spec=spec+da[:,int(bright_spots[reg[i]][0]),int(bright_spots[reg[i]][1])]
            plt.plot(np.linspace(0,94,94),spec/len(reg))
            plt.savefig("plot"+str(u)+str(c)+".png")
            plt.close()
            u=u+1
    c=c+1
