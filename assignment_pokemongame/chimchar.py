import pokemon
#불꽃숭이

class Chimchar(pokemon.Pokemon):
    """
    불꽃숭이 종족값 309
    파이숭이 종족값 405
    초염몽 종족값 534
    """
    def __init__(self):
        super().__init__()
        self.name = '불꽃숭이'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 44
        self.race_attack_rate = 58
        self.race_defence_rate = 44
        self.race_special_attack_rate = 58
        self.race_special_defence_rate = 44
        self.race_speed_rate = 61

        self.xp = 0
        self.level = 5
        self.skill = {"할퀴기" : (40,'physics'), "불꽃세레" : (40,'special'), "인파이트" : (120,'physics'), "화염방사" : (95,'special')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def experience_value(self, target):
        super().experience_value(target)

    def attack(self, target, skill_number):
        super().attack(target, skill_number)

    def evolve(self):
        if self.level == 14:
            print('불꽃숭이가 파이숭이로 진화하였습니다!')
            self.name = '파이숭이'
            self.race_hp = 64
            self.race_attack_rate = 78
            self.race_defence_rate = 52
            self.race_special_attack_rate = 78
            self.race_special_defence_rate = 52
            self.race_speed_rate = 81

        elif self.level == 36:
            print('파이숭이가 초염몽으로 진화하였습니다!')
            self.name = '초염몽'
            self.race_hp = 76
            self.race_attack_rate = 104
            self.race_defence_rate = 71
            self.race_special_attack_rate = 104
            self.race_special_defence_rate = 71
            self.race_speed_rate = 108


if __name__ == '__main__':
    print("불꽃숭이 -> 파이숭이 -> 초염몽")


