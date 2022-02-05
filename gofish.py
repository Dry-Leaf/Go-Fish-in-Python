import sys
from pc import *

players = ["human", "computer"]

#processes 
def setup():
    global pool; pool = shuffle(make_deck())
    global human_hand; human_hand = []
    global computer_hand; computer_hand = []
    global human_books; human_books = [0]; 
    global computer_books; computer_books = [0]
    global books; books = pip.copy()
    global ai_fish; ai_fish = None
    for x in range(9):
        deal(human_hand, pool); deal(computer_hand, pool)
    global active_player; active_player = random.choice(players)

def empty_check(hand):
    if not hand: deal(hand, pool)

def request():
    print("Request a pip in your deck(quit to exit game): ")
    user_input = input()
    if user_input == "quit": sys.exit()

    if user_input in pip: 
        return user_input 
    else:
        print("invalid input"); return request()
    
def search(request, hand):
    for card in hand:
        if card[0] == request: 
            return True
    return False
    
def fish(hand, player, request):
    global pool; global ai_fish; print("Go Fish\n") 
    deal(hand, pool)
    last_pip = hand[-1][0]
    
    if player == "computer": 
        if search(last_pip, hand[:-1]) == False:
            ai_fish = last_pip
    if last_pip == request:
        print("Drawn Card:", end = " "); contents([hand[-1]])
    
    
def give(request, giver_hand, asker_hand):
    matches = [card for card in giver_hand if card[0] == request]
    rem_cards = [card for card in giver_hand if card[0] != request]
    giver_hand.clear()
    giver_hand += rem_cards; asker_hand += matches;
    
def book_check(hand, player_books):
    global books; completed = []
    for book in books:
        counter = 0
        for card_number in range(len(hand)):
            if hand[card_number][0] == book: counter += 1
        if counter == 4:
            rem_cards = [card for card in hand if card[0] != book]
            hand.clear(); hand += rem_cards
            completed.append(book); player_books[0] += 1
            print("Book: ", book, "completed.\n")
    rem_books = [book for book in books if book not in completed]
    books.clear(); books += rem_books

def ai():
    global ai_fish
    
    if not ai_fish:
        return random.choice(computer_hand)[0]
    else:
        remembered = ai_fish; ai_fish = None
        return remembered
    
#game flow
def turn():
    global active_player; global pool
    while True:
        if active_player == "human":
            active_hand = human_hand; active_books = human_books
            passive_hand = computer_hand; passive_books = computer_books

        else:
            active_hand = computer_hand; active_books = computer_books
            passive_hand = human_hand; passive_books = human_books

        book_check(active_hand, active_books)    
        book_check(passive_hand, passive_books)
        empty_check(active_hand); empty_check(passive_hand)

        if not active_hand: break
        
        if active_player == "human":
            print("Your hand: "); contents(human_hand); print() 
            while True:
                choice = request()
                if search(choice, active_hand) == True: break

        else:
            choice = ai(); print("Computer's choice: ", choice)
        
        if search(choice, passive_hand) == True:
            give(choice, passive_hand, active_hand)
        else:
            fish(active_hand, active_player, choice); break
            
    active_player = players[not players.index(active_player)]
    print("Remaining Books", *books); input()

def demo():
    setup()
    while computer_books[0] + human_books[0] < 13:
         turn()
    print("Computer Books: ", computer_books[0], "\nHuman Books: ", human_books[0])
    if human_books[0] > computer_books[0]:
        print("You Win")
    else:
        print("You lose")

#testing bay 
demo()

