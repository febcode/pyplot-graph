# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 16:07:15 2021

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

n,bins,patches = ax1.hist(x=(hometeamgoal,awayteamgoal),bins=range(11),
         color=("red","blue"),cumulative=False )

print(n)
print(n[0][3])
patches[1][2].set_facecolor("orange")

redRectangle = Rectangle((0,0), 1, 1 ,color="red")
blueRectangle = Rectangle((0,0), 1, 1 ,color="blue")
boxes = [redRectangle,blueRectangle]
labels = ['htg','atg']
plt.legend(boxes,labels)
#plt.savefig("images\savetest.png",orientation= "portrait",dpi = 100) 
#portrait/landscape
plt.show()
