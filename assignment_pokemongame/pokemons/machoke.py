from assignment_pokemongame import pokemon


class Machoke(pokemon.Pokemon):
    """
    근육몬 종족값 405
    """
    def __init__(self):
        super().__init__()
        self.name = '근육몬'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 80
        self.race_attack_rate = 100
        self.race_defence_rate = 70
        self.race_special_attack_rate = 50
        self.race_special_defence_rate = 60
        self.race_speed_rate = 45

        self.xp = 0
        self.level = 32
        self.skill = {"잠깨움뺨치기" : (60,'physics'), "크로스촙" : (80,'physics'), "폭팔펀치" : (100,'physics'), "무릎차기" : (130,'physics')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)


if __name__ == '__main__':
    print(" ")