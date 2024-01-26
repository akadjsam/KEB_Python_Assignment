#first director of pokemon
from assignment_pokemongame.pokemon_game import *
from assignment_pokemongame.function import *

class Muchung:
    def __init__(self):
        self.name = '무청'
        self.pokemon_list = []
        self.pokemon_list.append(sneasel.Sneasel())
        self.pokemon_list.append(piloswine.Piloswine())
        self.pokemon_list.append(abomasnow.Abomansnow())
        self.pokemon_list.append(froslass.Froslass())
        #강석의 포켓몬 레벨 조정
        self.pokemon_list[0].level = 40
        self.pokemon_list[1].level = 40
        self.pokemon_list[2].level = 42
        self.pokemon_list[3].level = 44

        [self.pokemon_list[i].ability() for i in range(len(self.pokemon_list))] #강석의 포켓몬 종족값에 따른 능력치 설정

        print_delay('무청에게 도전하는 거야? 좋아! 강한 사람 기다리고 있었어.')
        print_delay('하지만 나도 정신을 집중할 거니까 강할걸? 포켓몬도 멋도 연애도 전부 정신집중이얏!')
        print_delay('이 부분을 받아줄 테니까 각오해 둬!')
        time.sleep(1)
        print()

    def lose_dialogue(self):
        print_delay('대단하다! 약간 존경심이 생길지도 모르겠다.')
        time.sleep(1)
        print("글레이셔벳지를 획득하였습니다!")