from assignment_pokemongame import pokemon


class Gyarados(pokemon.Pokemon):
    """
    갸라도스 종족값 540
    """
    def __init__(self):
        super().__init__()
        self.name = '갸라도스'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 95
        self.race_attack_rate = 125
        self.race_defence_rate = 79
        self.race_special_attack_rate = 60
        self.race_special_defence_rate = 100
        self.race_speed_rate = 81

        self.xp = 0
        self.level = 33
        self.skill = {"난동부리기" : (90,'physics'), "물기" : (60,'physics'), "아쿠아테일" : (90,'physics'), "하이드로펌프" : (120,'special')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)


if __name__ == '__main__':
    print(" ")