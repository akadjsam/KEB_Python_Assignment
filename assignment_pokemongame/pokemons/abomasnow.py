from assignment_pokemongame import pokemon


class Abomansnow(pokemon.Pokemon):
    """
    눈설왕 종족값 494
    """
    def __init__(self):
        super().__init__()
        self.name = '눈설왕'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 90
        self.race_attack_rate = 92
        self.race_defence_rate = 75
        self.race_special_attack_rate = 92
        self.race_special_defence_rate = 85
        self.race_speed_rate = 60

        self.xp = 0
        self.level = 42
        self.skill = {"냉동펀치" : (75,'physics'), "얼다바람" : (55,'special'), "우드해머" : (120,'physics'), "눈보라" : (120,'special')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)


if __name__ == '__main__':
    print(" ")