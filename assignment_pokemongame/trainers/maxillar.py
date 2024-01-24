#first director of pokemon
from assignment_pokemongame.pokemon_game import *
from assignment_pokemongame.function import *

class Maxillar:
    def __init__(self):
        self.name = '맥실러'
        self.director = []
        self.director.append(gyrados.Gyarados())
        self.director.append(quagsire.Quagsire())
        self.director.append(floatzel.Floatzel())

        #강석의 포켓몬 레벨 조정
        self.director[0].level = 33
        self.director[1].level = 34
        self.director[2].level = 37

        [self.director[i].ability() for i in range(len(self.director))] #강석의 포켓몬 종족값에 따른 능력치 설정
        print_delay('잘- 왔다!! 내가 들판시티 포켓몬체육관의 체육관 관장인 그 이름도 맥시멈가면!')
        print_delay('물의 힘으로 단련한 나의 포켓몬은! 너의 공격을 전부 받아들인 뒤에 승리할 테니 덤벼랏!')

        time.sleep(1)
        print()

    def lose_dialogue(self):
        print_delay('우왓! 끝나 버렸나! 뭐랄까, 좀 더 싸우고 싶은 기분이야!')
        time.sleep(1)
        print("펜벳지를 획득하였습니다!")