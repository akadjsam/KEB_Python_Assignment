#fifth director of pokemon
from assignment_pokemongame.pokemon_game import *
from assignment_pokemongame.function import *
class Melisa:
    def __init__(self):
        self.name = '멜리사'
        self.director = []
        self.director.append(turtwig.Turtwig())
        self.director.append(cherubi.Cherubi())
        self.director.append(roserade.Roserade())

        #강석의 포켓몬 레벨 조정
        self.director[0].level = 20
        self.director[1].level = 20
        self.director[2].level = 22

        [self.director[i].ability() for i in range(len(self.director))] #강석의 포켓몬 종족값에 따른 능력치 설정
        print_delay('오-호호호!! 기다리고 있었어요!!')
        print_delay('저 이 나라에 와서 많이 공부했어요. 이 마을은 콘테스트 해요. 그래서 전 이런 복장이죠.')
        print_delay('포켓몬에 대해서도 공부했어요. 그랬더니 체육관 관장이 되었어요. ')
        print_delay('으음 그러니까. 당신도 도전해 보세요. 전 당신을 이기겠어요. 그것이 체육관 관장!')



    def lose_dialogue(self):
        print("당신 최고로 강해요. 나 진 것 알아요.")
        time.sleep(1)