from assignment_pokemongame import pokemon


class Sneasel(pokemon.Pokemon):
    """
    포푸니 종족값 495
    """
    def __init__(self):
        super().__init__()
        self.name = '포푸니'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 55
        self.race_attack_rate = 95
        self.race_defence_rate = 55
        self.race_special_attack_rate = 35
        self.race_special_defence_rate = 75
        self.race_speed_rate = 115

        self.xp = 0
        self.level = 40
        self.skill = {"할퀴기" : (40,'physics'), "베어가르기" : (70,'physics'), "메탈크로우" : (50,'physics'), "얼음뭉치" : (40,'physics')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)


if __name__ == '__main__':
    print(" ")