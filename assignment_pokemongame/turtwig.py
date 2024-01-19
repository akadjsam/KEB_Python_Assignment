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
        self.hp = 55
        self.attack_rate = 68
        self.defence_rate = 64
        self.special_attack_rate = 45
        self.special_defence_rate = 55
        self.speed_rate = 31
        self.level = 5
        self.skill = {"몸통박치기" : (35,'physics') , "기가드레인" : (60,'special'), "우드해머" : (120,'physics'), "리프스톰" : (140,'special')}

    def attack(self, target, skill_number):
        super().attack(target, skill_number)

        if __name__ == '__main__':
            print("모부기 -> 수풀부기 -> 토대부기")