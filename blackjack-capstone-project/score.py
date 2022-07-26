class Score:
    def __init__(self):
        self.scores = {
            "user_score": 0,
            "cpu_score": 0
        }

    def calculate_score(self, dealer_instance):
        self.scores["user_score"] = 0
        self.scores["cpu_score"] = 0

        for card in dealer_instance.cards["user_cards"]:
            self.scores["user_score"] += card
            if self.scores["user_score"] > 21 and 11 in dealer_instance.cards["user_cards"]:
                dealer_instance.change_ace_value(True)
                self.calculate_score(dealer_instance)

        for card in dealer_instance.cards["cpu_cards"]:
            self.scores["cpu_score"] += card
            if self.scores["cpu_score"] > 21 and 11 in dealer_instance.cards["cpu_cards"]:
                dealer_instance.change_ace_value(False)
                self.calculate_score(dealer_instance)
