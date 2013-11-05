import card

class Deck:
    colors = []
    name = ""
    deckURL = ""
    owner = ""
    ownerURL = ""
    location = ""
    locationURL = ""
    placement = ""
    date = ""
    mainCards = []
    sideCards = []
    
    def printDeckInfo(self):
        print self.name
        print self.deckURL
        print "------------------------------"
        print "\t",self.owner
        print "\t",self.location
        print "\t",self.placement
        print "\t",self.date
        
    def printCards(self):
        for card in self.cards:
            print "\t\t ",card.count," ",card.name,
            if (card.sideboard == 1):
                print " (sideboard)"
            else:
                print ""
            
    def printDeck(self):
        self.printDeckInfo()
        self.printCards()
    