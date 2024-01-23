from assignment_pokemongame import pokemon
#로즈레이드 체육관 관장용 체종진화체만 만듦

class Roserade(pokemon.Pokemon):
    """
    로즈레이드 종족값 515
    """
    def __init__(self):
        super().__init__()
        self.name = '로즈레이드'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 60
        self.race_attack_rate = 70
        self.race_defence_rate = 65
        self.race_special_attack_rate = 125
        self.race_special_defence_rate = 105
        self.race_speed_rate = 90

        self.xp = 0
        self.level = 22
        self.skill = {"웨더볼" : (50,'special'), "메지컬리프" : (60,'special'), "독찌르기" : (80,'physics'), "솔라빔" : (120,'special')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)


if __name__ == '__main__':
    print(" ")


