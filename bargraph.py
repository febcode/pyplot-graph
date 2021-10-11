# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 12:49:49 2021

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
    

avgHTL = sum(hometeamgoal)/len(hometeamgoal)
avgATL = sum(awayteamgoal)/len(awayteamgoal)

#fig1 = plt.figure("onef",figsize=(8,8),facecolor="red")
fig2 = plt.figure("one",figsize=(6,6))
ax1 = fig2.add_subplot(1,1,1)

# ax1.bar(x = [1,2] , height=[avgHTL,avgATL] , width=0.35 ,align="center" ,
#         color=["red","black"],
#         bottom = [0.1,0.3])

ax1.bar(x = [1,1] , height=[avgHTL,avgATL] , width=0.35 ,align="center" ,
        color=["red","black"],
        bottom = [0 , avgHTL] , xerr=[[0.2,0.3],[0.4,0.1]],
        yerr=[[0.2,0.3],[0.4,0.1]] , ecolor = ["blue","orange"])
plt.xticks([1,2],["home team","away team"])
ax1.set_ylim(0,15)
ax1.set_xlim(0,6)

plt.show()
