from assignment_pokemongame import pokemon

class Jolteon(pokemon.Pokemon):
    """
    쥬피썬더 종족값 525
    """
    def __init__(self):
        super().__init__()
        self.name = '쥬피썬더'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 65
        self.race_attack_rate = 65
        self.race_defence_rate = 60
        self.race_special_attack_rate = 110
        self.race_special_defence_rate = 95
        self.race_speed_rate = 130

        self.xp = 0
        self.level = 42
        self.skill = {"번개엄니" : (65,'physics'), "10만볼트" : (95,'special'), "아이언테일" : (100,'physics'), "번개" : (120,'special')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)


if __name__ == '__main__':
    print(" ")