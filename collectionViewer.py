import bs4 as bs
import urllib.request
from collections import Counter

hpUserName = input("Enter your HearthPwn Username: ")

sauce = urllib.request.urlopen('http://www.hearthpwn.com/members/%s/collection' % (hpUserName)).read()
soup = bs.BeautifulSoup(sauce, 'lxml')

nCardsOwned = []
nCardsOwnedNumber = []
gCardsOwned = []
gCardsOwnedNumber = []

def scrapeUserCollection():
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

normalCardsOwned = dict(zip(nCardsOwned, nCardsOwnedNumber))
goldenCardsOwned = dict(zip(gCardsOwned, gCardsOwnedNumber))
a = Counter(normalCardsOwned)
b = Counter(goldenCardsOwned)
allCardsOwned = dict(a+b)
