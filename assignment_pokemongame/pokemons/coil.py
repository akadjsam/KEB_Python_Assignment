from assignment_pokemongame import pokemon


class Coil(pokemon.Pokemon):
    """
    레어코일 465
    """
    def __init__(self):
        super().__init__()
        self.name = '레어코일'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 50
        self.race_attack_rate = 60
        self.race_defence_rate = 98
        self.race_special_attack_rate = 120
        self.race_special_defence_rate = 70
        self.race_speed_rate = 70

        self.xp = 0
        self.level = 37
        self.skill = {"스파크" : (65,'physics'), "방전" : (80,'special'), "마그넷봄" : (60,'physics'), "전자포" : (120,'special')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)


if __name__ == '__main__':
    print(" ")