#! /usr/bin/python
# -*- coding: utf-8 -*-

from robot import Robot  # Import a base Robot
import math


class RoboTron(Robot):  # Create a Robot

    def init(self):  # To initialyse your robot

        # Set the bot color in RGB
        self.setColor(36, 242, 225)
        self.setGunColor(110, 255, 175)
        self.setRadarColor(250, 255, 110)
        self.setBulletsColor(255, 0, 0)

        self.radarVisible(True)  # if True the radar field is visible

        # get the map size
        size = self.getMapSize()

        self.lockRadar("gun")

        # Et radariga märgata esimene vastane.
        self.setRadarField("round")
        self.lastX = None
        self.lastY = None

    def run(self):  # main loop to command the bot

        self.move(10)
        self.gunTurn(15)
        self.turn(3)
        self.setRadarField("normal")

    def onHitWall(self):
        self.turn(60)
        self.move(20)

    def sensors(self):
        pass

    def onRobotHit(self, robotId, robotName):  # when My bot hit another
        self.move(-2)
        self.move(5)

    def onHitByRobot(self, robotId, robotName):
        self.move(40)

    def onHitByBullet(self, bulletBotId, bulletBotName, bulletPower):  # NECESARY FOR THE GAME
        self.move(20)

    def onBulletHit(self, botId, bulletId):  # NECESARY FOR THE GAME
        pass

    def onBulletMiss(self, bulletId):
        #Kui mööda laseme, siis suurendame radari vaatevälja, et rohkem roboteid näha.
        self.setRadarField('large')

    def onRobotDeath(self):
        pass

    def onTargetSpotted(self, botId, botName, botPos):  # NECESARY FOR THE GAME
        #Proovitud on implementeerida lineaarset tulistamist, et eeldatakse, et vastane liigub samas suunas.
        #Pythonis raskem implementeerida, kuna siin on ainult vastase asukoht olemas.
        #Javas on olemas ka vastase liikumissuund ja kiirus mille abil on seda palju lihtsam teha.
        self.setRadarField('normal')
        pos = self.getPosition()
        if self.lastX == None or self.lastY == None or -10 > self.lastX - botPos.x() > 10 or -10 > self.lastY - botPos.y() > 10 or (
                self.lastX == botPos.x() and self.lastY == botPos.y()):
            dx = botPos.x() - pos.x()
            dy = botPos.y() - pos.y()
        else:  # Võtame arvesse viimase asukoha.
            dx = (botPos.x() - self.lastX)*(18*abs(botPos.x() - pos.x())/self.getMapSize().width()) + botPos.x() - pos.x()
            dy = (botPos.y() - self.lastY)*(18*abs(botPos.y() - pos.y())/self.getMapSize().height()) + botPos.y() - pos.y()
        a = self.getEnemyAngle(dx, dy)

        self.gunTurn(a)
        self.fire(1)
        self.lastX = botPos.x()
        self.lastY = botPos.y()

    def getEnemyAngle(self, dx, dy):
        # Võetud track_target.py robotilt.
        my_gun_angle = self.getGunHeading() % 360
        enemy_angle = math.degrees(math.atan2(dy, dx)) - 90
        a = enemy_angle - my_gun_angle
        if a < -180:
            a += 360
        elif 180 < a:
            a -= 360
        return a
