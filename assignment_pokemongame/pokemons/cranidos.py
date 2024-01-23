from assignment_pokemongame import pokemon
#두개도스

class Cranidos(pokemon.Pokemon):
    """
    두개도스 종족값 350
    램펄드 종족값 495
    """
    def __init__(self):
        super().__init__()
        self.name = '두개도스'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 67
        self.race_attack_rate = 125
        self.race_defence_rate = 40
        self.race_special_attack_rate = 30
        self.race_special_defence_rate = 30
        self.race_speed_rate = 58

        self.xp = 0
        self.level = 12
        self.skill = {"따라가때리기" : (40,'physics'), "원시의힘" : (60,'special'), "사념의박치기" : (80,'physics'), "양날박치기" : (150,'physics')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def experience_value(self, target):
        super().experience_value(target)
        self.evolve()

    def attack(self, target, skill_number):
        super().attack(target, skill_number)

    def evolve(self):
        if self.level == 30:
            print('두개도스가 램펄드로 진화하였습니다!')
            self.name = '램펄드'
            self.race_hp = 97
            self.race_attack_rate = 165
            self.race_defence_rate = 60
            self.race_special_attack_rate = 65
            self.race_special_defence_rate = 50
            self.race_speed_rate = 58


if __name__ == '__main__':
    print(" ")


