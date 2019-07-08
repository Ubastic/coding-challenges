RANKS = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]


class Warrior:
    rank = property(lambda self: RANKS[self.level // 10])
    level = property(lambda self: self.experience // 100)

    def __init__(self):
        self.experience = 100
        self.achievements = []

    def battle(self, level):
        if not (1 <= level <= 100):
            return "Invalid level"
        elif level - self.level >= 5 and self.rank != RANKS[level // 10]:
            return "You've been defeated"
        elif self.level == level:
            result, exp = "A good fight", 10
        elif self.level - level == 1:
            result, exp = "A good fight", 5
        elif self.level - level > 1:
            result, exp = "Easy fight", 0
        else:
            diff = level - self.level
            result, exp = "An intense fight", 20 * diff ** 2

        self.experience = min((self.experience + exp), 10000)
        return result

    def training(self, args):
        desk, exp, level = args
        if level > self.level:
            return "Not strong enough"

        self.experience = min((self.experience + exp), 10000)
        self.achievements.append(desk)
        return desk