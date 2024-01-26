#first director of pokemon
from assignment_pokemongame.pokemon_game import *
from assignment_pokemongame.function import *

class Jadu:
    def __init__(self):
        self.name = '자두'
        self.pokemon_list = []
        self.pokemon_list.append(meditite.Meditite())
        self.pokemon_list.append(machoke.Machoke())
        self.pokemon_list.append(lucario.Lucario())

        #강석의 포켓몬 레벨 조정
        self.pokemon_list[0].level = 28
        self.pokemon_list[1].level = 29
        self.pokemon_list[2].level = 32

        [self.pokemon_list[i].ability() for i in range(len(self.pokemon_list))] #강석의 포켓몬 종족값에 따른 능력치 설정
        print_delay('안녕하세요. 잘 부탁드립니다. 저 체육관 관장인 자두라고 합니다.')
        print_delay('어째서 체육관 관장이 될 수 있었는지 강하다는 것이 어떤 것인지 제 스스로는 잘 모르지만')
        print_delay('체육관 관장으로서 제 나름대로 진지하게 열심히 할 테니 언제든지 덤비세요!')
        time.sleep(1)
        print()

    def lose_dialogue(self):
        print("나의 패배입니다... 왜냐면 당신이 너무 강하니까.")
        time.sleep(1)
        print("코블벳지를 획득하였습니다!")