import random
import numpy as np

# Suits and Ranks

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# deck

deck = []
suit_index = 0
while suit_index < len(suits):
    rank_index = 0
    while rank_index < len(ranks):
        card = ranks[rank_index] + " of " + suits[suit_index]
        deck.append(card)
        rank_index = rank_index + 1
    suit_index = suit_index + 1

# Shuffle

random.shuffle(deck)

# Deal cards

players = []
player_number = 0
while player_number < 4:
    hand = deck[player_number * 13 : (player_number + 1) * 13]
    players.append(hand)
    player_number = player_number + 1

# select the dealer

dealer = random.randint(0, 3)

# hukem choose a hukm

trump_chooser = (dealer + 1) % 4
trump_suit = random.choice(suits)

# Display

print("Dealer: Player", dealer)

print("Trump chooser: Player", trump_chooser)

print("Trump suit:", trump_suit)

print("\nPlayer hands:")

display_index = 0

while display_index < 4:

    print("Player", display_index, ":", players[display_index])

    display_index = display_index + 1

# rank values

rank_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


# which player played 

played_cards = []

played_by = []


# starting player

starting_player = trump_chooser


# Players turn

turns = []
turn_index = 0
while turn_index < 4:
    current_player = (starting_player + turn_index) % 4
    turns.append(current_player)
    turn_index = turn_index + 1

# the first card

lead_suit = " "

# players play

turn_index = 0
while turn_index < len(turns):
    current_player = turns[turn_index]
    hand = players[current_player]
    

# playable card 

    card_index = 0
    chosen_card = " "
    while card_index < len(hand):
        card = hand[card_index]
        card_rank, card_suit = card.split(" of ")
        
        if turn_index == 0:


# First player

            chosen_card = card
            lead_suit = card_suit
            break
        else:


# follow suit

            if card_suit == lead_suit:
                chosen_card = card
                break
        card_index = card_index + 1
    
#first available card

    if chosen_card == "":

        chosen_card = hand[0]
    
# Remove card

    players[current_player].remove(chosen_card)

    played_cards.append(chosen_card)

    played_by.append(current_player)
    
    print("Player", current_player, "played", chosen_card)
    
    turn_index = turn_index + 1

# winner of round

highest_value = -1

winning_player = " "

round_index = 0


while round_index < len(played_cards):

    card = played_cards[round_index]

    player = played_by[round_index]

    card_rank, card_suit = card.split(" of ")

    card_value = rank_values.index(card_rank)
    
    is_trump = card_suit == trump_suit

    is_lead = card_suit == lead_suit

    if winning_player == "":
        highest_value = card_value

        winning_player = player

        winning_card_suit = card_suit

    else:
        if winning_card_suit == trump_suit:

# Current winning card is hukem

            if is_trump and card_value > highest_value:

                highest_value = card_value

                winning_player = player

        elif is_trump:

# New card is hukm

            highest_value = card_value

            winning_player = player

            winning_card_suit = trump_suit

        elif card_suit == winning_card_suit and card_value > highest_value:


# Same suit, higher value

            highest_value = card_value

            winning_player = player

    round_index = round_index + 1

print("\nWinner of the round: Player", winning_player)


# Score

team1_score = 0  # Players 0 and 2


team2_score = 0  # Players 1 and 3


# Start with hukem

starting_player = trump_chooser


# rounds

while team1_score < 7 and team2_score < 7:
    

# One Round

    played_cards = []

    played_by = []

    turns = []

    turn_index = 0

    while turn_index < 4:

        current_player = (starting_player + turn_index) % 4

        turns.append(current_player)

        turn_index = turn_index + 1

    lead_suit = " "

    turn_index = 0

    while turn_index < len(turns):

        current_player = turns[turn_index]

        hand = players[current_player]

        
        card_index = 0

        chosen_card = " "

        while card_index < len(hand):

            card = hand[card_index]

            card_rank, card_suit = card.split(" of ")

            if turn_index == 0:

                chosen_card = card

                lead_suit = card_suit

                break

            else:
                if card_suit == lead_suit:
                    chosen_card = card
                    break

            card_index = card_index + 1

        if chosen_card is " ":

            chosen_card = hand[0]

        players[current_player].remove(chosen_card)

        played_cards.append(chosen_card)

        played_by.append(current_player)

        print("Player", current_player, "played", chosen_card)

        turn_index = turn_index + 1


    # Winner of Round

    highest_value = -1

    winning_player = " "

    round_index = 0

    while round_index < len(played_cards):

        card = played_cards[round_index]

        player = played_by[round_index]

        card_rank, card_suit = card.split(" of ")

        card_value = rank_values.index(card_rank)

        is_trump = card_suit == trump_suit

        is_lead = card_suit == lead_suit

        if winning_player == "":


            highest_value = card_value

            winning_player = player

            winning_card_suit = card_suit

        else:
            if winning_card_suit == trump_suit:
                if is_trump and card_value > highest_value:
                    highest_value = card_value
                    winning_player = player

            elif is_trump:
                highest_value = card_value
                winning_player = player
                winning_card_suit = trump_suit
                
            elif card_suit == winning_card_suit and card_value > highest_value:
                highest_value = card_value
                winning_player = player

        round_index = round_index + 1

    print(" Round winner: Player", winning_player)

 # Score

    if winning_player == 0 or winning_player == 2:

        team1_score = team1_score + 1

    else:
        team2_score = team2_score + 1

    print("Team 1 (Players 0 & 2) score:", team1_score)

    print("Team 2 (Players 1 & 3) score:", team2_score)


 # starts next round

    starting_player = winning_player

# End of Game

if team1_score >= 7:

    print("Team 1 wins the game")

else:
    print(" Team 2 wins the game")
