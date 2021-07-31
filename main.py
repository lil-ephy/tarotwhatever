import random
import sys
import os
from roman import toRoman
from deck import *
from rich import print as rprint

class tarotPls:
    def __init__(self, marseille=False):
        random.seed(os.urandom(16))
        self.marseille = marseille
        self.arcana = bool(random.randint(0,1))
        self.orientation = bool(random.randint(0,1))
        self.position = random.randint(0,21) if self.arcana == True else random.randint(0,13)
        self.suit = None if self.arcana == True else random.randint(0,3)

    def genPls(self, cards):
        for i in range(cards):
            x = tarotPls(self.marseille).__dict__
            yield x
    
    def cardPls(self, cards=1):
        y = []
        for i in self.genPls(cards):
            x = {}
            # print(", ".join(f"{k}: {v}" for k, v in i.items())) # pretty prints original dict
            x['orientation'] = "upright" if i['orientation'] else "reversed"
            if i['arcana']:
                # x['position'] = f"{toRoman(i['position'])}" if i['position'] > 0 else '0'
                x['position'] = f"{i['position']}"
                x['card'] = f"{arcanaGen(self.marseille)[i['position']]}"
            else: 
                if i['position'] > 9:
                    x['position'] = f"{cardGen(True, self.marseille)[i['position']-10]}"
                    x['suit'] = f"{cardGen(False, self.marseille)[i.get('suit')]}"
                else:
                    # x['position'] = f"{toRoman(i['position'])}" if i['position'] > 0 else "Ace" # add roman numbers to pip cards
                    x['position'] = f"{i['position']}" if i['position'] > 0 else "Ace"
                    x['suit'] = f"{cardGen(False, self.marseille)[i.get('suit')]}"

            y.append(x)
        return y
    
    def valuesPls(self, cards=1):
        x = []
        for each in tarotPls(self.marseille).cardPls(cards):
            x.append(list(v for k,v in each.items()))
        return x

for each in tarotPls(False).valuesPls(10):
    a = 'an' if each[0] == 'upright' else 'a'
    # rprint(f"You have drawn {a} [bold magenta]{each[0]}[/bold magenta]: {each[1]}")
    print(each)

def tests():
    print('\n################################################################################################################\n')
    # prints cards individually
    for i in tarotPls().cardPls(10):
        print(i)
    # print('\n################################################################################################################\n')
    # print(tarotPls().cardPls(1))
    print('\n################################################################################################################\n')
    # prints cards as list
    print(tarotPls().cardPls(10))
    print('\n################################################################################################################\n')
