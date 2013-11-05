import mtgparser

set_codes = ['M10', 'ZEN', 'WWK', 'ROE', 'M11', 'SOM', 'MBS', 'NPH', 'M12', 'ISD', 'DKA', 'AVR', 'M13', 'RTR', 'GTC']

standard = "RTR"
decks = []

#standard decks that placed in tournaments
#all places
#standardDecks = mtgparser.getDecks("http://magic.tcgplayer.com/db/deck_search_result.asp?format=Type%20II%20-%20" + standard + "&Place=1st,%202nd,%203rd%20-%204th,%205th%20-%208th,%209th%20-%2016th,%20m17th%20-%2032nd,%20m33rd%20-%2064th&order_by=deck_name")   
#1st, 2nd
decks.extend(mtgparser.getDecks("http://magic.tcgplayer.com/db/deck_search_result.asp?format=Type%20II%20-%20" + standard + "&Place=1st,%202nd&order_by=deck_name"))
#3rd-4th
decks.extend(mtgparser.getDecks("http://magic.tcgplayer.com/db/deck_search_result.asp?format=Type%20II%20-%20" + standard + "&Place=3rd%20-%204th&order_by=deck_name"))
#5th-8th
decks.extend(mtgparser.getDecks("http://magic.tcgplayer.com/db/deck_search_result.asp?format=Type%20II%20-%20" + standard + "&Place=5th%20-%208th&order_by=deck_name"))
#9th-16th
decks.extend(mtgparser.getDecks("http://magic.tcgplayer.com/db/deck_search_result.asp?format=Type%20II%20-%20" + standard + "&Place=9th%20-%2016th&order_by=deck_name"))
#17-32nd
#decks.extend(mtgparser.getDecks("http://magic.tcgplayer.com/db/deck_search_result.asp?format=Type%20II%20-%20" + standard + "&Place=17th%20-%2032nd&order_by=deck_name"))
#33rd-64th
#decks.extend(mtgparser.getDecks("http://magic.tcgplayer.com/db/deck_search_result.asp?format=Type%20II%20-%20" + standard + "&Place=33rd%20-%2064th&order_by=deck_name"))

#testing the card parser with deck 0
decks[0].cards = mtgparser.getCards(decks[0])
decks[0].printDeck()
print len(decks)
decks[len(decks) - 1].printDeck()

#TODO pull data for individual cards (colors, CMC, rarity, etc) 
#TODO store card data in a big dictionary, then only store the card names in the actual deck objects
#TODO Analyze data for individual decks and store it in the deck object
#TODO Analyze data for all decks for the standard and put it in a data object
#TODO Make xml files out of everything, then have a script that uses the xml to easily populate the javaScript frontend
#TODO do analysis for multiple standards

#after everything is said and done, consider contacting tcgplayer to use their api and make revenue