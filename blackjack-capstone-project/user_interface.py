def print_ask_to_play():
    return input("Do you want to play a game of Blackjack? Type 'y' or 'n':")


def print_user_hand(user_cards, user_score):
    print(f"Your cards: {user_cards}, current score: {user_score}")


def print_cpu_hand(cpu_cards, cpu_score):
    print(f"Computer's first card: {cpu_cards}, current score: {cpu_score}")


def print_hit_or_pass():
    return input("Type 'y' to get another card, type 'n' to pass: ")


def print_final_user_hand(user_cards, user_score):
    print(f"Your final hand: {user_cards}, final score: {user_score}")


def print_final_cpu_hand(cpu_cards, cpu_score):
    print(f"Computer's final hand: {cpu_cards}, final score: {cpu_score}")


def user_win(param):
    if param:
        print("Ganaste! 🎉")
    else:
        print("Has perdido ☹")
