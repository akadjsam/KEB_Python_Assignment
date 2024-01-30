
from assignment_pokemongame import pokemon

class Shinx(pokemon.Pokemon):
    """
    꼬링크 종족값 263
    럭시오 종족값 363
    렌트라 종족값 530
    """
    def __init__(self):
        super().__init__()
        self.name = '꼬링크'
        #초반 체력 초기화
        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 45
        self.race_attack_rate = 65
        self.race_defence_rate = 34
        self.race_special_attack_rate = 40
        self.race_special_defence_rate = 34
        self.race_speed_rate = 45

        self.level_flag = 1
        self.xp = 0
        self.level = 5
        self.skill = {"물기" : (60,'physics') , "방전" : (80,'special'), "아이언테일" : (100,'physics'), "번개" : (120,'special')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def experience_value(self, target):
        super().experience_value(target)
        self.evolve()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)

    def evolve(self):
        if self.level == 15:
            if self.level_flag == 1:
                print('꼬링크가 럭시오로 진화하였습니다!')
                self.level_flag = 0
            self.name = '럭시오'
            self.race_hp = 60
            self.race_attack_rate = 85
            self.race_defence_rate = 49
            self.race_special_attack_rate = 60
            self.race_special_defence_rate = 49
            self.race_speed_rate = 60

        elif self.level >= 30:
            if self.level_flag == 0:
                print('럭시오가 렌트라로 진화하였습니다!')
                self.level_flag = 1
            self.name = '렌트라'
            self.race_hp = 80
            self.race_attack_rate = 120
            self.race_defence_rate = 79
            self.race_special_attack_rate = 95
            self.race_special_defence_rate = 79
            self.race_speed_rate = 70

if __name__ == '__main__':
    print(" ")
