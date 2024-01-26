#first director of pokemon
from assignment_pokemongame.pokemon_game import *
from assignment_pokemongame.function import *
class Kangsuk:
    def __init__(self):
        self.name = '강석'
        self.pokemon_list = []
        self.pokemon_list.append(geodude.Geodude())
        self.pokemon_list.append(onix.Onix())
        self.pokemon_list.append(cranidos.Cranidos())

        #강석의 포켓몬 레벨 조정
        self.pokemon_list[0].level = 12
        self.pokemon_list[1].level = 12
        self.pokemon_list[2].level = 12

        [self.pokemon_list[i].ability() for i in range(len(self.pokemon_list))] #강석의 포켓몬 종족값에 따른 능력치 설정
        print_delay('무쇠시티 포켓몬체육관에 잘 왔어!')
        print_delay('내가 체육관 관장 강석이야!')
        print_delay('우리 인간은 포켓몬과 사이좋게 살고 있지. 함께 놀기도 하고 힘을 합쳐 일하기도 하고 그리고 포켓몬끼리 싸우게 하여 유대감을 돈독히 다지기도 하고...')
        print_delay('바위타입 포켓몬과 함께 나의 길을 걸어가기로 한 트레이너지.')
        print_delay('자, 그럼 트레이너로서 너의 실력이 어느 정도인지 그리고 함께 싸우는 포켓몬이 얼마나 강한지 확인해보겠어!')
        time.sleep(1)
        print()

    def lose_dialogue(self):
        print("이,이럴수가! 열심히 단련시킨 포켓몬들이!!")
        time.sleep(1)
        print("콜벳지를 획득하였습니다!")