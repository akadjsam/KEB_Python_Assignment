#first director of pokemon
from assignment_pokemongame.pokemon_game import *
from assignment_pokemongame.function import *
#전진 - 쥬피썬더,라이츄,렌트라,에레키블
class Jeonjin:
    def __init__(self):
        self.name = '전진'
        self.pokemon_list = []
        self.pokemon_list.append(jolteon.Jolteon())
        self.pokemon_list.append(pikachu.Pikachu())
        self.pokemon_list.append(shinx.Shinx())
        self.pokemon_list.append(electivire.Electivire())
        #강석의 포켓몬 레벨 조정
        self.pokemon_list[0].level = 46
        self.pokemon_list[1].level = 46
        self.pokemon_list[2].level = 48
        self.pokemon_list[3].level = 50

        self.pokemon_list[1].evolve()
        self.pokemon_list[2].evolve()

        [self.pokemon_list[i].ability() for i in range(len(self.pokemon_list))] #강석의 포켓몬 종족값에 따른 능력치 설정

        print_delay(' ...자 도전자. 나에게 시합을 도전하는 트레이너가 가끔 있지만 다들 시시하다고 할까.')
        print_delay('별로 시합을 하는 것 같지가 않아...')
        print_delay(' ...후우 나는 체육관 관장 전진.')
        print_delay('신오 제일의 체육관 관장으로 불리지만... 뭐 상관없어.')
        print_delay('나에게 포켓몬 승부의 즐거움을 다시 깨닫게 해주는 트레이너이길 바래!')

        time.sleep(1)
        print()

    def lose_dialogue(self):
        print_delay('이런...! 너와 포켓몬의 한결같은 마음, 싸우는 것만으로도 뜨겁게 벅차게 봤다. 아주 좋은 승부였다.')
        time.sleep(1)
        print("비컨벳지를 획득하였습니다!")