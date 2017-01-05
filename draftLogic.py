from hearthstone import cardxml; db, _ = cardxml.load()
from hearthstone.enums import CardClass
import random

pickNumber = 1

def selectRarity(pickCount):
    draftRarity = " "
    rarityNumber = random.randint(1,100)
    # 83% RARE, 13% EPIC, 4% LEGENDARY
    if pickCount == 1 or pickCount == 10 or pickCount == 20 or pickCount == 30:
        if rarityNumber < 83:
            draftRarity = 3 # RARE
        elif rarityNumber >= 84 and rarityNumber <= 96:
            draftRarity = 4 # EPIC
        else:
            draftRarity = 5 # LEGENDARY
    # 76% COMMON, 20% RARE, 3% EPIC, 1% LEGENDARY
    else:
        if rarityNumber < 77:
            draftRarity = 1 # COMMON
        elif rarityNumber >= 77 and rarityNumber <= 96:
            draftRarity = 3 # RARE
        elif rarityNumber > 96 and rarityNumber <= 99:
            draftRarity = 4 # EPIC
        elif rarityNumber == 100:
            draftRarity = 5 # LEGENDARY
    return draftRarity


def selectClass(chosenClass):
    cardClass = " "
    classNumber = random.randint(0,100)
    if classNumber < 67:
        cardClass = chosenClass
    else:
        cardClass = 12 # NEUTRAL
    return cardClass

def chooseClass():
    classOptions = random.sample(range(1,9), 3)
    for i in range(len(classOptions)):
        if classOptions[i] == 1:
            classOptions[i] = 2 # DRUID
        elif classOptions[i] == 2:
            classOptions[i] = 3 # HUNTER
        elif classOptions[i] == 3:
            classOptions[i] = 4 # MAGE
        elif classOptions[i] == 4:
            classOptions[i] = 5 # PALADIN
        elif classOptions[i] == 5:
            classOptions[i] = 6 # PRIEST
        elif classOptions[i] == 6:
            classOptions[i] = 7 # ROGUE
        elif classOptions[i] == 7:
            classOptions[i] = 8 # SHAMAN
        elif classOptions[i] == 8:
            classOptions[i] = 9 # WARLOCK
        elif classOptions[i] == 9:
            classOptions[i] = 10 # WARRIOR
    return classOptions

classOptions = chooseClass()    
print(CardClass(classOptions[0]))
print(CardClass(classOptions[1]))
print(CardClass(classOptions[2]))
chosenClass = (classOptions[int(input())])
print('You chose: ' + str(CardClass(chosenClass)))



##while pickNumber <= 30:
##    draftRarity = selectRarity(pickNumber)
    

##def pCards(number):
##    for i in db:
##        if (db[i].rarity == number) and (db[i].collectible) and (db[i].type != 'HERO'):
##            print(db[i].name)
