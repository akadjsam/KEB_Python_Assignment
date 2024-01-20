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
        self.hp = 44
        self.attack_rate = 58
        self.defence_rate = 44
        self.special_attack_rate = 58
        self.special_defence_rate = 44
        self.speed_rate = 61
        self.xp = 0
        self.level = 5
        self.skill = {"할퀴기" : (40,'physics'), "불꽃세레" : (40,'special'), "인파이트" : (120,'physics'), "화염방사" : (95,'special')}

    def experience_value(self, target):
        super().experience_value(target)

    def attack(self, target, skill_number):
        super().attack(target, skill_number)



if __name__ == '__main__':
    print("불꽃숭이 -> 파이숭이 -> 초염몽")


