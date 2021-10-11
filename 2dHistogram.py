# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 17:04:40 2021

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
    

fig2 = plt.figure("one",figsize=(6,6))
ax1 = fig2.add_subplot(1,1,1)

# ax1.hist2d(x = hometeamgoal , y = awayteamgoal ,
#         bins = [range(9),range(6)])

counts, xedges, yedges, Image = ax1.hist2d(x = hometeamgoal , y = awayteamgoal ,
        bins = [range(8),range(7)],
        cmap = plt.cm.jet)


extent = [xedges[0],xedges[-1],yedges[-1],yedges[0]]
im = ax1.imshow(counts ,extent = extent )
fig2.colorbar(im,ax=ax1)

#           OR
# plt.hist2d(x = hometeamgoal , y = awayteamgoal ,
#         #bins = [range(8),range(7)] ,
#         cmap = plt.cm.jet_r) #ocean,hot _r for reverse 
#plt.colorbar()


plt.show()

