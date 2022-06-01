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

    def change_ace_value(self, cards):
        cards.remove(11)
        cards.append(1)
