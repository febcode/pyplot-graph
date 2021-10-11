# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 17:57:36 2021

@author: 91750
"""

import matplotlib.pyplot as plt 
import matplotlib.image as mpimg


fig2 = plt.figure("one",figsize=(6,6))
ax1 = fig2.add_subplot(1,1,1)


img = mpimg.imread("Target.png")
ax1.imshow(img)

plt.show()
