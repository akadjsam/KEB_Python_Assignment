from assignment_pokemongame import pokemon


class Froslass(pokemon.Pokemon):
    """
    눈여아 종족값 480
    """
    def __init__(self):
        super().__init__()
        self.name = '눈여아'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 70
        self.race_attack_rate = 80
        self.race_defence_rate = 70
        self.race_special_attack_rate = 80
        self.race_special_defence_rate = 70
        self.race_speed_rate = 110

        self.xp = 0
        self.level = 44
        self.skill = {"얼음뭉치" : (40,'physics'), "괴상한바람" : (60,'special'), "잠깨움뺨치기" : (60,'physics'), "눈보라" : (120,'special')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)


if __name__ == '__main__':
    print(" ")