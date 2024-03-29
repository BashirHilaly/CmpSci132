"""
----------------------------------------------------
-- CMPSC_132, Spring 2024, Bashir Hilaly
-- Lab: Dealing Cards
----------------------------------------------------
"""
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
    while not inputValid:
        playersInput = input('Input the number of players between 1 and 5: ')
        if int(playersInput) > 5 or int(playersInput) < 1:
            print("Invalid player input")
            inputValid = False
        else:
            inputValid = True
            return int(playersInput)

if __name__ == "__main__":

    deck = generateDeck()
    numberOfPlayer = inputPlayers()