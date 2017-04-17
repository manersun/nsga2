#coding=utf-8
from function import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def min_Tc(Tn,DHEws):
    minTcInfo=[]
    minTcs = [0]*5
    minTc = 9999
    minIndex = 0
    minTc_DHEw = 0
    for i in range(0,len(DHEws)):
        sumTc, Tcs = gainTc(Tn, DHEws[i])
        if(sumTc<minTc and (Tcs[3]!=Tcs[4] or Tcs[3]==Tcs[4]==0)):
            for j in range(0, 5):
                minTcs[j] = Tcs[j]
            minTc = sumTc
            minIndex = i
            minTc_DHEw = DHEws[i]
    minTcInfo.append(minIndex)
    minTcInfo.append(minTc)
    minTcInfo.append(minTcs)
    minTcInfo.append(minTc_DHEw)
    return minTcInfo