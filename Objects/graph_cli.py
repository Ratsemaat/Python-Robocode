#! /usr/bin/python
# -*- coding: utf-8 -*-

import time, os, random



from robot import Robot


class Graph():

    def __init__(self,  width, height):
        self.width = width
        self.height = height
        self.grid = self.getGrid()



    def AddRobots(self, botList):

        """
        """
        self.aliveBots = []
        self.deadBots = []
        try:
            posList = random.sample(self.grid, len(botList))
            for bot in botList:
                try:
                    robot = bot(self.width, self, str(bot))
                    self.aliveBots.append(robot)
                    robot.setPos(posList.pop())
                except Exception as e:
                    print("Problem with bot file '{}': {}".format(bot, str(e)))
            print(self.aliveBots)
        except ValueError:
            raise Exception("Too many Bots for the map's size!")
        except AttributeError:
            pass

    def battleFinished(self):
        print("battle terminated")
        try:
            self.deadBots.append(self.aliveBots[0])
            self.removeItem(self.aliveBots[0])
        except IndexError:
            pass
        j = len(self.deadBots)

        for i in range(j):
            print("N° {}:{}".format(j - i, self.deadBots[i]))
            if j - i == 1:  # first place
                self.Parent.statisticDico[repr(self.deadBots[i])].first += 1
            if j - i == 2:  # 2nd place
                self.Parent.statisticDico[repr(self.deadBots[i])].second += 1
            if j - i == 3:  # 3rd place
                self.Parent.statisticDico[repr(self.deadBots[i])].third += 1

            self.Parent.statisticDico[repr(self.deadBots[i])].points += i

        self.Parent.chooseAction()

    def getGrid(self):
        w = int(self.width / 80)
        h = int(self.height / 80)
        l = []
        for i in range(w):
            for j in range(h):
                l.append((i * 80, j * 80))
        return l

