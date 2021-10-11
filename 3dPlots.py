# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:25:03 2021

@author: 91750
"""

import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

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
    

fig2 = plt.figure("one",figsize=(9,9))
ax1 = fig2.add_subplot(2,1,1,projection = "3d") #nrows n columns
ax2 = fig2.add_subplot(2,1,2,projection = "3d")



ax1.plot(xs = x,ys = hometeamgoal , zs = awayteamgoal )
ax1.set_xlabel("game number")
ax1.set_ylabel("home team")
ax1.set_zlabel("away team")
ax1.set_title("3d line plot")

ax2.scatter(xs = x,ys = hometeamgoal , zs = awayteamgoal ,s = 20 , 
            depthshade = True , c= "red")
ax2.set_xlabel("game number")
ax2.set_ylabel("home team")
ax2.set_zlabel("away team")
ax2.set_title("3d scatter plot")

ax2.view_init(30,45) #elevation and rotation angle

for angle in range(0,360):
    ax2.view_init(30,angle)
    plt.draw()
    plt.pause(0.01)

plt.show()

