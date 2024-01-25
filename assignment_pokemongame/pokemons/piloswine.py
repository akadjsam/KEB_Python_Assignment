from assignment_pokemongame import pokemon


class Piloswine(pokemon.Pokemon):
    """
    메꾸리 종족값 450
    """
    def __init__(self):
        super().__init__()
        self.name = '메꾸리'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 100
        self.race_attack_rate = 100
        self.race_defence_rate = 80
        self.race_special_attack_rate = 60
        self.race_special_defence_rate = 60
        self.race_speed_rate = 50

        self.xp = 0
        self.level = 40
        self.skill = {"얼음엄니" : (65,'physics'), "지진" : (100,'physics'), "진흙폭탄" : (65,'special'), "눈보라" : (120,'special')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)


if __name__ == '__main__':
    print(" ")