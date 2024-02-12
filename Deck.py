from PlayingCard import*
from random import*



class Deck():
    def __init__(self):
        self.cardList = []
        for s in ['d', 'c', 'h', 's']:
            for r in range(1,14):
                self.cardList.append(PlayingCard(r,s))
       
                
    def shuffle(self):
        shuffle(self.cardList)
        return self.cardList

    def dealCard(self):
        index = randrange(0,len(self.cardList))
        #new_card = self.cardList[index]
        return self.cardList.pop(index)
    def cardLeft(self):
        
        return len(self.cardList)

def main():
    deck = Deck()
    deck.shuffle()
    print(deck.dealCard())
    print(deck.cardLeft())



if __name__ == "__main__":
    main()
    

        
