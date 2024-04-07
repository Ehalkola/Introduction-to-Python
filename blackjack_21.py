import random


# Define function to generate and shuffle deck of cards
def deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = list(range(2, 15))  # Cards from 2 to Ace (14)
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck


# Define function to draw a card from the deck
def draw_card(deck):
    return deck.pop()


# Define function display_hand to display hand
def display_hand(hand, show_all=False):
    if show_all:
        return hand
    else:
        return [hand[0], 'Face Down Card']


# Define function to calculate the value of a hand
def hand_value(hand):
    value = sum(card[0] for card in hand)
    # Adjust for Ace
    for card in hand:
        if card[0] == 14 and value > 21:
            value -= 10
    return value


# Define function play to run the game
def blackjack():
    while True:
        # Create a new deck for each game
        game_deck = deck()

        # Draw first card for dealer
        dealer_hand = [draw_card(game_deck)]

        # Draw first card for player
        player_hand = [draw_card(game_deck)]

        # Player's turn
        while hand_value(player_hand) < 21:
            print(f"Player's Hand: {player_hand}")
            print(f"Dealer's Hand: {display_hand(dealer_hand)}")

            # Ask user if they want to hit or stand, define if loop to draw a card (hit) or (stand) 'break'
            action = input("Do you want to 'hit' or 'stand'? ").lower()
            if action == 'hit':
                drawn_card = draw_card(game_deck)
                player_hand.append(drawn_card)
                print(f"You drew a {drawn_card}.")
            elif action == 'stand':
                break

        # Create a display of dealer's hand
        print(f"Dealer's Hand: {dealer_hand}")

        # Define dealers turn, if hand total < 17, draw a card if over stop drawing
        while hand_value(dealer_hand) < 17:
            drawn_card = draw_card(game_deck)
            dealer_hand.append(drawn_card)
            print(f"Dealer drew a {drawn_card}.")

        # Display players and dealers hand
        print(f"\nPlayer's Hand: {player_hand}")
        print(f"Dealer's Hand: {dealer_hand}")

        # Determine the outcome of the game
        player_score = hand_value(player_hand)
        dealer_score = hand_value(dealer_hand)

        if player_score > 21:
            print("Player busts! Dealer wins!")
        elif dealer_score > 21:
            print("Dealer busts! You win!")
        elif player_score > dealer_score:
            print("You win!")
        elif player_score < dealer_score:
            print("Dealer wins!")
        else:
            print("It's a tie!")

        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break


# Define main to run the game
if __name__ == "__main__":
    print("Welcome to Blackjack!")
    blackjack()
