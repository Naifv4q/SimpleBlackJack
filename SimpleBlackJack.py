import BlackJackArt
import random
from os import system

CardsDic={0:"Ace",1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:"King",12:"Queen",13:"Jack"}

def calculateScore(cards):
    """This function takes the cards as an argument and return its summed score."""
    score=0
    numOfAces=0
    
    for card in cards:
        if card in ["King","Queen","Jack"]:
            score+=10
        elif card == "Ace":
            numOfAces+=1
        else:
            score+=card
    
    
    for ace in range(numOfAces):
        if score + 11 > 21:
            score+=1
        else:
            score+=11
    
    return score

def drawCard():
    """This function simply draws 1 card from CardsDic."""
    return random.choice(list(CardsDic.values()))

def getInitialCards():
    """This function deals 2 cards for the player to initiate the game."""
    return [drawCard(),drawCard()]

def playerTurn(userCards,dealerCards):
    """This function takes both user & dealer cards as an argument, to print both
       and give the player the choice to draw one more card if he sees fit."""
    while True:
        score=calculateScore(userCards)
        print(f"Your cards: {userCards}, current score: {score}")
        print(f"Dealer first Card: {dealerCards}")
        if score>=21:
            return score
        isTrue=True
        while isTrue:
            dec=input("Type [y] to get another card, [n] to pass: ").lower()
            if dec=="y":
                userCards.append(drawCard())
                isTrue=False
            elif dec=="n":
                return score
                isTrue=False
            else:
                print("Invalid input !")

def dealerTurn(dealerCards):
    """This function takes the dealers cards as an argument, then see if the dealer has less than 17,
       if so he draws another card, if not the function simply returns the summed score of the dealer's cards"""
    while calculateScore(dealerCards)<17:
        dealerCards.append(drawCard())
    return calculateScore(dealerCards)

def playBlackJack():
    """This function starts the game by asking the player if he wants to play, and uses all the above functions
       to make the game work as intended !"""
    
    dec=input("Would you like to play a game of blackjack ? [y] for yes, [n] for no: ").lower()
    while True:
        system("cls")
        BlackJackArt.Intro()
        print("="*80)
        if dec=="y":
            userCards=getInitialCards()
            dealerCards=[drawCard()]
            
            userScore=playerTurn(userCards,dealerCards)
            dealerScore=dealerTurn(dealerCards)
            
            print(f"Your cards: {userCards}, your score: {userScore}")
            print(f"Dealer cards: {dealerCards}, dealer score: {dealerScore}")
            
            if userScore > 21:
                print("You went over 21, you lose !")
                dec=input("Would you like to play a game of blackjack ? [y] for yes, [n] for no: ").lower()
            elif dealerScore > 21:
                print("Dealer went over 21, you win !")
                dec=input("Would you like to play a game of blackjack ? [y] for yes, [n] for no: ").lower()
            elif userScore > dealerScore:
                print("You win !")
                dec=input("Would you like to play a game of blackjack ? [y] for yes, [n] for no: ").lower()
            elif dealerScore > userScore:
                print("The house wins ! You lose :(")
                dec=input("Would you like to play a game of blackjack ? [y] for yes, [n] for no: ").lower()
            elif dealerScore == userScore:
                print("Its a draw !")
                dec=input("Would you like to play a game of blackjack ? [y] for yes, [n] for no: ").lower()
        elif dec=="n":
            print("Maybe another time :)")
            break
        else:
            print("Invalid input ! Please enter [y] or [n].")
            dec=input("Would you like to play a game of blackjack ? [y] for yes, [n] for no: ").lower()

playBlackJack()
