def calculate_score(cards):
    score = 0
    for index, card in enumerate(cards):
        score += card
        if score > 21 and card == 11:
            score -= 10
            cards[index] = 1
    return score, cards
