import random
from collections import OrderedDict

"""
############################## TAROT APP ##############################
#  1) need to make random number generator and iterate over rng func  #
#     to create list of random numbers                                #
#  2) use list to select arcana, suit, card, and orientation          #
#######################################################################
"""


def randPls(x, y, z):
    if z == 1:
        return random.randint(x, y)
    else:
        return random.sample(range(x, y), z)


class cardPls:
    def __init__(self, arcana, suit, pos):
        self.major_arcana = [
            "The Fool",
            "The Magician",
            "The High Priestess",
            "The Empress",
            "The Emperor",
            "The Hierophant",
            "The Lovers",
            "The Chariot",
            "Strength",
            "The Hermit",
            "Wheel of Fortune",
            "Justice",
            "The Hanged Man",
            "Death",
            "Temperance",
            "The Devil",
            "The Tower",
            "The Star",
            "The Moon",
            "The Sun",
            "Judgment",
            "The World",
        ]
        self.arcana = arcana
        self.suit = suit
        self.pos = pos

        if self.arcana == True:
            self.numb = randPls(0, 21, 1)
        else:
            self.numb = randPls(0, 13, 1)

    def write_roman(self, num):
        roman = OrderedDict()
        roman[1000] = "M"
        roman[900] = "CM"
        roman[500] = "D"
        roman[400] = "CD"
        roman[100] = "C"
        roman[90] = "XC"
        roman[50] = "L"
        roman[40] = "XL"
        roman[10] = "X"
        roman[9] = "IX"
        roman[5] = "V"
        roman[4] = "IV"
        roman[1] = "I"

        def roman_num(num):
            for r in roman.keys():
                x, y = divmod(num, r)
                yield roman[r] * x
                num -= r * x
                if num <= 0:
                    break

        return "".join([a for a in roman_num(num)])

    def getCardPls(self):
        card = {}
        # print(len(self.major_arcana))
        # print(self.numb)
        if self.arcana == 1:
            card["arcana"] = "Major"
            x = randPls(0, 21, 1)
            card["name"] = self.major_arcana[x]
            card["suit"] = f"{self.write_roman(x+1)}"
        else:
            card["arcana"] = "Minor"
            if self.suit == 0:
                card["suit"] = "Cups"
            elif self.suit == 1:
                card["suit"] = "Pentacles"
            elif self.suit == 2:
                card["suit"] = "Swords"
            elif self.suit == 3:
                card["suit"] = "Wands"
            if self.numb >= 1:
                card["name"] = f"{self.numb+1} of {card['suit']}"
            elif self.numb < 1:
                card["name"] = f"Ace of {card['suit']}"
            # card['name'] =
        if self.pos == True:
            card["pos"] = "Upright"
        else:
            card["pos"] = "Reversed"
        return card


a = cardPls(randPls(0, 1, 1), randPls(0, 3, 1), randPls(0, 1, 1)).getCardPls()
print(", ".join("%s: %s" % item for item in a.items()))

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
