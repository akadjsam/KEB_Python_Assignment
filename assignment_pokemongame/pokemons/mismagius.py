from assignment_pokemongame import pokemon
class Mismagius(pokemon.Pokemon):
    """
    무우마직 종족값 495
    """
    def __init__(self):
        super().__init__()
        self.name = '무우마직'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 60
        self.race_attack_rate = 60
        self.race_defence_rate = 60
        self.race_special_attack_rate = 105
        self.race_special_defence_rate = 105
        self.race_speed_rate = 105

        self.xp = 0
        self.level = 34
        self.skill = {"사이코키네시스" : (90,'special'), "보복" : (50,'physics'), "악의파동" : (80,'special'), "섀도볼" : (80,'special')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)


if __name__ == '__main__':
    print(" ")