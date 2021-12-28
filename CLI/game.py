# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

import os, pickle


from graph_cli import Graph
from robot import Robot
from statistic import statistic


class MainWindow():
    """
    Class documentation goes here.
    """

    def __init__(self):
        """
        Constructor
        """
        width = 500
        height = 500
        self.field = Graph(width, height)
        self.countBattle = 0
        self.listBots = {}
        botFiles = os.listdir(os.getcwd() + "/Robots")
        for botFile in botFiles:
            if botFile.endswith('.py'):
                botName = botPath = botFile[:botFile.rfind('.')]
                botnames = []
                if botName not in botnames:
                    botnames.append(botName)
                    try:
                        botModule = __import__(botPath)
                        for name in dir(botModule):
                            if getattr(botModule, name) in Robot.__subclasses__():
                                someBot = getattr(botModule, name)
                                bot = someBot
                                self.listBots[str(bot).replace("<class '", "").replace("'>", "")] = bot
                                break
                    except Exception as e:
                        print("Problem with bot file '{}': {}".format(botFile, str(e)))

        alive_robots= []
        temp_dict = {}
        for i,key in enumerate(self.listBots.keys()):
            temp_dict[i+1]=key
        for key, value in temp_dict.items():
            print(f'[{key}] {value.split(".")[1]}')

        ctr = 1
        while True:
            robot_nr = input(f"Select robot {ctr}: ")
            if robot_nr=="-1" and ctr>2:
                break
            elif str.isdigit(robot_nr):
                alive_robots.append(temp_dict[int(robot_nr)])
                ctr+=1
            else:
                continue
            if ctr>2:
                print(f'Selected robot(s): {alive_robots}. Press -1 to stop adding')
            elif ctr==2:
                print(f'Selected robot: {alive_robots}')

        bots=[]
        for bot in alive_robots:
            bots.append(self.listBots[bot])
        self.setUpBattle(bots)


    def setUpBattle(self, botList):
        self.statisticDico = {}
        for bot in botList:
            self.statisticDico[self.repres(bot)] = statistic()
        self.startBattle(botList)

    def startBattle(self, botList):
        self.countBattle += 1
        self.field.AddRobots(botList)

    def repres(self, bot):
        repres = repr(bot).split(".")
        return repres[1].replace("'>", "")