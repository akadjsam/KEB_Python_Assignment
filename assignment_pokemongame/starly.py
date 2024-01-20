import pokemon
#찌르꼬

class Starly(pokemon.Pokemon):
    """
    찌르꼬 종족값 235
    찌르버드 종족값 340
    찌르호크 종족값 485
    """
    def __init__(self):
        super().__init__()
        self.name = '찌르꼬'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 30
        self.race_attack_rate = 55
        self.race_defence_rate = 30
        self.race_special_attack_rate = 30
        self.race_special_defence_rate = 30
        self.race_speed_rate = 60

        self.xp = 0
        self.level = 5
        self.skill = {"몸통박치기" : (35,'physics'), "날개치기" : (60,'physics'), "인파이트" : (120,'physics'), "브레이브버드" : (95,'physics')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def experience_value(self, target):
        super().experience_value(target)

    def attack(self, target, skill_number):
        super().attack(target, skill_number)

    def evolve(self):
        if self.level == 14:
            print('찌르꼬가 찌르버드로 진화하였습니다!')
            self.name = '찌르버드'
            self.race_hp = 55
            self.race_attack_rate = 75
            self.race_defence_rate = 50
            self.race_special_attack_rate = 40
            self.race_special_defence_rate = 40
            self.race_speed_rate = 80

        elif self.level == 34:
            print('찌르버드가 찌르호그로 진화하였습니다!')
            self.name = '찌르호크'
            self.race_hp = 85
            self.race_attack_rate = 120
            self.race_defence_rate = 70
            self.race_special_attack_rate = 50
            self.race_special_defence_rate = 60
            self.race_speed_rate = 100


if __name__ == '__main__':
    print("찌르꼬 -> 찌르버드 -> 찌르호크")


