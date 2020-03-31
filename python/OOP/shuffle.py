# Deck of cards
# 52 cards in a deck
# suits hearts, spades, diamonds, clubs

# [x] build card
# [x] build deck
# [ ] implement shuffle
# [ ] implement a sort
# [ ] implement a game

import random

class Card():
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit
        names = {
            1: "Ace",
            11: "Jack",
            12: "Queen",
            13: "King"
        }
        self.name = names.get(value) or str(value)

    def show_value(self):
        print(f"{self.name} of {self.suit}")


# ace_of_hearts = Card('hearts', 2)
# ace_of_hearts.show_value()

class Deck():
    def __init__(self):
        self.cards = []

        # populate / the cards list
        for suit in ["Hearts", "Clubs", "Diamonds", "Spades"]:
            # build each suit
            # print('suit:"', suit)
            for value in range(1, 14):
                # print('value:"', value)
                # create a card
                self.cards.append(Card(suit, value))

    def shuffle(self):
        deck = self.cards
        for i in range(0,3000):
            index = random.randrange(0,len(deck))
            [deck[index],deck[-1]] = [deck[-1],deck[index]]

        return self

    def sort(self):
        pass

    def game(self):
        pass


bicycle_deck = Deck()

bicycle_deck.shuffle()

for card in bicycle_deck.cards:
    card.show_value()
