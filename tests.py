from main import *
from cards import *

def testAscii():
    for k,v in majorAscii().items():
        print(v)

def printRaw(quantity):
    print(*(tarotPls().valuesPls(quantity)))  # PRETTY PRINT UNPACKED LIST
    print(tarotPls().valuesPls(quantity))  # PRETTY PRINT NESTED LIST


def printNice(quantity):
    for each in tarotPls().valuesPls(quantity):
        a = "an" if each[0] == "upright" else "a"
        if each[1] == "minor":
            print(
                f"You have drawn {a} [blue]{each[0]}[/blue]: [bold blue]{each[2]}[/bold blue] of [bold blue]{each[3]}[/bold blue]"
            )
        else:
            print(
                f"You have drawn {a} [blue]{each[0]}[/blue]: [bold blue]{each[3]}[/bold blue] [italic yellow]({toRoman(int(each[2]))})[/italic yellow]"
            )


printRaw(5)
printNice(5)
