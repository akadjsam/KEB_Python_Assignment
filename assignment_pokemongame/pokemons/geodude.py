from assignment_pokemongame import pokemon
#꼬마돌

class Geodude(pokemon.Pokemon):
    """
    꼬마돌 종족값 300
    데구리 종족값 390
    딱구리 종족값 495
    """
    def __init__(self):
        super().__init__()
        self.name = '꼬마돌'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 40
        self.race_attack_rate = 80
        self.race_defence_rate = 100
        self.race_special_attack_rate = 30
        self.race_special_defence_rate = 30
        self.race_speed_rate = 20

        self.xp = 0
        self.level = 10
        self.skill = {"몸통박치기" : (35,'physics'), "지진" : (100,'physics'), "돌떨구기" : (50,'physics'), "이판사판태클" : (120,'physics')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def experience_value(self, target):
        super().experience_value(target)
        self.evolve()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)

    def evolve(self):
        if self.level == 25:
            print('꼬마돌이 데구리로 진화하였습니다!')
            self.name = '데구리'
            self.race_hp = 55
            self.race_attack_rate = 95
            self.race_defence_rate = 115
            self.race_special_attack_rate = 45
            self.race_special_defence_rate = 45
            self.race_speed_rate = 35

        elif self.level == 45:
            print('데구리가 딱구리로 진화하였습니다!')
            self.name = '딱구리'
            self.race_hp = 80
            self.race_attack_rate = 120
            self.race_defence_rate = 130
            self.race_special_attack_rate = 55
            self.race_special_defence_rate = 65
            self.race_speed_rate = 45


if __name__ == '__main__':
    print(" ")


