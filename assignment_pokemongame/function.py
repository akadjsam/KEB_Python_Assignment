import time

from assignment_pokemongame.pokemon_game import *

def print_delay(message): #print delay message
    print(message)
    time.sleep(1)

def battle(player1,player2,choice_skill_number):
    if player1.speed_rate >= player2.speed_rate:
        player1.attack(player2, choice_skill_number - 1)
        if player2.hp <= 0:
            player1.experience_value(player2)
            return 1
        player2.attack(player1, random.randrange(4))
        if player1.hp <= 0:
            return 1
    else:
        player2.attack(player1, random.randrange(4))
        if player1.hp <= 0:
            return 1
        player1.attack(player2, choice_skill_number - 1)
        if player2.hp <= 0:
            player1.experience_value(player2)
            return 1
def skillbattle(player, rival,i):
    while True:
        print()
        print("사용할 스킬을 선택하세요(1 ~ 4)")
        print(", ".join(list(player[0].skill.keys())), " : ")
        choice_skill_number = input()
        if choice_skill_number in ('1', '2', '3', '4'):
            choice_skill_number = int(choice_skill_number)
            battle_end_flag = battle(player[0], rival.pokemon_list[i], choice_skill_number)
            if player[0].hp == 0:
                if sum([player[i].hp for i in range(len(player))]) / len(player) == 0:
                    print("더이상 전투할 포켓몬이 없습니다. 포켓몬 센터로 이동합니다.")
                    lose_flag = 1
                    return battle_end_flag,lose_flag
                else:
                    while True:
                        print("어느 포켓몬으로 교체하시겠습니까?")
                        print(", ".join([(f'{i + 1})Lv{player[i].level} : ') + player[i].name for i in range(len(player))]))
                        change_sequence = input("몇번째 포켓몬을 첫번째로 하시겠습니까? : ")
                        change_pokemon(change_sequence)
                        if player[0].hp == 0:
                            print("해당 포켓몬은 싸울 힘이 남아있지 않습니다.")
                            print()
                            continue
                        else:
                            print(f'"가랏 {player[0].name}! Lv{player[0].level}"')
                            break
                    continue
            print()
            return battle_end_flag, 0
        else:
            print("1,2,3,4 중에 한개를 골라주세요!")