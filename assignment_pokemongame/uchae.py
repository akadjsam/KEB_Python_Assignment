#second director of pokemon
import turtwig,cherubi,roserade
from pokemon_game import *
class Uchae:
    def __init__(self):
        self.name = '유채'
        self.director = []
        self.director.append(turtwig.Turtwig())
        self.director.append(cherubi.Cherubi())
        self.director.append(roserade.Roserade())

        #강석의 포켓몬 레벨 조정
        self.director[0].level = 20
        self.director[1].level = 20
        self.director[2].level = 22

        [self.director[i].ability() for i in range(len(self.director))] #강석의 포켓몬 종족값에 따른 능력치 설정


    def lose_dialogue(self):
        print("이,이럴수가! 열심히 단련시킨 포켓몬들이!!")
        time.sleep(1)