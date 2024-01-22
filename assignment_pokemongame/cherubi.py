import pokemon
#체리버

class Cherubi(pokemon.Pokemon):
    """
    체리버 종족값 275
    체리꼬 종족값 450
    """
    def __init__(self):
        super().__init__()
        self.name = '체리버'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 45
        self.race_attack_rate = 35
        self.race_defence_rate = 45
        self.race_special_attack_rate = 62
        self.race_special_defence_rate = 53
        self.race_speed_rate = 35

        self.xp = 0
        self.level = 10
        self.skill = {"몸통박치기" : (40,'physics'), "에너지볼" : (80,'special'), "이판사판태클" : (120,'physics'), "솔라빔" : (120,'special')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def experience_value(self, target):
        super().experience_value(target)
        self.evolve()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)

    def evolve(self):
        if self.level == 36:
            print('체리버가 체리꼬로 진화하였습니다!')
            self.name = '체리버'
            self.race_hp = 70
            self.race_attack_rate = 60
            self.race_defence_rate = 70
            self.race_special_attack_rate = 87
            self.race_special_defence_rate = 78
            self.race_speed_rate = 85


if __name__ == '__main__':
    print(" ")


