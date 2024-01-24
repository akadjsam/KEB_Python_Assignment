#first director of pokemon
from assignment_pokemongame.pokemon_game import *
from assignment_pokemongame.function import *
class Red:
    def __init__(self):
        self.name = '레드'
        self.director = []
        self.director.append(geodude.Geodude())
        self.director.append(onix.Onix())
        self.director.append(cranidos.Cranidos())

        #강석의 포켓몬 레벨 조정
        self.director[0].level = 88
        self.director[1].level = 80
        self.director[2].level = 82
        [self.director[i].ability() for i in range(len(self.director))] #강석의 포켓몬 종족값에 따른 능력치 설정
        for i in range(5):
            print_delay('... ... ... ... ... ... ... ... ... ...')
            time.sleep(1)
        print()

    def lose_dialogue(self):
        print("'... ... ... ... ... ... ... ... ... ...!")
        time.sleep(1)
        print("The end")
        sys.exit()