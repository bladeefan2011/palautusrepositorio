class TennisGame:
    score_names = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1_score += 1
        else:
            self.p2_score += 1

    def get_score(self):
        if self.p1_score == self.p2_score:
            return self.even_score()
        elif self.p1_score >= 4 or self.p2_score >= 4:
            return self.both_score_four()
        else: 
            return self.scoring()
        

    def even_score(self):
        if self.p1_score < 3:
            return self.score_names[self.p1_score] + "-All"
        else:
            return "Deuce"
        
        
    def both_score_four(self):
        difference = self.p1_score - self. p2_score
        if difference == 1:
            return "Advantage player1"
        elif difference == -1:
            return "Advantage player2"
        elif difference >= 2:
            return"Win for player1"
        else:
            return "Win for player2"
        

    def scoring(self):
        p1_res = self.score_names[self.p1_score]
        p2_res = self.score_names[self.p2_score]
        return f"{p1_res}-{p2_res}"
