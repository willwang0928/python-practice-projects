import random
print("Welcome to Blackjack!")
print("The goal of the game is to get as close to 21 as possible without going over.")

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
player_hand = []
dealer_hand = []

def initial_hand():
    player_hand.append(deck.pop(random.randint(0, len(deck)-1)))
    dealer_hand.append(deck.pop(random.randint(0, len(deck)-1)))
    dealer_hand.append(deck.pop(random.randint(0, len(deck)-1)))
    player_hand.append(deck.pop(random.randint(0, len(deck)-1)))
    
initial_hand()
print("Player's hand:", player_hand, "Total:", sum(player_hand))
print("Dealer's hand:", dealer_hand, "Total:", sum(dealer_hand))

print("You need " + str(21 - sum(player_hand)) + " to win.")

def player_turn():
    while True:
        choice = input("Do you want to hit or stand? (h/s) ")
        if choice.lower() == 'h':
            player_hand.append(deck.pop(random.randint(0, len(deck)-1)))
            print("Player's hand:", player_hand, "Total:", sum(player_hand))
            print("You need " + str(21 - sum(player_hand)) + " to win.")
            if sum(player_hand) > 21:
                print("You bust! Dealer wins.")
                break
        elif choice.lower() == 's':
            break
        else:
            print("Invalid choice. Please enter 'h' or 's'.")
            
def dealer_turn():
    while sum(dealer_hand) < 17:
        dealer_hand.append(deck.pop(random.randint(0, len(deck)-1)))
    print("Dealer's hand:", dealer_hand, "Total:", sum(dealer_hand))
    if sum(dealer_hand) > 21:
        print("Dealer busts! You win.")
        
player_turn()

if sum(player_hand) <= 21:
    dealer_turn()
    if sum(dealer_hand) <= 21:
        if sum(player_hand) > sum(dealer_hand):
            print("You win!")
        elif sum(player_hand) < sum(dealer_hand):
            print("Dealer wins!")
        else:
            print("Push! It's a tie.")
            
# add main with play again function


