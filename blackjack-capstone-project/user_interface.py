ask_to_play = "Do you want to play a game of Blackjack? Type 'y' or 'n':"
user_hand = "Your cards: #, current score: $"
cpu_hand = "Computer's first card: #"
hit_or_pass = "Type 'y' to get another card, type 'n' to pass: "
final_user_hand = "Your final hand: #, final score: $"
final_cpu_hand = "Computer's final hand: #, final score: $"


def print_ask_to_play():
    return input(ask_to_play)


def print_user_hand(user_cards, user_score):
    print((user_hand.replace("#", user_cards)).replace("$", user_score))


def print_cpu_hand(cpu_cards, cpu_score):
    print((user_hand.replace("#", cpu_cards)).replace("$", cpu_score))


def print_hit_or_pass():
    return input(hit_or_pass)


def print_final_user_hand(user_cards, user_score):
    print((final_user_hand.replace("#", user_cards)).replace("$", user_score))


def print_final_cpu_hand(cpu_cards, cpu_score):
    print((final_cpu_hand.replace("#", cpu_cards)).replace("$", cpu_score))

