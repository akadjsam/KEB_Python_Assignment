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
        self.skill = {"할퀴기" : (0.4,'physics') , "불꽃세레" : (0.5,'special'), "인파이트" : (1.0,'physics'), "화염방사" : (0.5,'special')}

    def attack(self, target, skill_number):
        super().attack(target, skill_number)


