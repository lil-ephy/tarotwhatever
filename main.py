import random
import sys
import os
from roman import toRoman
from deck import *

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
            x = tarotPls().__dict__
            yield x
    
    def cardPls(self, cards=1):
        y = []
        for i in self.genPls(cards):
            x = {}
            # print(", ".join(f"{k}: {v}" for k, v in i.items())) # pretty prints original dict
            x['orientation'] = "Upright" if i['orientation'] else "Reversed"
            if i['arcana']:
                x['card'] = f"{arcanaGen(False)[i['position']]}"
                x['position'] = f"{toRoman(i['position'])}" if i['position'] > 0 else '0'
            else: 
                if i['position'] > 9:
                    x['card'] = f"{cardGen(True)[i['position']-10]} of {cardGen(False)[i.get('suit')]}"
                else:
                    x['card'] = f"{i['position']} of {cardGen(False)[i.get('suit')]}" if i['position'] != 0 else f"Ace of {cardGen(False)[i.get('suit')]}"
                    # x['position'] = f"{toRoman(i['position'])}" # add roman numbers to pip cards
            y.append(x)
        return y

print(tarotPls().cardPls(1))

def tests():
    # prints cards individually
    for i in tarotPls().cardPls(10):
        print(i)

    print('\n################################################################################################################\n')

    # prints cards as list
    print(tarotPls().cardPls(10))

# tests()