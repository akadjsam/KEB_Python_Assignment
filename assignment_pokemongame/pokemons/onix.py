from assignment_pokemongame import pokemon
#롱스톤

class Onix(pokemon.Pokemon):
    """
    롱스톤 종족값 385
    강철톤 종족값 510
    """
    def __init__(self):
        super().__init__()
        self.name = '롱스톤'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 35
        self.race_attack_rate = 45
        self.race_defence_rate = 160
        self.race_special_attack_rate = 30
        self.race_special_defence_rate = 45
        self.race_speed_rate = 70
        self.level_flag = 1

        self.xp = 0
        self.level = 10
        self.skill = {"번개엄니" : (65,'physics'), "용의숨결" : (60,'special'), "아이언테일" : (100,'physics'), "이판사판태클" : (120,'physics')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def experience_value(self, target):
        super().experience_value(target)
        self.evolve()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)

    def evolve(self):
        if self.level == 36:
            if self.level_flag == 1:
                print('롱스톤이 강철톤으로 진화하였습니다!')
                self.level_flag = 0
            self.name = '강철톤'
            self.race_hp = 75
            self.race_attack_rate = 85
            self.race_defence_rate = 200
            self.race_special_attack_rate = 55
            self.race_special_defence_rate = 65
            self.race_speed_rate = 30


if __name__ == '__main__':
    print(" ")


