import pokemon
#딥상어동

class Gible(pokemon.Pokemon):
    """
    딥상어동 종족값 300
    한바이트 종족값 410
    한카리아스 종족값 600
    """
    def __init__(self):
        super().__init__()
        self.name = '딥상어동'

        self.hp = 0
        self.attack_rate = 0
        self.defence_rate = 0
        self.special_attack_rate = 0
        self.special_defence_rate = 0
        self.speed_rate = 0

        self.race_hp = 58
        self.race_attack_rate = 70
        self.race_defence_rate = 45
        self.race_special_attack_rate = 40
        self.race_special_defence_rate = 45
        self.race_speed_rate = 42

        self.xp = 0
        self.level = 5
        self.skill = {"드래곤크루" : (80,'physics'), "드래곤다이브" : (100,'physics'), "지진" : (100,'physics'), "불대문자" : (120,'special')}

    def ability(self): #포켓몬 실제 능력치 계산
        super().ability()

    def experience_value(self, target):
        super().experience_value(target)

    def attack(self, target, skill_number):
        super().attack(target, skill_number)

    def evolve(self):
        if self.level == 24:
            print('딥상어동이 한바이트로 진화하였습니다!')
            self.name = '한바이트'
            self.race_hp = 68
            self.race_attack_rate = 90
            self.race_defence_rate = 65
            self.race_special_attack_rate = 50
            self.race_special_defence_rate = 55
            self.race_speed_rate = 55

        elif self.level == 48:
            print('한바이트가 한카리아스로 진화하였습니다!')
            self.name = '한카리아스'
            self.race_hp = 108
            self.race_attack_rate = 130
            self.race_defence_rate = 95
            self.race_special_attack_rate = 80
            self.race_special_defence_rate = 85
            self.race_speed_rate = 102


if __name__ == '__main__':
    print("찌르꼬 -> 찌르버드 -> 찌르호크")


