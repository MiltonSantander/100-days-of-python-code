import random


class Dealer:
    def __init__(self):
        self.cards = {
            "full_deck": [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
            "user_cards": [],
            "cpu_cards": []
        }

    def deal_card(self):
        return random.choice(self.cards["full_deck"])

    def serve_new_hand(self):
        for _ in range(2):
            self.cards["user_cards"].append(self.deal_card())
            self.cards["cpu_cards"].append(self.deal_card())

    def change_ace_value(self, is_user_cards):
        if is_user_cards:
            self.cards["user_cards"].remove(11)
            self.cards["user_cards"].append(1)
        else:
            self.cards["cpu_cards"].remove(11)
            self.cards["cpu_cards"].append(1)

    def clear_hand(self):
        self.cards["user_cards"].clear()
        self.cards["cpu_cards"].clear()
