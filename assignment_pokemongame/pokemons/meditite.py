from assignment_pokemongame import pokemon


class Meditite(pokemon.Pokemon):
    """
    요가랑 종족값 280
    """
    def __init__(self):
        super().__init__()
        self.name = '요가랑'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 30
        self.race_attack_rate = 40
        self.race_defence_rate = 55
        self.race_special_attack_rate = 40
        self.race_special_defence_rate = 55
        self.race_speed_rate = 60

        self.xp = 0
        self.level = 28
        self.skill = {"염동력" : (50,'special'), "환상빔" : (65,'special'), "샤념의박치기" : (80,'physics'), "무릎차기" : (130,'special')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)


if __name__ == '__main__':
    print(" ")


