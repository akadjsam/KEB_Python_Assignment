

class Pokemon:
    def __init__(self):
        self.private_name = None
        self.private_hp = None
        self.private_attack_rate = None
        self.private_defence_rate = None
        self.private_special_attack_rate = None
        self.private_special_defence_rate = None
        self.private_speed_rate = None
        self.level = 0
        self.xp = 0
        self.skill = {}

#####################################################
    @property  # getter
    def name(self):
        return self.private_name

    @name.setter  # setter
    def name(self, new):
        self.private_name = new

    @property  # getter
    def hp(self):
        return self.private_hp

    @hp.setter  # setter
    def hp(self, new):
        self.private_hp = new

    @property
    def attack_rate(self):
        return self.private_attack_rate

    @attack_rate.setter  # setter
    def attack_rate(self, new):
        self.private_attack_rate = new

    @property
    def defence_rate(self):
        return self.private_defence_rate

    @defence_rate.setter  # setter
    def defence_rate(self, new):
        self.private_defence_rate = new

    @property
    def special_attack_rate(self):
        return self.private_special_attack_rate

    @special_attack_rate.setter  # setter
    def special_attack_rate(self, new):
        self.private_special_attack_rate = new

    @property
    def special_defence_rate(self):
        return self.private_special_defence_rate

    @special_defence_rate.setter  # setter
    def special_defence_rate(self, new):
        self.private_special_defence_rate = new

    @property
    def speed_rate(self):
        return self.private_speed_rate

    @speed_rate.setter  # setter
    def speed_rate(self, new):
        self.private_speed_rate = new

#레벨업 조건 level**3 의 경험치를 획득하면 레벨업
    def experience_value(self,target):
        self.xp += target.level**3
        self.level_up()
    def level_up(self):
        if self.xp >= self.level**3:
            self.level += 1
            self.xp = 0
            print(f"레벨업! {self.private_name}의 레벨은 {self.level}입니다.")



#####################################################

    # 데미지 연산은 다음과 같이 정의한다.
    # 데미지 = 위력 × 공격 or 특수공격 × (레벨 × 2 ÷ 5 + 2 ) ÷ 방어 or 특수방어 ÷ 50 + 2

    def attack(self,target,skill_number):
        attack_name = list(self.skill.keys())[skill_number] #키값 추출 후 리스트로 형 변환
        print(f' {self.private_name}이(가) {target.private_name}에게 {attack_name}공격을 시전!')

        if self.skill.get(attack_name)[1] == 'physics': #물리공격
            damage = int((self.skill.get(attack_name)[0] * self.private_attack_rate) \
                         * (self.level * 2 / 5 + 2) / target.private_defence_rate / 50 + 2)
            if damage <= 0:
                damage = 0
            target.private_hp = target.private_hp - damage
            if target.private_hp <= 0:
                print(f'{target.private_name}이(가) 사망했습니다.')
            else:
                print(f'{target.private_name}의 체력이 {target.private_hp} 남았습니다.')

        elif self.skill.get(attack_name)[1] == 'special': #특수공격
            damage = int((self.skill.get(attack_name)[0] * self.private_special_attack_rate)\
                     * (self.level * 2 / 5 + 2) / target.private_special_defence_rate / 50 + 2)
            if damage <= 0:
                damage = 1
            target.private_hp = target.private_hp - damage
            if target.private_hp <= 0:
                print(f'{target.private_name}이(가) 사망했습니다.')
            else:
                print(f'{target.private_name}의 체력이 {target.private_hp} 남았습니다.')
