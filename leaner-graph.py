# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 16:07:15 2021

@author: 91750
"""

import matplotlib.pyplot as plt 

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
fig2 = plt.figure("one",figsize=(15,15))
ax1 = fig2.add_subplot(2,1,1)
ax2 = fig2.add_subplot(2,1,2)
ax1.plot(x,hometeamgoal,color=(1,0,.5),marker="^",markerfacecolor="black",
         markersize=5, linestyle=":",linewidth=5)
ax1.set_xlim(0,11)
ax1.set_ylim(0,11)
ax1.set_xlabel("homex")
ax1.set_ylabel("homey")

ax1.set_title(r"Home team goal", loc = "center",
              fontdict={"fontsize":20,"color":"red"})
ax2 .plot(x,awayteamgoal,color="green",marker="*",markerfacecolor="black",
         markersize=5, linestyle=":",linewidth=5)
ax2.set_xlim(0,11)
ax2.set_ylim(0,11)
ax1.set_xlabel("homex")
ax1.set_ylabel("homey")
ax2.set_title("away team goal", loc = "center" ,
              fontdict={"fontsize":20,"color":"green" ,"rotation":45})
ax2.set_xlabel("awayx")
ax2.set_ylabel("awayy")


plt.show()
