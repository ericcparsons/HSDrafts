import bs4 as bs
import urllib.request

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
