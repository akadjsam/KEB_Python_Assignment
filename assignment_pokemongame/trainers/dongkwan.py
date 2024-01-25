#first director of pokemon
from assignment_pokemongame.pokemon_game import *
from assignment_pokemongame.function import *

class Dongkwan:
    def __init__(self):
        self.name = '동관'
        self.director = []
        self.director.append(coil.Coil())
        self.director.append(onix.Onix())
        self.director.append(bastiodon.Bastiodon())
        self.director[1].level_flag = 0
        #강석의 포켓몬 레벨 조정
        self.director[0].level = 37
        self.director[1].level = 38
        self.director[2].level = 41

        [self.director[i].ability() for i in range(len(self.director))] #강석의 포켓몬 종족값에 따른 능력치 설정
        self.director[1].evolve()
        print_delay('오우! 그것은 무쇠체육관 배지, 그렇구나 그렇구나!')
        print_delay('내 아들을 쓰러뜨렸구나. 뭐 녀석은 아직 미숙하니까.')
        print_delay('아들인 강석이를 대신해서 나 동관이가 상대를 해 주지!')
        time.sleep(1)
        print()

    def lose_dialogue(self):
        print_delay('우-음! 단련한 포켓몬들이!!')
        time.sleep(1)
        print("마인뱃지를 획득하였습니다!")