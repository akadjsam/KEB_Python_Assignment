#모부기
import pokemon

class Turtwig(pokemon.Pokemon):
    """
    모부기 종족값 318
    수풀부기 종족값 405
    토대부기 종족값 525
    """
    def __init__(self):
        super().__init__()
        self.name = '모부기'
        # 초반 체력 초기화
        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 55
        self.race_attack_rate = 68
        self.race_defence_rate = 64
        self.race_special_attack_rate = 15
        self.race_special_defence_rate = 55
        self.race_speed_rate = 31

        self.xp = 0
        self.level = 5
        self.skill = {"몸통박치기" : (35,'physics') , "기가드레인" : (60,'special'), "우드해머" : (120,'physics'), "리프스톰" : (140,'special')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def experience_value(self, target):
        super().experience_value(target)
        self.evolve()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)

    def evolve(self):
        if self.level == 14:
            print('모부기가 수풀부기로 진화하였습니다!')
            self.name = '수풀부기'
            self.race_hp = 75
            self.race_attack_rate = 89
            self.race_defence_rate = 85
            self.race_special_attack_rate = 55
            self.race_special_defence_rate = 65
            self.race_speed_rate = 36

        elif self.level == 36:
            print('수풀부기가 토대부기로 진화하였습니다!')
            self.name = '토대부기'
            self.race_hp = 95
            self.race_attack_rate = 109
            self.race_defence_rate = 105
            self.race_special_attack_rate = 75
            self.race_special_defence_rate = 85
            self.race_speed_rate = 56

        if __name__ == '__main__':
            print("모부기 -> 수풀부기 -> 토대부기")