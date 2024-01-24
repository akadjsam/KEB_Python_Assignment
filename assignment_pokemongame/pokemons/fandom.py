from assignment_pokemongame import pokemon
class Fandom(pokemon.Pokemon):
    """
    팬텀 종족값 500
    """
    def __init__(self):
        super().__init__()
        self.name = '팬텀'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 60
        self.race_attack_rate = 65
        self.race_defence_rate = 60
        self.race_special_attack_rate = 130
        self.race_special_defence_rate = 75
        self.race_speed_rate = 110

        self.xp = 0
        self.level = 34
        self.skill = {"섀도펀치" : (60,'physics'), "보복" : (50,'physics'), "악의파동" : (80,'special'), "섀도볼" : (80,'special')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)


if __name__ == '__main__':
    print(" ")