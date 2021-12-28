#! /usr/bin/python
# -*- coding: utf-8 -*-

import time, os, random

from robot import Robot


class Commentator():

    def __init__(self, allowed, window, name="COMMENTATOR", betting=True, chattiness=3):
        self.__chattiness = chattiness
        self.window = window
        self.allowed = allowed
        self.allowBetting = betting
        self.name = name
        self.spottingDict = dict()

    def commentHealth(self):
        print(f'{self.name}: Current status:')
        for item in self.window.getScene().items():
            if isinstance(item, Robot) and item.getHealth() > 0:
                print(f'{item} health: {item.getHealth()}')

    def commentDeath(self, bot):
        print(f'{self.name}: {bot} died')
        self.commentHealth()

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

    def initBetting(self):
        robs=[]
        for item in self.window.getScene().items():
            if isinstance(item, Robot):
                robs.append(item)
        for i, rob in enumerate(robs):
            print(f"[{i}] {rob}")
        bet = input("Place your bets: ")

    def resolveBetting(self):
        print(self.window)
