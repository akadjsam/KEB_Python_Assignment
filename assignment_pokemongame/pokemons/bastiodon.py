from assignment_pokemongame import pokemon


class Bastiodon(pokemon.Pokemon):
    """
    바리톱스 종족값 495
    """
    def __init__(self):
        super().__init__()
        self.name = '바리톱스'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 60
        self.race_attack_rate = 52
        self.race_defence_rate = 168
        self.race_special_attack_rate = 47
        self.race_special_defence_rate = 138
        self.race_speed_rate = 30

        self.xp = 0
        self.level = 41
        self.skill = {"몸통박치기" : (35,'physics'), "원시의힘" : (60,'special'), "아이언헤드" : (80,'physics'), "지진" : (95,'physics')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)


if __name__ == '__main__':
    print(" ")