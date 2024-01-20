#팽도리
import pokemon

class Piplup(pokemon.Pokemon):
    """
    팽도리 종족값 314
    팽태자 종족값 405
    엠페르트 종족값 530
    """
    def __init__(self):
        super().__init__()
        self.name = '팽도리'
        self.hp = 53
        self.attack_rate = 51
        self.defence_rate = 53
        self.special_attack_rate = 61
        self.special_defence_rate = 56
        self.speed_rate = 40
        self.xp = 0
        self.level = 5
        self.skill = {"막치기" : (40,'physics') , "거품광선" : (65,'special'), "회전부리" : (80,'physics'), "하이드로펌프" : (120,'special')}

    def experience_value(self, target):
        super().experience_value(target)

    def attack(self, target, skill_number):
        super().attack(target, skill_number)

if __name__ == '__main__':
    print("팽도리 -> 팽태자 -> 엠페르트")
