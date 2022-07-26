import user_interface
import dealer
import score

score = score.Score()
dealer = dealer.Dealer()


def play():
    dealer.cards["user_cards"] = []
    dealer.cards["cpu_cards"] = []
    user_input = user_interface.print_ask_to_play()
    if "n" == user_input or user_input == "y":
        if user_input == "y":
            dealer.serve_new_hand()
            check_winner(False)
        if user_input == "n":
            print("no se juega")
            return
    else:
        play()


def check_winner(game_over):
    score.calculate_score(dealer)
    if not game_over:
        if score.scores["user_score"] < 21:
            user_interface.print_user_hand(dealer.cards["user_cards"], score.scores["user_score"])
            user_interface.print_cpu_hand(dealer.cards["cpu_cards"])
            hit_or_pass()
        if score.scores["user_score"] > 21:
            user_interface.print_final_user_hand(dealer.cards["user_cards"], score.scores["user_score"])
            user_interface.print_final_cpu_hand(dealer.cards["cpu_cards"], score.scores["cpu_score"])
            user_interface.user_win(False)
            dealer.clear_hand()
            play()
    else:
        if score.scores["user_score"] < score.scores["cpu_score"] or score.scores["user_score"] > 21:
            user_interface.print_final_user_hand(dealer.cards["user_cards"], score.scores["user_score"])
            user_interface.print_final_cpu_hand(dealer.cards["cpu_cards"], score.scores["cpu_score"])
            user_interface.user_win(False)
            dealer.clear_hand()
            play()
        if score.scores["cpu_score"] < score.scores["user_score"] <= 21:
            user_interface.print_final_user_hand(dealer.cards["user_cards"], score.scores["user_score"])
            user_interface.print_final_cpu_hand(dealer.cards["cpu_cards"], score.scores["cpu_score"])
            user_interface.user_win(True)
            dealer.clear_hand()
            play()
        if score.scores["user_score"] == score.scores["cpu_score"]:
            user_interface.print_final_user_hand(dealer.cards["user_cards"], score.scores["user_score"])
            user_interface.print_final_cpu_hand(dealer.cards["cpu_cards"], score.scores["cpu_score"])
            user_interface.user_win(False)
            dealer.clear_hand()
            play()


def hit_or_pass():
    user_input = user_interface.print_hit_or_pass()
    if user_input == "y":
        dealer.cards["user_cards"].append(dealer.deal_card())
        check_winner(False)
    if user_input == "n":
        check_winner(True)
    else:
        hit_or_pass()


play()
