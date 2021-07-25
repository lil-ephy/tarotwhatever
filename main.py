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
    
    def setMarseille(self, x=False):
        self.marseille = x
        return self
    
    def __init__(self, arcana, suit, upright):
        self.major_arcana = deckPls('major_arcana')
        self.arcana = bool(arcana)
        self.suit = suit
        self.upright = bool(upright)
        self.marseille = False
        # def test():
            #list(x) = i for i in list(locals().keys()) if i != 'self'
            # print(dict(locals()))
            # k = (k for k in locals().keys() if k != 'self')
            # for each in k: 
            #     self.newAttr(each)
            #     print(each)
            #   newAttr(k for k in locals())
            
            # print(locals())
            # x = list(filter(lambda x:x != 'self', locals().keys()))
            # self.x = x for i in list(x)
            # print(x)
            # print(self.__dict__)
            # print(self.__dict__.keys())
            # for i in x:
            #     self.__setattr__(i,self.__dir__)
            # print(self.__dict__)
                # self.__dict__ = i.__dict__.copy()
            # x = ['arcana', 'suit', 'pos']
            # for i in list(itslocals().keys()):
            #     # self.i = i if i != 'self' else print('SELF!!')
            # self.arcana = self.suit = self.pos = index_
        self.numb = randPls(0, 21 if self.arcana else 13, 1)

    def getCardPls(self):
        card = {}
        
        suit_names = ["Cups", "Pentacles", "Swords", "Wands"] if self.marseille == False else ["Coupes", "Deniers", "Épées", "Bâtons"]
        face_names = ["Page", "Knight", "Queen", "King"] if self.marseille == False else ['Valet', 'Cavalier', 'Dame', 'Roi']
        # face vs pip cards
        
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

standard = cardPls(*(randPls(0, 1, 1), randPls(0, 3, 1), randPls(0, 1, 1))).getCardPls()
de_marseille = cardPls(*(randPls(0, 1, 1), randPls(0, 3, 1), randPls(0, 1, 1))).setMarseille(True).getCardPls()

print(", ".join(f"{key}: {value}" for key, value in de_marseille.items()))

# a = cardPls(randPls(0, 1, 1), randPls(0, 3, 1), randPls(0, 1, 1)).getCardPls()
# print(", ".join(f"{key}: {value}" for key, value in a.items()))

# def mainTest():
    # for i in a.items():
    #     print(i)
    # attrs = vars(a)
    # print(attrs)
    # for i in attrs.items():
    #     print(i)
    # print(item for item in attrs.items())
    # print(', '.join("%s: %s" % item for item in attrs.items()))
    # print(dir(a))
    # attributes = [attr for attr in dir(a)
    #               if not attr.startswith('__')]
    # print(attributes)
    # print(cardPls.getCardPls())
