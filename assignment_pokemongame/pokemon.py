class Pokemon:
    def __init__(self):
        self.private_name = None
        self.private_hp = None
        self.private_attack_rate = None
        self.private_defence_rate = None
        self.private_special_attack_rate = None
        self.private_special_defence_rate = None
        self.private_speed_rate = None
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

#####################################################

    def attack(self,target,skill_number):
        attack_name = list(target.skill.keys())[skill_number]
        print(f'{self.private_name}이(가) {target.private_name}에게 {attack_name}공격을 시전!')
        if target.skill.get(attack_name)[1] == 'physics':
            print('physics')

