import bs4 as bs
import urllib.request
import random

hpUserName = input("Enter your HearthPwn Username: ")

sauce = urllib.request.urlopen('http://www.hearthpwn.com/members/%s/collection' % (hpUserName)).read()
soup = bs.BeautifulSoup(sauce, 'lxml')

cardsOwned = []
cardsOwnedNumber = []

def scrapeUserCollection():
    for h in soup.find_all(attrs={'class':'card-image-item owns-card'}):
        cardsOwned.append(h.get('data-card-name'))

    for i in soup.find_all(attrs={'class':'card-image-item owns-card'}):
        for j in i.find_all(attrs={'class':'inline-card-count'}):
            cardsOwnedNumber.append(j.get('data-card-count'))

#selects the rarity of the chosen card
def selectRarity(pickCount):
    draftRarity = " "
    rarityNumber = random.randint(1,100)
    if pickCount == 1 or pickCount == 10 or pickCount == 20 or pickCount == 30:
        if rarityNumber < 83:
            draftRarity = "RARE"
        elif rarityNumber >= 84 and rarityNumber <= 96:
            draftRarity = "EPIC"
        else:
            draftRarity = "LEGENDARY"
    else:
        if rarityNumber < 77:
            draftRarity = "COMMON"
        elif rarityNumber >= 77 and rarityNumber <= 96:
            draftRarity = "RARE"
        elif rarityNumber > 96 and rarityNumber <= 99:
            draftRarity = "EPIC"
        else:
            draftRarity = "LEGENDARY"
    return draftRarity

def selectClass():
    classNumber = random.randint(0,100)
    