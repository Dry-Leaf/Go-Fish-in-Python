import random

pip = ["a", "2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k"]
suit = ["♣", "♦", "♥", "♠"]

def make_deck():
    new_deck = []
    for p in pip:
        for s in suit:
            new_deck.append([p, s])
    return new_deck

def shuffle(deck):
    random.shuffle(deck)
    return deck 

def deal(other_deck, deck):
    if deck: other_deck.append(deck.pop(0))

def contents(deck):
    line = 1
    for card in range(len(deck)):
        print(*deck[card], sep='', end =" ")
        if (card / 13) > line: 
            print(); line += 1
    print()
'''
new = shuffle(make_deck()) 
contents(new)
'''
