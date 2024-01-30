#피카츄
from assignment_pokemongame import pokemon

class Pikachu(pokemon.Pokemon):
    """
    피츄 종족값 314
    피카츄 종족값 405
    라이츄 종족값 530
    """
    def __init__(self):
        super().__init__()
        self.name = '피츄'
        #초반 체력 초기화
        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 20
        self.race_attack_rate = 40
        self.race_defence_rate = 15
        self.race_special_attack_rate = 35
        self.race_special_defence_rate = 35
        self.race_speed_rate = 60

        self.level_flag = 1
        self.xp = 0
        self.level = 15
        self.skill = {"힘껏펀치" : (150,'physics') , "번개" : (120,'special'), "아이언테일" : (100,'physics'), "기합구슬" : (120,'special')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def experience_value(self, target):
        super().experience_value(target)
        self.evolve()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)

    def evolve(self):
        if self.level == 16:
            if self.level_flag == 1:
                print('피츄가 피카츄로 진화하였습니다!')
                self.level_flag = 0
            self.name = '피카츄'
            self.race_hp = 35
            self.race_attack_rate = 55
            self.race_defence_rate = 40
            self.race_special_attack_rate = 50
            self.race_special_defence_rate = 50
            self.race_speed_rate = 90

        elif self.level >= 36:
            if self.level_flag == 0:
                print('피카츄가 라이츄로 진화하였습니다!')
                self.level_flag = 1
            self.name = '라이츄'
            self.race_hp = 60
            self.race_attack_rate = 90
            self.race_defence_rate = 55
            self.race_special_attack_rate = 90
            self.race_special_defence_rate = 80
            self.race_speed_rate = 110

if __name__ == '__main__':
    print(" ")
