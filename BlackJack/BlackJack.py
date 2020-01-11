import random


class Card():
    def __init__(self, deck, suite, face, value1, value2):
        self.deck = deck
        self.suite = suite
        self.value1 = value1
        self.value2 = value2

        self.face = face

    def getValue1():
        return self.value1

    def getValue2():
        return self.value2

    def __str__(self):
        ###Function called when class is printed
        return (str(self.deck) + " " + self.suite + " " + str(self.face))


class Deck():
    cardCount = 52
    suiteCount = 13

    def __init__(self, deckId):
        ### Initilize the deck with predefined suites and values
        self.cards = [None] * Deck.cardCount
        i = 0
        # Loop over 13 Cards * 4 suites
        for face in range(1, self.suiteCount + 1):
            for suite in ('D', 'S', 'C', 'H'):
                if int(face) == 1:  # Conditions for Ace
                    value1 = 1
                    value2 = 11
                elif int(face) > 10:
                    value1 = 10
                    value2 = 10
                else:
                    value1 = int(face)
                    value2 = int(face)
                # print(i)
                self.cards[i] = Card(deckId, suite, face, value1, value2)

                # print(self.cards[i])
                i += 1

    def __str__(self):
        ###Function called when class is printed
        # prints the entire deck and returns blank
        print("Deck Suite Value")
        for i in range(self.cardCount):
            print(self.cards[i])
        return ""

    def draw_card(self):
        ###draw a random cards from the deck and return Card object
        randCard = random.randint(0, 51)
        return self.cards[randCard]


class CardSet():
    def __init__(self, deckCount):
        self.deckCount = deckCount
        self.decks = [None] * self.deckCount
        for d in range(self.deckCount):
            self.decks[d] = Deck(d)

    # Function called when class is printed
    def __str__(self):
        for p in range(self.deckCount):
            print(self.decks[p])
        return ""

    def draw_card(self, drawCount):  # draw a card from the cardset and return Card object
        ###draw a number of random cards from the cardset and return List of Card objects
        listCards = [None] * drawCount
        for i in range(drawCount):
            randDeck = random.randint(0, self.deckCount - 1)
            listCards[i] = self.decks[randDeck].draw_card()
        return listCards


def calculateTotal(listCards):
    count = len(listCards)
    total1 = 0
    total2 = 0
    for i in range(count):
        total1 += listCards[i].getValue1()
        total2 += listCards[i].getValue2()


def main():
    # deckCount = int(input("How many decks? : "))
    deckCount = 2
    cardSet = CardSet(deckCount)
    # print(cardSet)

    listCards = cardSet.draw_card(2)
    print(*listCards, sep='\n')


if __name__ == "__main__":
    main()