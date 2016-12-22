import json
import requests
import pprint
import sqlite3

# connects to json and imports info to cardData
url = 'https://api.hearthstonejson.com/v1/15590/enUS/cards.collectible.json'
response = requests.get(url)
print(response)

cardData = json.loads(response.text)

conn = sqlite3.connect('allCollectibleCards.db')
c = conn.cursor()

def createTables():
    c.execute('CREATE TABLE IF NOT EXISTS minions(name TEXT, playerClass TEXT, rarity TEXT, expansion TEXT, cost INTEGER, attack INTEGER, health INTEGER, text TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS spells(name TEXT, playerClass TEXT, rarity TEXT, expansion TEXT, cost INTEGER, text TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS weapons(name TEXT, playerClass TEXT, rarity TEXT, expansion TEXT, cost INTEGER, attack INTEGER, durability INTEGER, text TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS heroes(name TEXT, playerClass TEXT)')

def minionDataEntryWithText():
    name = item['name']
    playerClass = item['playerClass']
    rarity = item['rarity']
    expansion = item['set']
    cost = item['cost']
    attack = item['attack']
    health = item['health']
    cardText = item['text']
    c.execute("INSERT INTO minions (name, playerClass, rarity, expansion, cost, attack, health, text) VALUES (?,?,?,?,?,?,?,?)",
              (name, playerClass, rarity, expansion, cost, attack, health, cardText))
    conn.commit()

def minionDataEntryWithoutText():
    name = item['name']
    playerClass = item['playerClass']
    rarity = item['rarity']
    expansion = item['set']
    cost = item['cost']
    attack = item['attack']
    health = item['health']
    c.execute("INSERT INTO minions (name, playerClass, rarity, expansion, cost, attack, health) VALUES (?,?,?,?,?,?,?)",
              (name, playerClass, rarity, expansion, cost, attack, health))
    conn.commit()

def minionDataEntryWithMultiClass():
    h = 0
    while h < 3:
        name = item['name']
        classes = item['classes']
        playerClass = classes[h]
        rarity = item['rarity']
        expansion = item['set']
        cost = item['cost']
        attack = item['attack']
        health = item['health']
        cardText = item['text']
        c.execute("INSERT INTO minions (name, playerClass, rarity, expansion, cost, attack, health, text) VALUES (?,?,?,?,?,?,?,?)",
              (name, playerClass, rarity, expansion, cost, attack, health, cardText))
        conn.commit()
        h = h + 1

def spellDataEntryWithText():
    name = item['name']
    playerClass = item['playerClass']
    rarity = item['rarity']
    expansion = item['set']
    cost = item['cost']
    cardText = item['text']
    c.execute("INSERT INTO spells (name, playerClass, rarity, expansion, cost, text) VALUES (?,?,?,?,?,?)",
              (name, playerClass, rarity, expansion, cost, cardText))
    conn.commit()

def weaponDataEntryWithText():
    name = item['name']
    playerClass = item['playerClass']
    rarity = item['rarity']
    expansion = item['set']
    cost = item['cost']
    attack = item['attack']
    durability = item['durability']
    cardText = item['text']
    c.execute("INSERT INTO weapons (name, playerClass, rarity, expansion, cost, attack, durability, text) VALUES (?,?,?,?,?,?,?,?)",
              (name, playerClass, rarity, expansion, cost, attack, durability, cardText))
    conn.commit()

def weaponDataEntryWithoutText():
    name = item['name']
    playerClass = item['playerClass']
    rarity = item['rarity']
    expansion = item['set']
    cost = item['cost']
    attack = item['attack']
    durability = item['durability']
    c.execute("INSERT INTO weapons (name, playerClass, rarity, expansion, cost, attack, durability) VALUES (?,?,?,?,?,?,?)",
              (name, playerClass, rarity, expansion, cost, attack, durability))
    conn.commit()

def heroDataEntry():
    name = item['name']
    playerClass = item['playerClass']
    c.execute("INSERT INTO heroes (name, playerClass) VALUES (?,?)",
              (name, playerClass))

def connClose():
    c.close()
    conn.close()

createTables()

for item in cardData:
    if item['type']=='MINION':
        if 'classes' in item:
            minionDataEntryWithMultiClass()
        else:
            if ('text' in item):
                minionDataEntryWithText()
            else:
                minionDataEntryWithoutText()
    elif item['type']=='SPELL':
        if ('text' in item):
            spellDataEntryWithText()
    elif item['type']=='WEAPON':
        if ('text' in item):
            weaponDataEntryWithText()
        else:
            weaponDataEntryWithoutText()
    elif item['type']=='HERO':
        if item['set']=='CORE':
            heroDataEntry()

print('Database Successfully Created!')
connClose()

##if __name__=="__main__":
##    createTables()
##
##    for item in cardData:
##        if item['type']=='MINION':
##            if 'classes' in item:
##                minionDataEntryWithMultiClass()
##            else:
##                if ('text' in item):
##                    minionDataEntryWithText()
##                else:
##                    minionDataEntryWithoutText()
##        elif item['type']=='SPELL':
##            if ('text' in item):
##                spellDataEntryWithText()
##        elif item['type']=='WEAPON':
##            if ('text' in item):
##                weaponDataEntryWithText()
##            else:
##                weaponDataEntryWithoutText()
##        elif item['type']=='HERO':
##            if item['set']=='CORE':
##                heroDataEntry()
##
##    print('Database Successfully Created!')
##    connClose()
