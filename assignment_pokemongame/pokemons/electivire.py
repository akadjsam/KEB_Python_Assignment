from assignment_pokemongame import pokemon

class Electivire(pokemon.Pokemon):
    """
    에레키블 종족값 540
    """
    def __init__(self):
        super().__init__()
        self.name = '에레키블'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 75
        self.race_attack_rate = 123
        self.race_defence_rate = 67
        self.race_special_attack_rate = 95
        self.race_special_defence_rate = 85
        self.race_speed_rate = 95

        self.xp = 0
        self.level = 40
        self.skill = {"불꽃펀치" : (75,'physics'), "10만볼트" : (95,'special'), "번개" : (120,'special'), "기가임팩트" : (150,'physics')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)


if __name__ == '__main__':
    print(" ")