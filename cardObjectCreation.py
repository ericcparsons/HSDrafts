import json
import requests
import bs4 as bs
import urllib.request
from collections import Counter
import random

# connects to hearthpwn and scrapes users collection into allCardsOwned
hpUserName = input("Enter your HearthPwn Username: ")

sauce = urllib.request.urlopen('http://www.hearthpwn.com/members/%s/collection' % (hpUserName)).read()
soup = bs.BeautifulSoup(sauce, 'lxml')

nCardsOwned = []
nCardsOwnedNumber = []
gCardsOwned = []
gCardsOwnedNumber = []

def scrapeUserCollection():
    # does the scraping
    for h in soup.find_all(attrs={'class':'card-image-item owns-card'}):
        if h.get('data-is-gold') == 'False':
            nCardsOwned.append(h.get('data-card-name'))

    for i in soup.find_all(attrs={'class':'card-image-item owns-card'}):
        for j in i.find_all(attrs={'class':'inline-card-count'}):
            if i.get('data-is-gold') == 'False':
                nCardsOwnedNumber.append(int(j.get('data-card-count')))

    for k in soup.find_all(attrs={'class':'card-image-item owns-card'}):
        if k.get('data-is-gold') == 'True':
            gCardsOwned.append(k.get('data-card-name'))

    for l in soup.find_all(attrs={'class':'card-image-item owns-card'}):
        for m in l.find_all(attrs={'class':'inline-card-count'}):
            if l.get('data-is-gold') == 'True':
                gCardsOwnedNumber.append(int(m.get('data-card-count')))

scrapeUserCollection()

# combines lists into a dictionary with numbers owned
normalCardsOwned = dict(zip(nCardsOwned, nCardsOwnedNumber))
goldenCardsOwned = dict(zip(gCardsOwned, gCardsOwnedNumber))
a = Counter(normalCardsOwned)
b = Counter(goldenCardsOwned)
allCardsOwned = dict(a+b)

# connects to json and imports info to cardData
url = 'https://api.hearthstonejson.com/v1/15590/enUS/cards.collectible.json'
response = requests.get(url)
print(response)

cardData = json.loads(response.text)

# constructer for Card
class Card(object):

    def __init__(self, name, playerClass, rarity, cost, set, type, id):
        self.name = name
        self.playerClass = playerClass
        self.rarity = rarity
        self.cost = cost
        self.set = set
        self.type = type
        self.id = id
        self.numOwned = 0

    def setAttackHealth(self, attack, health):
        self.attack = attack
        self.health = health

    def setText(self, text):
        self.text = text

    def setAttackDurability(self, attack, durability):
        self.attack = attack
        self.durability = durability

# builds list of Cards from JSON
allCards = []
goodType = ['MINION', 'SPELL', 'WEAPON']
cardCount = -1
for item in cardData:
    if item['type'] in goodType:
        allCards.append(Card(item['name'], item['playerClass'], item['rarity'], item['cost'], item['set'], item['type'], (cardCount + 1)))
        cardCount = cardCount + 1
    if 'text' in item:
        allCards[cardCount].setText(item['text'])
    if item['type'] == 'MINION':
        allCards[cardCount].setAttackHealth(item['attack'], item['health'])
    if item['type'] == 'WEAPON':
        allCards[cardCount].setAttackDurability(item['attack'], item['durability'])
    
# searches through allCards for a card by exact name
def cardSearch(name):
    for k in allCards:
        if k.name == name:
            print('Name: ' + k.name)
            print('Type: ' + k.type)
            try:
                print('Attack: ' + str(k.attack))
                try:
                    print('Health: ' + str(k.health))
                except:
                    pass
                try:
                    print('Durability: ' + str(k.durability))
                except:
                    pass
            except:
                pass
            try:
                print('Text: ' + k.text)
            except:
                pass
            print('Class: ' + k.playerClass)
            print('Rarity: ' + k.rarity)
            print('Set: ' + k.set)
            print('ID: ' + str(k.id))

# sets numberOwned for each Card in allCards
for item in allCardsOwned:
    for Card in allCards:
        if item == Card.name:
            Card.numOwned = allCardsOwned.get(item)

for Card in allCards:
    if Card.numOwned == 0:
        allCards.remove(Card)

pickCount = 1

def selectRarity(pickCount):
    # selects rarity for pick
    draftRarity = ""
    rarityChance = random.randint(1,100)
    # 83% RARE, 13% EPIC, 4% LEGENDARY
    if pickCount == 1 or pickCount == 10 or pickCount == 20 or pickCount == 30:
        if rarityChance < 83:
            draftRarity = 'RARE' # RARE
        elif rarityChance >= 84 and rarityChance <= 96:
            draftRarity = 'EPIC' # EPIC
        else:
            draftRarity = 'LEGENDARY' # LEGENDARY
    # 76% COMMON, 20% RARE, 3% EPIC, 1% LEGENDARY
    else:
        if rarityChance < 77:
            draftRarity = 'COMMON' # COMMON
        elif rarityChance >= 77 and rarityChance <= 96:
            draftRarity = 'RARE' # RARE
        elif rarityChance > 96 and rarityChance <= 99:
            draftRarity = 'EPIC' # EPIC
        elif rarityChance == 100:
            draftRarity = 'LEGENDARY' # LEGENDARY
    return draftRarity

def selectNeutrality(chosenClass):
    # selects whether card will be neutral or chosen class
    cardClass = ""
    classNumber = random.randint(0,100)
    if classNumber < 67: # CHOSEN CLASS
        cardClass = chosenClass
    else:
        cardClass = 'NEUTRAL' # NEUTRAL
    return cardClass

# presents user with 3 classes to choose from
classOptions = random.sample(range(1, 9), 3)
for i in range(len(classOptions)):
    if classOptions[i] == 1:
        classOptions[i] = 'DRUID'
    elif classOptions[i] == 2:
        classOptions[i] = 'HUNTER'
    elif classOptions[i] == 3:
        classOptions[i] = 'MAGE'
    elif classOptions[i] == 4:
        classOptions[i] = 'PALADIN'
    elif classOptions[i] == 5:
        classOptions[i] = 'PRIEST'
    elif classOptions[i] == 6:
        classOptions[i] = 'WARRIOR'
    elif classOptions[i] == 7:
        classOptions[i] = 'WARLOCK'
    elif classOptions[i] == 8:
        classOptions[i] = 'ROGUE'
    elif classOptions[i] == 9:
        classOptions[i] = 'SHAMAN'
print(classOptions)
chosenClass = classOptions[int(input('Choose a class (0, 1, or 2): '))]
print('You chose ' + chosenClass)

# reduces numOwned down to max pick for a deck (1 for legendary, 2 for everything else)
for Card in allCards:
    if Card.rarity == 'LEGENDARY':
        Card.numOwned = 1
    else:
        Card.numOwned = 2
    
chosenCards = []

# builds a list of Cards that match the selected rarity/neutrality
def findMatches(pickRarity, pickNeutrality):
    matches = []
    for Card in allCards:
        if pickRarity == Card.rarity and pickNeutrality == Card.playerClass:
            matches.append(Card)
    return matches

# draft logic
while pickCount <= 30:
    try:
        cardOptions = []
        pickRarity = selectRarity(pickCount)
        while len(cardOptions) <= 2:
            pickNeutrality = selectNeutrality(chosenClass)
            matches = findMatches(pickRarity, pickNeutrality)
            cardOptionsTemp = random.randint(0, len(matches)-1)
            if matches[cardOptionsTemp].name in cardOptions:
                pass
            else:
                cardOptions.append(matches[cardOptionsTemp].name)  
        print(cardOptions)
        chosenCard = cardOptions[int(input('Choose a card (0, 1, or 2): '))]
        chosenCards.append(chosenCard)
        for Card in allCards:
            if Card.name == chosenCard:
                Card.numOwned = Card.numOwned - 1
                if Card.numOwned == 0:
                    allCards.remove(Card)
        pickCount += 1
    except:
        pass
    
print(chosenCards)

