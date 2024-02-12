from Deck import*
from PlayingCard import*
from graphics import* 

class baccarat:
      
    def __init__(self, dHand=[], pHand=[]):
            #constructor that initializes instance variables
            #it also gives the playingDeck an initial shuffle
        self.dHand = dHand
        self.pHand = pHand
        self.deck = Deck()
        self.deck.shuffle()
        self.images = []

    def dealCard(self, win, xposD, yposD, xposP, yposP, index):
        #deal card for both sides
        
        self.pHand.append(self.deck.dealCard()) #card player

        playerCardRank = self.pHand[index].getRank()
        playerCardSuit = self.pHand[index].getSuit()
        playerFile = "playingcards/" + playerCardSuit + str(playerCardRank) + ".gif"

        pImage = Image(Point(xposP, yposP) , playerFile)
        pImage.draw(win)
        self.images.append(pImage)
        #draw card

        
        self.dHand.append(self.deck.dealCard()) #card banker
        
        dealerCardRank = self.dHand[index].getRank()
        dealerCardSuit = self.dHand[index].getSuit()
        dealerFile = "playingcards/" + dealerCardSuit + str(dealerCardRank) + ".gif"

        dImage = Image(Point(xposD, yposD) , dealerFile)
        dImage.draw(win)
        self.images.append(dImage)
        #draw card


    def bankerDealCard(self, win, xposD, yposD):
        #deal card for banker only
        self.dHand.append(self.deck.dealCard())
        
        dealerCardRank = self.dHand[2].getRank()
        dealerCardSuit = self.dHand[2].getSuit()
        dealerFile = "playingcards/" + dealerCardSuit + str(dealerCardRank) + ".gif"

        dImage = Image(Point(xposD, yposD) , dealerFile)
        dImage.draw(win)
        self.images.append(dImage)
        #draw card
        

        
        
        
            
    def evaluateHand(self, hand):
            #totals the cards in the hand that is passed in and returns total
        total = 0
        for i in range(len(hand)):
            cardValue = hand[i].getRank()
            if cardValue == 10 or cardValue == 11 or cardValue ==12 or cardValue ==13:
                #10,J,Q,K = 0
                total = total
                
            else:
                total = total + cardValue

        return total
    
    def renewWin(self):
    #clear window
        
        for card in self.images:
            card.undraw()


        self.images = []
        self.pHand = []
        self.dHand = []
        self.deck = Deck()
        self.deck.shuffle()

        
























        
        
    
