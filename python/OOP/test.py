deck = [1,2,3,4,5,6,7,8,9,10]

import random

def shuffle(deck):
    shuffled_deck = []
    
    for i in range(0,len(deck)):
        index = random.randrange(0,len(deck))
        shuffled_deck.append(deck[index])
        deck.pop(index)
    deck = shuffled_deck
    print(deck)

    return shuffled_deck

shuffle(deck)

