#팽도리
from assignment_pokemongame import pokemon

class Piplup(pokemon.Pokemon):
    """
    팽도리 종족값 314
    팽태자 종족값 405
    엠페르트 종족값 530
    """
    def __init__(self):
        super().__init__()
        self.name = '팽도리'
        #초반 체력 초기화
        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 53
        self.race_attack_rate = 51
        self.race_defence_rate = 53
        self.race_special_attack_rate = 61
        self.race_special_defence_rate = 56
        self.race_speed_rate = 40

        self.xp = 0
        self.level = 5
        self.skill = {"막치기" : (40,'physics') , "거품광선" : (65,'special'), "회전부리" : (80,'physics'), "하이드로펌프" : (120,'special')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def experience_value(self, target):
        super().experience_value(target)
        self.evolve()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)

    def evolve(self):
        if self.level == 16:
            print('팽도리가 팽태자로 진화하였습니다!')
            self.name = '팽태자'
            self.race_hp = 64
            self.race_attack_rate = 66
            self.race_defence_rate = 68
            self.race_special_attack_rate = 81
            self.race_special_defence_rate = 76
            self.race_speed_rate = 50

        elif self.level == 36:
            print('팽태자가 엠페르트로 진화하였습니다!')
            self.name = '엠페르트'
            self.race_hp = 84
            self.race_attack_rate = 86
            self.race_defence_rate = 88
            self.race_special_attack_rate = 111
            self.race_special_defence_rate = 101
            self.race_speed_rate = 60

if __name__ == '__main__':
    print("팽도리 -> 팽태자 -> 엠페르트")
