import random
from logo import logo_blackjack


def deal_card():
    """Returs a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and returs the score calcuated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0 

    if 11 in cards and sum(cards > 21):
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has a Blackjack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over, You Lose"
    elif c_score > 21:
        return "Opponent went over. You Win"
    elif u_score > c_score:
        return "You Win"
    else:
        return "You Lose"


def play_game():
    print(logo_blackjack)

    user_cards =[]
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:    
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your card: {user_cards}     Your score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else : 
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score< 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
















# play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

# player_cards = (random.sample(cards,2))
# computers_first_card = (random.choice(cards))
# player_score = sum(player_cards)
# print(f"    Your cards: {player_cards}       Your score: {player_score}")
# print(f"    Computer's first card: {computers_first_card}")
# play_pass = input("Type 'y' to get another card, type 'n' to pass: ")


# computer_cards.append(computers_first_card)

# continue_playing = True

# while continue_playing:
    
#     if play_pass == "y":
#         player_cards.append(random.choice(cards))
#         computer_cards.append(random.choice(cards))
#         player_score = sum(player_cards)
#         computers_score = sum(computer_cards)
#         print(f"    Your cards: {player_cards}       Your score: {player_score}")
#         print(f"    Computer's cards: {computer_cards}")

#         if player_score > 21:
#             continue_playing = False
#             print("You Lose")
#         elif computers_score > 21:
#             continue_playing = False
#             print("You Won")
#         elif computers_score == player_score:
#             continue_playing =False
#             print("Its a draw")


#     elif play_pass == "n":
#         continue_playing = False

