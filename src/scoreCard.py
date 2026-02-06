class ScoreCard:

    # constructor que recibe una cadena de tiradas y la convierte en una lista de enteros
    STRIKE_PINS = 10
    TOTAL_FRAMES = 10

    def __init__(self, scorecard):
        self.scorecard = scorecard
        self.throws = []  # almaceno las tiradas parseadas

        for symbol in self.scorecard:  # recorre cada carácter en la scorecard
            if symbol == 'X':          # strike
                self.throws.append(self.STRIKE_PINS)
            elif symbol == '-':        # miss / foul
                self.throws.append(0)
            elif symbol == '/':        # spare
                self.throws.append(self.STRIKE_PINS - self.throws[-1])
            else:                      # pins derribados
                self.throws.append(int(symbol))

    def score(self):
        game_score = 0
        roll = 0

        for _ in range(self.TOTAL_FRAMES):  # 10 frames
            if self._is_strike(roll):                    # strike
                game_score += self.STRIKE_PINS + self._strike_bonus(roll)
                roll += 1
            elif self._is_spare(roll):                    # spare
                game_score += self.STRIKE_PINS + self._spare_bonus(roll)
                roll += 2
            else:                                         # open frame
                first_throw = self.throws[roll]
                second_throw = self.throws[roll + 1] if roll + 1 < len(self.throws) else 0
                game_score += first_throw + second_throw
                roll += 2

        return game_score

    def _is_strike(self, roll):
        return self.throws[roll] == self.STRIKE_PINS

    def _is_spare(self, roll):
        return (roll + 1) < len(self.throws) and \
               (self.throws[roll] + self.throws[roll + 1] == self.STRIKE_PINS)

    def _strike_bonus(self, roll):
        bonus = 0
        if roll + 1 < len(self.throws):
            bonus += self.throws[roll + 1]
        if roll + 2 < len(self.throws):
            bonus += self.throws[roll + 2]
        return bonus

    def _spare_bonus(self, roll):
        return self.throws[roll + 2] if (roll + 2) < len(self.throws) else 0
