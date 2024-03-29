"""
----------------------------------------------------
-- CMPSC_132, Spring 2024, Bashir Hilaly
-- Lab: Dealing Cards
----------------------------------------------------
"""
import random
import time

def generateDeck():
    suits = ['Clubs', 'Diamonds', 'Spades', 'Hearts']
    rankings = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    cards = []
    for suit in suits:
        for ranking in rankings:
            card = f'{ranking} of {suit}'
            cards.append(card)
    return cards

def inputPlayers():
    inputValid = False
    numOfPlayers = 0
    players = []
    while not inputValid:
        playersInput = input('Input the number of players between 1 and 5: ')
        if int(playersInput) > 5 or int(playersInput) < 1:
            print("Invalid player input")
            inputValid = False
        else:
            inputValid = True
            numOfPlayers = int(playersInput)
    for i in range(numOfPlayers):
        name = input(f'Enter a name for player {i+1}: ')
        players.append(name)
    return players

def dealCards(deck):
    # Choose a random card
    selectedCard = random.choice(deck)
    deck.remove(selectedCard)
    return selectedCard

if __name__ == "__main__":
    # deck is a list of 52 playing cards
    print("\nWelcome to Dealing cards!\n")
    deck = generateDeck()

    # Returns a list of players
    print('Lets get started\n')
    players = inputPlayers()

    # time.sleep() is for making the input look nicer
    print("\nDealing cards...\n")
    time.sleep(1)
    # Deal the cards
    playerTurn = 0 # Current player who is being served the card
    numOfDealtCards = 0
    # To only deal 5 cards to each player then change for loop to: range(len(players) * 5) To deal all change to len(deck)
    for card in range(len(players) * 5): # Loop through the dynamically changing deck range
        if playerTurn >= len(players): playerTurn = 0 # if we went around to all players we start again from the begining
        print('\n', dealCards(deck), 'dealt to', players[playerTurn])
        playerTurn += 1
        numOfDealtCards += 1
        time.sleep(.3)

print("\nALL CARDS HAVE BEEN DEALT")