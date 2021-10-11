# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:05:21 2021

@author: 91750
"""

import matplotlib.pyplot as plt 
from matplotlib.patches import Rectangle

with open("testdata1.txt","r") as goaldata:
    hometeamline = goaldata.readline()
    hometeamline = hometeamline.strip(" /n")
    hometeamline = hometeamline.split()
    hometeamgoal = [int(x) for x in hometeamline]
    
    awayteamline = goaldata.readline()
    awayteamline = awayteamline.strip(" /n")
    awayteamline = awayteamline.split()
    awayteamgoal = [int(x) for x in awayteamline]

print(hometeamgoal)

x = []
for i in range(1,len(hometeamgoal)+1):
    x.append(i)
    

#fig1 = plt.figure("onef",figsize=(8,8),facecolor="red")
fig2 = plt.figure("one",figsize=(6,6))
ax1 = fig2.add_subplot(1,1,1)

ax1.boxplot(x = [hometeamgoal,awayteamgoal] , 
            # positions=[0.5,5],
            sym = "+" , notch = True)

plt.show()
