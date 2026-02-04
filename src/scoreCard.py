class ScoreCard:
    def __init__(self, score_string):
        self.rolls = self._parse_rolls(score_string)
        self.frame_pins = self._build_frames()  
    def _parse_rolls(self, score_string):
        rolls = []
        for char in score_string:
            if char == 'X':          # strike
                rolls.append(10)
            elif char == '-':        # falla la tirada
                rolls.append(0)
            elif char == '/':        # semipleno
                rolls.append(10 - rolls[-1])
            else:                    # número de pines derribados
                rolls.append(int(char))
        return rolls

    def _build_frames(self):
        frames = []
        i = 0
        for frame in range(10):
            if self.rolls[i] == 10:  # strike
                frames.append([10])
                i += 1
            else:
                frames.append([self.rolls[i], self.rolls[i+1]])
                i += 2
        # Tiradas extra del décimo frame
        if i < len(self.rolls):
            frames[-1].extend(self.rolls[i:])
        return frames

    def score(self):
        # Calcula el puntaje total de la partida.
        
        total_score = 0
        roll_index = 0
        for frame in range(10):
            if self._is_strike(roll_index):
                total_score += 10 + self._strike_bonus(roll_index)
                roll_index += 1
            elif self._is_spare(roll_index):
                total_score += 10 + self._spare_bonus(roll_index)
                roll_index += 2
            else:
                total_score += self.rolls[roll_index] + self.rolls[roll_index + 1]
                roll_index += 2
        return total_score

    def _is_strike(self, roll_index):
        return self.rolls[roll_index] == 10

    def _is_spare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10

    def _strike_bonus(self, roll_index):
        return self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def _spare_bonus(self, roll_index):
        return self.rolls[roll_index + 2]
