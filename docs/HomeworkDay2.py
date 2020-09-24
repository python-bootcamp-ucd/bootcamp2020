#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = 'StateYlyTempAndLocData.csv'
raw = []
fid = open(filename,'r')
hdr = fid.readline()
for i in fid:
    splitted = i.split(',')
    tmp = [splitted[0]]
    for j in splitted[1:]:
        try:
            tmp.append(float(j))
        except:
            print(tmp[0])
    raw.append(tmp)


StateData = []
for i in raw:
    tmp = i[:3]
    last10 = np.mean(np.array(i[3:13]))
    first10 = np.mean(np.array(i[-10:]))
    difference = last10-first10
    tmp.append(difference)
    StateData.append(tmp)
StateData



lats = []
lons = []
stateNames = []
TempDiff = []
for i in StateData:
    lats.append(float(i[1]))
    lons.append(-1*float(i[2]))
    stateNames.append(i[0])
    TempDiff.append(i[3])
#TempDiff = np.array(TempDiff)-np.min(TempDiff)
#TempDiff = TempDiff/np.max(TempDiff)




plt.figure()
plt.scatter(lons,lats,c=TempDiff,cmap='seismic')
plt.ylabel(hdr[1])
plt.xlabel(hdr[2])
plt.title('Temperature difference between mean of last 10 years and earliest 10 years')
plt.colorbar()
plt.show()



test = [1,2,3,4,5,6]
count = 0
index = 0
for i in test:
    if i == 3:
        index = count
        break
    else:
        count += 1
print(index)


TmpTemperature = temp[3:13]
Temp = []
for i in TmpTemperature:
    if i != '':
        Temp.append(float(i))



