class Pokemon:
    def __init__(self):
        self.name = None
        self.hp = None
        self.attack_rate = None
        self.defence_rate = None
        self.special_attack_rate = None
        self.special_defence_rate = None
        self.speed_rate = None

        self.race_name = None
        self.race_hp = None
        self.race_attack_rate = None
        self.race_defence_rate = None
        self.race_special_attack_rate = None
        self.race_special_defence_rate = None
        self.race_speed_rate = None

        self.level = 0
        self.xp = 0
        self.skill = {}

    # 능력치 설정 기준 : (종족값 * 2 + 개체값(15로 고정) ) / (레벨/100) + 10 + 레벨
    def ability(self):
        self.hp = int((self.race_hp * 2 + 15) * (self.level / 100) + 10 + self.level)
        self.attack_rate = int((self.race_attack_rate * 2 + 15) * (self.level / 100) + 10 + self.level)
        self.defence_rate = int((self.race_defence_rate * 2 + 15) * (self.level / 100) + 10 + self.level)
        self.special_attack_rate = int((self.race_special_attack_rate * 2 + 15) * (self.level / 100) + 10 + self.level)
        self.special_defence_rate = int((self.race_special_defence_rate * 2 + 15) * (self.level / 100) + 10 + self.level)
        self.speed_rate = int((self.race_speed_rate * 2 + 15) * (self.level / 100) + 10 + self.level)


    # 레벨업 조건 level**3 의 경험치를 획득하면 레벨업
    def experience_value(self,target):
        self.xp += target.level**3
        self.level_up()
    def level_up(self):
        if self.level == 100:
            pass #레벨 100도달하면 레벨업 하지않음
        elif self.xp >= self.level**3:
            self.level += 1
            self.xp = 0
            print(f"레벨업! {self.name}의 레벨은 {self.level}입니다.")
            self.ability()

#####################################################

    # 데미지 연산은 다음과 같이 정의한다.
    # 데미지 = 위력 × 공격 or 특수공격 × (레벨 × 2 ÷ 5 + 2 ) ÷ 방어 or 특수방어 ÷ 50 + 2
    def attack(self,target,skill_number):
        attack_name = list(self.skill.keys())[skill_number] #키값 추출 후 리스트로 형 변환
        print(f'{self.name}이(가) {target.name}에게 {attack_name} 공격을 시전!')

        if self.skill.get(attack_name)[1] == 'physics': #물리공격
            damage = int((self.skill.get(attack_name)[0] * self.attack_rate) \
                         * (self.level * 2 / 5 + 2) / target.defence_rate / 50 + 2)
            if damage <= 0:
                damage = 0
            target.hp = target.hp - damage
            if target.hp <= 0:
                target.hp = 0
                print(f'{target.name}이(가) 쓰러졌습니다.')
            else:
                print(f'{target.name}의 체력이 {target.hp} 남았습니다.')

        elif self.skill.get(attack_name)[1] == 'special': #특수공격
            damage = int((self.skill.get(attack_name)[0] * self.special_attack_rate) \
                         * (self.level * 2 / 5 + 2) / target.special_defence_rate / 50 + 2)
            if damage <= 0:
                damage = 1
            target.hp = target.hp - damage
            if target.hp <= 0:
                target.hp = 0
                print(f'{target.name}이(가) 쓰러졌습니다.')
            else:
                print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
