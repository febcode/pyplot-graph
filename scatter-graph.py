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
#fig1 = plt.figure("onef",figsize=(8,8),facecolor="red")
fig2 = plt.figure("one",figsize=(18,18))

axList = []
for i in range(1,10):
    axList.append(fig2.add_subplot(3,3,i))

plt.figure("one")

plt.sca(axList[3])
plt.scatter(x =hometeamgoal, y = awayteamgoal ,s = 400 ,
            c =range(len(hometeamgoal)) , 
            marker ='*' ,alpha=1)

plt.sca(axList[1])
plt.scatter(x =hometeamgoal, y = awayteamgoal ,s = 400 ,
            c =range(len(hometeamgoal)) , 
            marker ='*' ,alpha=0.7)


plt.show()
