# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 16:07:15 2021

@author: 91750
"""

import matplotlib.pyplot as plt 
print(plt.style.available)
plt.style.use("bmh")
from matplotlib.ticker import MultipleLocator,FormatStrFormatter

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
    
    
majortickLocator = MultipleLocator(2)
minorjortickLocator = MultipleLocator(1)
majortickformator = FormatStrFormatter("0%3d")


#fig1 = plt.figure("onef",figsize=(8,8),facecolor="red")
fig2 = plt.figure("one",figsize=(15,15))
ax1 = fig2.add_subplot(2,1,1)

ax1.plot(x,hometeamgoal,color=(1,0,.5),marker="^",markerfacecolor="black",
         markersize=15, linestyle=":",linewidth=5 , label="HTG")
ax1.set_xlim(0,15)
ax1.set_ylim(0,15)
ax1.set_xlabel("homex")
ax1.set_ylabel("homey")
ax1.xaxis.set_major_locator(majortickLocator)
ax1.xaxis.set_minor_locator(minorjortickLocator)
ax1.xaxis.set_major_formatter(majortickformator)

xticklable = ax1.get_xticks().tolist()
xticklable[3] = "four"
ax1.set_xticklabels(xticklable)


ax1.set_title("Home team goal", loc = "center",
              fontdict={"fontsize":20,"color":"red"})
plt.yticks([2,4,6],['two','four','six'])
ax1.legend(loc ="upper center")
#left right center upper lower best
ax1.text(x=5, y= 6 , s="test text")
ax1.text(1, 3 , s="test text2") #use allignement, rotation , style , 
#weight with it 

ax1.spines["right"].set_visible(False)
ax1.yaxis.set_ticks_position("left")

plt.savefig("images\savetest.png",orientation= "portrait",dpi = 100
            ) #portrait/landscape
plt.show()
