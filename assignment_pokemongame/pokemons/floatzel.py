from assignment_pokemongame import pokemon


class Floatzel(pokemon.Pokemon):
    """
    플로젤 종족값 495
    """
    def __init__(self):
        super().__init__()
        self.name = '플로젤'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 85
        self.race_attack_rate = 105
        self.race_defence_rate = 55
        self.race_special_attack_rate = 85
        self.race_special_defence_rate = 50
        self.race_speed_rate = 115

        self.xp = 0
        self.level = 37
        self.skill = {"얼음엄니" : (65,'physics'), "물대포" : (40,'special'), "깨물어부수기" : (80,'physics'), "파도타기" : (95,'special')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)


if __name__ == '__main__':
    print(" ")