class Score:
    def __init__(self):
        self.scores = {
            "user_score": 0,
            "cpu_score": 0
        }

    def calculate_score(self, user_cards, cpu_cards):
        self.scores["user_score"] = 0
        self.scores["cpu_score"] = 0

        for card in user_cards:
            self.scores["user_score"] += card

        for card in cpu_cards:
            self.scores["cpu_score"] += card
