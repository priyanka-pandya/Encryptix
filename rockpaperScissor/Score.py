 
class Score:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0

    def update_score(self, result):
        if result == "You win!":
            self.user_score += 1
        elif result == "You lose!":
            self.computer_score += 1

    def get_scores(self):
        return self.user_score, self.computer_score
