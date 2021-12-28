#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import math

from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QColor, QPainter


class Bullet():

    def __init__(self, power, bot):

        self.isfired = False
        # physics
        if power <= 0.5:
            power = 0.5
        elif power >= 10:
            power = 10
        self.power = power
        bsize = power
        if power < 3:
            bsize = 4
        self.pixmap = self.pixmap.scaled(bsize, bsize)
        self.robot = bot

    def init(self, pos, angle, scene):

        self.angle = angle
        self.setPos(pos)
        self.scene = scene
        self.isfired = True


    def advance(self):
        if self.isfired:
            pos = self.pos()
            x = pos['X']
            y = pos['Y']
            dx = - math.sin(math.radians(self.angle)) * 10.0
            dy = math.cos(math.radians(self.angle)) * 10.0
            self.setPos(x + dx, y + dy)
            if x < 0 or y < 0 or x > self.scene.width or y > self.scene.height:
                self.robot.onBulletMiss(id(self))
                self.scene.removeItem(self)
                self.robot.removeMyProtectedItem(self)

    def pos(self):
        return {'X': self.x, 'Y': self.y}

    def setPos(self, new_x, new_y):
        self.x = new_x
        self.y = new_y









