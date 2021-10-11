# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 18:12:16 2021

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
    
fig2 = plt.figure("one",figsize=(6,6))
ax1 = fig2.add_subplot(1,1,1)

cmap = plt.cm.get_cmap("jet",5) #number of colors to show
colors = cmap(range(11))

n,bins,patches = ax1.hist(hometeamgoal,bins=range(11) )

for color,patch in zip(colors,patches):
    patch.set_facecolor(color)
    
plt.show()