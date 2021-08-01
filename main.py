import random
import sys
import os
import datetime
from roman import toRoman
from deck import *
from rich import print


class tarotPls:
    def __init__(self, marseille=False):
        random.seed(os.urandom(16))
        self.marseille = marseille
        self.arcana = bool(random.randint(0, 1))
        self.orientation = bool(random.randint(0, 1))
        self.position = (
            random.randint(0, 21) if self.arcana == True else random.randint(0, 13)
        )
        self.suit = None if self.arcana == True else random.randint(0, 3)

    def genPls(self, cards):
        for x in range(cards):
            x = tarotPls(self.marseille).__dict__
            yield x

    def cardPls(self, cards=1):
        y = []
        for i in self.genPls(cards):
            x = {}
            # print(", ".join(f"{k}: {v}" for k, v in i.items())) # pretty prints original dict
            x["orientation"] = "upright" if i["orientation"] else "reversed"
            x["arcana"] = "major" if i["arcana"] == True else "minor"
            if i["arcana"]:
                # x['position'] = f"{toRoman(i['position'])}" if i['position'] > 0 else '0'
                x["position"] = f"{i['position']}"
                x["card"] = f"{arcanaGen(self.marseille)[i['position']]}"
            else:
                if i["position"] > 9:
                    x["position"] = f"{cardGen(True, self.marseille)[i['position']-10]}"
                    x["suit"] = f"{cardGen(False, self.marseille)[i.get('suit')]}"
                elif 9 > i["position"] > 0:
                    # x['position'] = f"{toRoman(i['position'])}" if i['position'] > 0 else "Ace" # add roman numbers to pip cards
                    x["position"] = f"{i['position']+1}"
                    x["suit"] = f"{cardGen(False, self.marseille)[i.get('suit')]}"
                else:
                    x["position"] = "Ace"
                    x["suit"] = f"{cardGen(False, self.marseille)[i.get('suit')]}"
            y.append(x)
        return y

    def valuesPls(self, cards=1):
        x = []
        for each in tarotPls(self.marseille).cardPls(cards):
            x.append(list(v for k, v in each.items()))
        return x


class spreadPls(object):
    def __init__(self):
        pass

    def __new__(cls, quantity):
        return tarotPls().valuesPls(quantity)


def readingPls():
    x = f"{datetime.datetime.utcnow():%Y-%m-%d-%T}"
    with open(f'{x.replace(":","")}.txt', "w+") as file:
        for each in spreadPls(10):
            file.writelines(f"{each}\n")

