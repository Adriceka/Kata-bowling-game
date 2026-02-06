class ScoreCard:
    def __init__(self, scorecard):
        self.throws = self._parse_throws(scorecard)
        self.frames = self._build_frames()  

    def _parse_throws(self, scorecard):
        throws = []
        for symbol in scorecard:
            if symbol == 'X':          # strike
                throws.append(10)
            elif symbol == '-':        # miss / foul
                throws.append(0)
            elif symbol == '/':        # spare
                throws.append(10 - throws[-1])
            else:                      # pins knocked down
                throws.append(int(symbol))
        return throws

    def _build_frames(self):
        frames = []
        roll = 0
        for frame in range(10):
            if self.throws[roll] == 10:   # strike
                frames.append([10])
                roll += 1
            else:
                frames.append([self.throws[roll], self.throws[roll + 1]])
                roll += 2
        # Bonus throws in the 10th frame
        if roll < len(self.throws):
            frames[-1].extend(self.throws[roll:])
        return frames

    def score(self):
        game_score = 0
        roll = 0
        for frame in range(10):
            if self._is_strike(roll):
                game_score += 10 + self._strike_bonus(roll)
                roll += 1
            elif self._is_spare(roll):
                game_score += 10 + self._spare_bonus(roll)
                roll += 2
            else:
                game_score += self.throws[roll] + self.throws[roll + 1]
                roll += 2
        return game_score

    def _is_strike(self, roll):
        return self.throws[roll] == 10

    def _is_spare(self, roll):
        return self.throws[roll] + self.throws[roll + 1] == 10

    def _strike_bonus(self, roll):
        return self.throws[roll + 1] + self.throws[roll + 2]

    def _spare_bonus(self, roll):
        return self.throws[roll + 2]
