
from random import *
from enum import Enum
from enum import IntEnum


##class Rank():
####    1 = ace
####    2 = two
####    3 = three 
####    4 = four 
####    5 = five
####    6 = six  
####    7 = seven 
####    8 = eight 
####    9 = nine
####    10 = ten 
####    11 = jack 
####    12 = queen 
####    13 = king
##
##    ace = 1
##    two = 2
##    three = 3
##    four = 4
##    five = 5
##    six = 6
##    seven = 7
##    eight = 8
##    nine = 9
##    ten = 10
##    jack = 11
##    queen = 12
##    king = 13
##    
##class Suit():
##    s = 'Spades'
##    h = 'Hearts'
##    d = 'Diamonds'
##    c = 'Clubs'

class PlayingCard:
    def __init__ (self,rank,suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank 

    def getSuit(self):
        return self.suit
    
    def value (self):
        if self.rank > 10:
            self.value = 10
        else:
            self.value = rank
            
    def __str__ (self):
        name = ''
        if self.rank == 1:
            name = 'Ace'
        elif self.rank == 11:
            name = 'Jack'
        elif self.rank == 12:
            name = 'Queen'
        elif self.rank == 13:
            name = 'King'
        else:
            name = self.rank
    
        return ('{0} of {1}'.format(name,self.suit))

def main():
    c = PlayingCard(1,'s')
    c.getRank()
    c.getSuit()
    print(c.__str__())


   
        

if __name__ == "__main__":
    main()
