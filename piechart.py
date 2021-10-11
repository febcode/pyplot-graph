# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:16:55 2021

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
    
totalHTG = sum(hometeamgoal)
totalATG = sum(awayteamgoal)

#fig1 = plt.figure("onef",figsize=(8,8),facecolor="red")
fig2 = plt.figure("one",figsize=(6,6))
ax1 = fig2.add_subplot(1,1,1)

ax1.pie(x = [totalHTG,totalATG] , labels = ["HTG","ATG"] ,
        labeldistance = 0.2 , colors =["pink","green"] , 
        explode = [0,0.2] , shadow = True, radius = 0.75)
# ax1.pie(x = [0.3,0.4,0.5, 1] , labels = ["HTG","ATG","test","test1"])

plt.show()
