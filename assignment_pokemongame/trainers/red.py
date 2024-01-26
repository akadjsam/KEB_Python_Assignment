#first director of pokemon
from assignment_pokemongame.pokemon_game import *
from assignment_pokemongame.function import *
class Red:
    def __init__(self):
        self.name = '레드'
        self.pokemon_list = []
        self.pokemon_list.append(geodude.Geodude())
        self.pokemon_list.append(onix.Onix())
        self.pokemon_list.append(cranidos.Cranidos())

        #강석의 포켓몬 레벨 조정
        self.pokemon_list[0].level = 88
        self.pokemon_list[1].level = 80
        self.pokemon_list[2].level = 82
        [self.pokemon_list[i].ability() for i in range(len(self.pokemon_list))] #강석의 포켓몬 종족값에 따른 능력치 설정
        for i in range(5):
            print_delay('... ... ... ... ... ... ... ... ... ...')
            time.sleep(1)
        print()

    def lose_dialogue(self):
        print("'... ... ... ... ... ... ... ... ... ...!")
        time.sleep(1)
        print("The end")
        sys.exit()