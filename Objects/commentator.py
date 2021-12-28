#! /usr/bin/python
# -*- coding: utf-8 -*-

import time, os, random

class Commentator():

    def __init__(self, allowed, name="COMMENTATOR", betting =True, chattiness= 3):
        self.__chattiness = chattiness
        self.allowed = allowed
        self.allowBetting = betting
        self.name = name
        self.spottingDict=dict()

    def commentDeath(self, bot):
        print(f'{self.name}: {bot} died')

    def commentSpotted(self, bot, target):
        if bot in self.spottingDict:
            if target in self.spottingDict[bot]:
                return
            print(f'{self.name}: {bot} spotted by {target}')
            self.spottingDict[bot].append(target)
            return
        self.spottingDict[bot] = [target]
        print(f'{self.name}: {bot} spotted by {target}')

    def commentHit(self, target, attacker, dmg):
        print(f'{self.name}: {target} was hit by {attacker} for {dmg} damage.')
