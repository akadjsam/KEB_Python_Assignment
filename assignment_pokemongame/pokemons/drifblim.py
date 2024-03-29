from assignment_pokemongame import pokemon
class Drifblim(pokemon.Pokemon):
    """
    둥실라이드 종족값 498
    """
    def __init__(self):
        super().__init__()
        self.name = '둥실라이드'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 150
        self.race_attack_rate = 80
        self.race_defence_rate = 44
        self.race_special_attack_rate = 90
        self.race_special_defence_rate = 54
        self.race_speed_rate = 80

        self.xp = 0
        self.level = 34
        self.skill = {"놀래키기" : (30,'physics'), "보복" : (50,'physics'), "괴상한바람" : (60,'special'), "섀도볼" : (80,'special')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)


if __name__ == '__main__':
    print(" ")