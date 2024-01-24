from assignment_pokemongame import pokemon


class Quagsire(pokemon.Pokemon):
    """
    누오 종족값 430
    """
    def __init__(self):
        super().__init__()
        self.name = '누오'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 95
        self.race_attack_rate = 85
        self.race_defence_rate = 85
        self.race_special_attack_rate = 65
        self.race_special_defence_rate = 65
        self.race_speed_rate = 35

        self.xp = 0
        self.level = 34
        self.skill = {"머드샷" : (50,'special'), "힘껏치기" : (80,'physics'), "지진" : (100,'physics'), "물대포" : (40,'special')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)


if __name__ == '__main__':
    print(" ")