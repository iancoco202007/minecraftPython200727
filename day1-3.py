# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:11:10 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()


x = 1000.9999999999999999
y = 1000.1
z = 10000.9999999999999999
mc.player.setPos(x,y,z)