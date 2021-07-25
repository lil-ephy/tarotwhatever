import random
from deck import deckPls
from roman import toRoman

"""
############################## TAROT APP ##############################
#  1) Need to make random number generator and iterate over rng func  #
#     to create list of random numbers                                #
#  2) Use list to select arcana, suit, card, and orientation          #
#  3) Need to add spreads such as three card, five card and the       #
#     Celtic cross                                                    #
#######################################################################
"""


def randPls(x, y, z):
    if z == 1:
        return random.randint(x, y)
    else:
        return random.sample(range(x, y), z)

def newAttr(self, attr):
            setattr(self, attr, attr)

class cardPls:
    def __init__(self, arcana, suit, upright):
        self.marseille = False
        self.arcana = bool(arcana)
        self.suit = suit
        self.upright = bool(upright)
        self.numb = randPls(0, 21 if self.arcana else 13, 1)

    def setMarseille(self, x=False):
        self.marseille = x
        return self

    def getCardPls(self):
        
        self.major_arcana = deckPls('major_arcana', self.marseille)
        card = {}
        suit_names = ["Cups", "Pentacles", "Swords", "Wands"] if self.marseille == False else ["Coupes", "Deniers", "Épées", "Bâtons"]
        face_names = ["Page", "Knight", "Queen", "King"] if self.marseille == False else ['Valet', 'Cavalier', 'Dame', 'Roi']
        
        if self.arcana:
            card["Arcana"] = "Major"
            x = randPls(0, 21, 1)
            card["Name"] = self.major_arcana[x]
            card["Suit"] = f"{toRoman(x) if x > 0 else '0'}"
        else:
            card["Arcana"] = "Minor"
            card["Suit"] = suit_names[self.suit]
            if self.numb >= 1 and self.numb < 10:
                card["Name"] = f"{self.numb+1} of {card['Suit']}"
            elif self.numb < 1:
                 card["Name"] = f"Ace of {card['Suit']}"
            elif self.numb >=10:
                card["Name"] = f"{face_names[self.numb-10]} of {card['Suit']}"

        # need to check if card >= 10 then set name to page, knight, queen, king based on index

        card["Orientation"] = "Upright" if self.upright else "Reversed"
        
        return card


cardPls(*(1,2,1)).getCardPls()


standard = cardPls(*(randPls(0, 1, 1), randPls(0, 3, 1), randPls(0, 1, 1))).getCardPls()
de_marseille = cardPls(*(randPls(0, 1, 1), randPls(0, 3, 1), randPls(0, 1, 1))).setMarseille(True).getCardPls()

print(", ".join(f"{key}: {value}" for key, value in de_marseille.items()))


