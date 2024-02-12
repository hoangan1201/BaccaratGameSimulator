from baccarat import*
from graphics import*
from buttonclass import*
from time import*
from wavemod import*


def winner(text):
    text.setSize(35)
    text.setFill("red")
    sleep(3)
    text.setSize(30)
    text.setFill("black")
    

def main():
    win = GraphWin("Baccarat", 800, 800)
    win.setCoords(0, 0, 800, 800)
    #win.setBackground("green")
    bgImg = Image(Point(400,400), "baccaratBG.gif")
    bgImg.draw(win)

    img = Image(Point(300,100), "pokerchip100x100.gif")
    img.draw(win)


    Baccarat = baccarat()

    playerName = Text(Point(200,670), "Player")
    playerName.setSize(25)
    playerName.draw(win)

    bankerName = Text(Point(600,670), "Banker")
    bankerName.setSize(25)
    bankerName.draw(win)

    quitButton = Button(win, Point(700,100), 150, 50, "Quit")

    reButton = Button(win, Point(530,100), 150, 50, "Bet")
    #newButton = Button(win, Point(500,100), 150, 50, "New bet")

    playerB = Button(win, Point(400,300) , 300,50, "Player\n1:1")
    bankerB = Button(win, Point(400,370), 300, 50, "Banker\n0.95:1")
    tieB = Button(win, Point(400, 440), 300, 50, "Tie\n9:1")

    playerAmount = 0
    bankerAmount = 0
    tieAmount = 0

    playerText = Text(Point(200,530), "")
    playerText.setSize(20)
    playerText.draw(win)

    bankerText = Text(Point(600,530), "")
    bankerText.setSize(20)
    bankerText.draw(win)

    betamountList =[25,50,100,200,500]
    betamountText = Text(Point(300,100), "100")
    betamountText.setSize(15)
    betamountText.draw(win)
    betamount = betamountList[2]
    index = 2

    minusButton = Button(win, Point(210,100), 35, 35, "-")
    
    plusButton = Button(win, Point(390,100), 35, 35, "+")


    balance = 10000
    balanceText = Text(Point(100,100), "Balance\n$" + str(balance))
    balanceText.setSize(22)
    balanceText.draw(win)
    
    
    
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        while minusButton.clicked(pt) or plusButton.clicked(pt):
            
            if minusButton.clicked(pt):
                if index > 0:
                    index = index - 1
                else:
                    index = index
                betamount = betamountList[index]
                betamountText.setText(str(betamount))
                pt = win.getMouse()
            

            elif plusButton.clicked(pt):
                if index < 4:
                    index = index + 1
                else:
                    index = index
                betamount = betamountList[index]
                betamountText.setText(str(betamount))
                pt = win.getMouse()


            
        if playerB.clicked(pt): #bet on player
            playerAmount = betamount        
            playerB.bold()
           

        elif bankerB.clicked(pt): #bet on banker
            bankerAmount = betamount
            bankerB.bold()

        elif tieB.clicked(pt): #bet on tie
            tieAmount = betamount
            tieB.bold()


        pt = win.getMouse()
            
        while reButton.clicked(pt):
            # betSound = WavMod("CoinPayout.wav")
            # betSound.test()
            winSound = WavMod("CoinWin.wav")
            winSound.test()
            balance = balance - playerAmount - bankerAmount - tieAmount
            balanceText.setText("Balance\n$" + str(balance))
            
            Baccarat.renewWin()
            playerText.setText("")
            bankerText.setText("")
            playerTotalVal = 0
            bankerTotalVal = 0

            dealCardSound = WavMod("CardFlip.wav")
            dealCardSound.test()
            Baccarat.dealCard(win, 500, 600, 100, 600, 0)
            
            playerTotalVal = Baccarat.evaluateHand(Baccarat.pHand) % 10
            bankerTotalVal = Baccarat.evaluateHand(Baccarat.dHand) % 10

            playerText.setText("Total: " + str(playerTotalVal))
            bankerText.setText("Total: " + str(bankerTotalVal))

            sleep(3)
            dealCardSound = WavMod("CardFlip.wav")
            dealCardSound.test()
            Baccarat.dealCard(win, 600, 600, 200, 600, 1)
            
            playerTotalVal = Baccarat.evaluateHand(Baccarat.pHand) % 10
            bankerTotalVal = Baccarat.evaluateHand(Baccarat.dHand) % 10

            playerText.setText("Total: " + str(playerTotalVal))
            bankerText.setText("Total: " + str(bankerTotalVal))

            sleep(3)
            if playerTotalVal == 9 and bankerTotalVal < 9:
                print("P")
                winner(playerName)
                balance = balance + playerAmount*2
                balanceText.setText("Balance\n$" + str(balance))

                
            elif bankerTotalVal == 9 and playerTotalVal < 9:
                print("B")
                winner(bankerName)
                balance = balance + bankerAmount*1.95
                balanceText.setText("Balance\n$" + str(balance))
                    

            elif playerTotalVal > 5:
                dealCardSound = WavMod("CardFlip.wav")
                dealCardSound.test()
                Baccarat.bankerDealCard(win, 700, 600)
                
                bankerTotalVal = Baccarat.evaluateHand(Baccarat.dHand) % 10
                bankerText.setText("Total: " + str(bankerTotalVal))
                
                if playerTotalVal > bankerTotalVal:
                    print("P")
                    winner(playerName)
                    balance = balance + playerAmount*2
                    balanceText.setText("Balance\n$" + str(balance))
                    
                elif playerTotalVal < bankerTotalVal:
                    print("B")
                    winner(bankerName)
                    balance = balance + bankerAmount*1.95
                    balanceText.setText("Balance\n$" + str(balance))
                    
                else:
                    print("T")
                    balance = balance + tieAmount*10
                    balanceText.setText("Balance\n$" + str(balance))

            else:
                dealCardSound = WavMod("CardFlip.wav")
                dealCardSound.test()
                Baccarat.dealCard(win, 700, 600, 300, 600, 2)
                
                playerTotalVal = Baccarat.evaluateHand(Baccarat.pHand) % 10
                bankerTotalVal = Baccarat.evaluateHand(Baccarat.dHand) % 10

                playerText.setText("Total: " + str(playerTotalVal))
                bankerText.setText("Total: " + str(bankerTotalVal))

                if playerTotalVal > bankerTotalVal:
                    print("P")
                    winner(playerName)
                    balance = balance + playerAmount*2
                    balanceText.setText("Balance\n$" + str(balance))
                    
                elif playerTotalVal < bankerTotalVal:
                    print("B")
                    winner(bankerName)
                    balance = balance + bankerAmount*1.95
                    balanceText.setText("Balance\n$" + str(balance))
                    
                else:
                    print("T")
                    balance = balance + tieAmount*10
                    balanceText.setText("Balance\n$" + str(balance))


            playerAmount = 0
            bankerAmount = 0
            tieAmount = 0
            playerB.unbold()
            tieB.unbold()
            bankerB.unbold()
                
                

            pt = win.getMouse()


    win.close()
        
        


    

main()
