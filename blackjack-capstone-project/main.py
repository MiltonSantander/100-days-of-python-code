import user_interface
import dealer
import score

user_new_hand = []
cpu_new_hand = []


def play(param):
    if "n" == param or param == "y":
        if param == "y":
            serve_new_hand()
        elif param == "n":
            print("no se juegas")
            return
    else:
        new_user_input = user_interface.print_ask_to_play()
        play(new_user_input)


def serve_new_hand():
    cpu_new_hand.append(dealer.deal_card())
    cpu_score, cpu_cards = score.calculate_score(cpu_new_hand)

    user_new_hand.append(dealer.deal_card())
    user_new_hand.append(dealer.deal_card())
    user_score, user_cards = score.calculate_score(user_new_hand)
    if user_score == 21:
        user_interface.print_final_user_hand(str(user_cards), str(user_score))
        user_interface.print_final_cpu_hand(str(cpu_cards), str(cpu_score))
    else:
        user_interface.print_user_hand(str(user_cards), str(user_score))
        user_interface.print_cpu_hand(str(cpu_cards), str(cpu_score))


user_input = user_interface.print_ask_to_play()
play(user_input)
