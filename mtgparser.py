import httplib2
from bs4 import BeautifulSoup
import deck
import card

def getDecks(url):
    #gets the HTML file
    http = httplib2.Http()
    
    resp, raw = http.request(url)
    
    content = raw.decode('windows-1252')
    
    #replace bad characters
    content = content.replace('\x92', u"'")
    
    #converts to a BeautifulSoup parse tree
    soup = BeautifulSoup(content)
    
    #finds the header of the table, then uses nextSibling to find the table of decks
    deckTable = soup.body.find('table', bordercolorlight="#303030").findNextSibling('table')
    
    #write the soup hierarchy to file
    fh = open("workfile.txt", "w")
    fh.write(soup.prettify())
    fh.close()
    
    #write deck table to file
    fd = open("decktable.txt", "w")
    fd.write(deckTable.prettify())
    fd.close()
    
    #deck counter
    num = 1
    decks = []
    
    #parses the deck data
    #for each row (deck)
    for tr in deckTable:
        #if the row is valid
        if type(tr) ==  type(deckTable.tr):
            
            #field counter
            fieldCount = 0
            
            #increment count
            num = num + 1
            d = deck.Deck()
            
            #for each column (field)
            for td in tr:
                #if column is valid
                if type(td) == type(deckTable.tr.td):
                    
                    #find their contents
                    if len(td) == 1:
                        string = td.string
                    else:
                        string = td.contents[1].string
                    
                    #deck colors
                    if fieldCount == 0:
                        pass
                    #deck name
                    elif fieldCount == 1:
                        d.deckURL = 'http://magic.tcgplayer.com' + td.a['href']
                        d.name = string
                    #deck owner
                    elif fieldCount == 2:
                        d.ownerURL = 'http://magic.tcgplayer.com' + td.a['href']
                        d.owner = string
                    #tournament
                    elif fieldCount == 3:
                        d.locationURL = 'http://magic.tcgplayer.com' + td.a['href']
                        d.location = string
                    #placement
                    elif fieldCount == 4:
                        d.placement = string
                    #date
                    elif fieldCount == 5:
                        d.date = string
                        
                    #increment field count
                    fieldCount += 1
                    
            #store deck in the list 
            decks.append(d)
    
    return decks
    
def getCards(deck):
    
    #gets the HTML file
    http = httplib2.Http()
    resp, raw = http.request(deck.deckURL.replace('deck.asp', 'deck_blog.asp'))
    
    #replaces bad characters
    content = raw.decode('windows-1252')
    content = content.replace('\x92', u"'")
    content = content.replace('<BR>\r<br>', '<br>')
    
    #converts to a BeautifulSoup parse tree
    soup = BeautifulSoup(content)
    
     #writes the deck page to file
    fd = open("cardtable.txt", "w")
    fd.write(soup.prettify())
    fd.close()
    
    cards = []
    
    #find the </br> tag after Main Deck:
    cardElement = soup.body.div.find('b').findNextSibling('b').findNextSibling('a')
    while(True):
        #get card attributes
        numCard = unicode(cardElement.previousSibling).strip(' \r\n')
        cardURL = cardElement['href']
        cardName = cardElement.string

        #store attributes into a Card object
        newCard = card.Card()
        newCard.count = int(numCard)
        newCard.name = cardName
        newCard.URL = cardURL
           
        #add to the main deck
        if (cardElement.findPreviousSibling('b').string.strip(' \r\n') == 'Main Deck:'):
            newCard.sideboard = 0
        #add to the sideboard
        elif (cardElement.findPreviousSibling('b').string.strip(' \r\n') == 'Sideboard:'):
            newCard.sideboard = 1
            
        cards.append(newCard)
        
        #break when done
        if(cardElement.findNextSibling('a') == None):
            break
        
        #increment card
        cardElement = cardElement.findNextSibling('a')
            
            
    return cards
    
    