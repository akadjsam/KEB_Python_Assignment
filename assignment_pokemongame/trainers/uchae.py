#second director of pokemon
from assignment_pokemongame.pokemon_game import *
from assignment_pokemongame.function import *
class Uchae:
    def __init__(self):
        self.name = '유채'
        self.director = []
        self.director.append(turtwig.Turtwig())
        self.director.append(cherubi.Cherubi())
        self.director.append(roserade.Roserade())
        #유채의 포켓몬 레벨 조정
        self.director[0].level = 20
        self.director[1].level = 20
        self.director[2].level = 22

        [self.director[i].ability() for i in range(len(self.director))] #강석의 포켓몬 종족값에 따른 능력치 설정
        print_delay('영원시티 포켓몬체육관에 잘 왔어!')
        print_delay('확실히 풀타입은 약점이 많지만 그것만으로 승패가 갈리지 않는다는 걸 가르쳐줄게!')
        time.sleep(1)
        print()

    def lose_dialogue(self):
        print("대단해! 너 정말 강하구나!")
        time.sleep(1)
        print("포리스트 벳지를 획득하였습니다!")