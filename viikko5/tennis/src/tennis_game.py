class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = player1_name
        self.player2 = player2_name
        self.score = {player1_name: 0, player2_name: 0}
        self.d = {0: "Love",
                    1:"Fifteen",
                    2: "Thirty",
                    3: "Forty",
                    4: "Deuce"}

    def won_point(self, player_name):
        self.score[player_name] += 1

    def tie_score(self):
        tie_score = f"{self.d[self.score[self.player1]]}-All"
        return tie_score if "Deuce" not in tie_score else "Deuce"

    def four_or_more(self):
        dif = abs(self.score[self.player1] - self.score[self.player2])
        player = max(self.score, key=self.score.get)
        if dif > 1:
            return f"Win for {player}"
        else:
            return f"Advantage {player}"

    def get_score(self):
        if self.score[self.player1] == self.score[self.player2]:
            return self.tie_score()
        if self.score[self.player1] >= 4 or self.score[self.player2] >= 4:
            return self.four_or_more()
        return f"{self.d[self.score[self.player1]]}-{self.d[self.score[self.player2]]}"
