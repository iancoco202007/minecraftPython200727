# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:33:22 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
x = 60
y = 120
z = 200

mc.player.setTilePos(x,y,z)
time.sleep(4)

x = x + 20 #x=590+30=70
mc.player.setTilePos(x,y,z)
time.sleep

x = x + 20 
mc.player.setTilePos(x,y,z)