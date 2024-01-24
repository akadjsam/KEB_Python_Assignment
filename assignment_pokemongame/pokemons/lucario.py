from assignment_pokemongame import pokemon


class Lucario(pokemon.Pokemon):
    """
    루카리오 종족값 525
    """
    def __init__(self):
        super().__init__()
        self.name = '루카리오'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 70
        self.race_attack_rate = 110
        self.race_defence_rate = 70
        self.race_special_attack_rate = 115
        self.race_special_defence_rate = 70
        self.race_speed_rate = 90

        self.xp = 0
        self.level = 29
        self.skill = {"발경" : (60,'physics'), "파동탄" : (90,'special'), "인파이트" : (120,'physics'), "악의파동" : (80,'special')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)


if __name__ == '__main__':
    print(" ")