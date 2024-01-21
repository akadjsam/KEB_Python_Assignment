#플레이어의 포켓몬은 4세대 스타팅 포켓몬으로 하였다.
#데미지 계산 공식은 1세대 기준을 참고하여 설정하였다.
#전투가 종료되면 플레이어의 포켓몬들은 자동 치료
#능력치 설정 기준 : (종족값 * 2 + 개체값(15로 고정) / 4 ) / 2 + 10 + 레벨
#추후 개발 예정
#타입 상성, 기술 상성
#가상의 트레이너와 승부, 포켓몬 관장, 갤럭시단, 전설의 포켓몬, 사천왕, 챔피언
import copy
import random
import sys
import time

import chimchar, piplup, turtwig, starly, gible, geodude, cranidos, onix
import firstdirector

# c1 = chimchar.Chimchar()
# p1 = piplup.Piplup()
# t1 = turtwig.Turtwig()

# c1.attack(p1,1)
# # p1.attack(t1,1)
# # t1.attack(c1,1)
# c1.experience_value(p1)
def print_delay(message): #print dr.ma's message
    print(message)
    time.sleep(2)
def wild_pokemon(level): #나중에 포켓몬 랜덤으로 바꾸기
    if level < 10:
        monster = starly.Starly()
    elif level < 15:
        monster = geodude.Geodude()
    else:
        random_num = random.randrange(2)
        if random_num == 1:
            monster = cranidos.Cranidos()
        else:
            monster = onix.Onix()
    return monster
def battle(player1,player2):
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

if __name__ == '__main__':

    # print_delay('흐음!! 잘왔다! 포켓몬스터의 세계에 온 것을 환영한다!')
    # print_delay('내 이름은 마박사! 모두가 포켓몬 박사님이라고 부르고 있단다. 이 세계에는 포켓몬스터, 줄여서 포켓몬이라 불리는 생명체가 도처에 살고 있다!')
    # print_delay('우리 인간은 포켓몬과 사이좋게 살고 있지. 함께 놀기도 하고 힘을 합쳐 일하기도 하고 그리고 포켓몬끼리 싸우게 하여 유대감을 돈독히 다지기도 하고...')
    # print_delay('나는 그런 포켓몬들을 자세히 알기 위해 연구하고 있는 것이란다!')
    # print_delay('이제부터 너만의 이야기가 시작된다!')
    # print_delay('거기서 너는 여러 포켓몬이나 많은 사람들과 만나 무언가를 발견하게 되겠지.')
    # print_delay('그럼 포켓몬스터의 세계로!')
    # time.sleep(1)

    player = [] #포켓몬 포획시 리스트에 담기. 개발 진행중
    while True: #select player's starting pokemon
        print("포켓몬을 선택하세요",end=' ')
        try:
            select_pokemon = input('1)모부기\t2)팽도리\t3)불꽃숭이 4)프로그램 종료 : ')
            if select_pokemon == '1':
                player.append(turtwig.Turtwig())
                player[0].ability()
                break
            elif select_pokemon == '2':
                player.append(piplup.Piplup())
                player[0].ability()
                break
            elif select_pokemon == '3':
                player.append(chimchar.Chimchar())
                player[0].ability()
                break
            elif select_pokemon == '981123':
                player.append(gible.Gible())
                player[0].ability()
                break
            elif select_pokemon == '4':
                sys.exit()
            else:
                print("다시 선택하세요")
        except Exception as e:
            print(e)
            sys.exit("프로그램의 오류로 인하여 강제 종료됩니다.")
    print(f'스타팅 포켓몬으로 {player[0].name}을(를) 선택하셨습니다.')
    while True:
        print(player[0].hp)
        print(player[0].attack_rate)
        menu = input(f'"메뉴를 선택하세요 : 1)야생포켓몬과 전투\t2)포켓몬 트레이너와 전투'
                     f'\t3)포켓몬 관장에게 도전하기({1}번째 관장)"\t4)내 포켓몬 확인하기\t5)게임 종료 : ')
        if menu == '1':
            enemy = wild_pokemon(int((sum(player[i].level for i in range(len(player))))/len(player)))
            enemy.ability()
            print(f'"앗! 야생의 {enemy.name}이(가) 나타났다!"')
            while True:
                choice = input("1)싸운다.\t2)도망간다.\t3)포획한다. : ")
                if choice == '1': #포켓몬 배틀
                    while True:
                        print()
                        print("사용할 스킬을 선택하세요(1 ~ 4)")
                        print(", ".join(list(player[0].skill.keys()))," : ")
                        choice_skill_number = input()
                        if choice_skill_number in ('1', '2', '3', '4'):
                            choice_skill_number = int(choice_skill_number)
                            battle_end_flag = battle(player[0],enemy)
                            print()
                            break
                        else:
                            print("1,2,3,4 중에 한개를 골라주세요!")

                elif choice == '2':
                    if player[0].speed_rate <= enemy.speed_rate:
                        print("도망칠 수 없습니다!")
                    else:
                        print("무사히 도망쳤다!")
                        break

                elif choice == '3':
                    catch = copy.deepcopy(enemy)
                    player.append(catch)
                    print("포획 성공 !")
                    break

                if battle_end_flag == 1:
                    battle_end_flag = 0
                    [player[i].ability() for i in range(len(player))]  # 전투 종료후 플레이어의 능력치 재설정
                    break

        elif menu == '2':
            print("개발 진행중입니다.")

        elif menu == '3':
            f1 = firstdirector.Kangsuk()
            f1.director
            print(f'포켓몬 관장 {f1.name}이(가) 승부를 걸어왔다!')
            print(f'{f1.name}은 {f1.director[0].name}을(를) 내보냈다!')
            while True:
                choice = input("1)싸운다.\t2)도망간다.\t3)포획한다. : ")
                if choice == '1': #포켓몬 배틀
                    while True:
                        print()
                        print("사용할 스킬을 선택하세요(1 ~ 4)")
                        print(", ".join(list(player[0].skill.keys()))," : ")
                        choice_skill_number = input()
                        if choice_skill_number in ('1', '2', '3', '4'):
                            choice_skill_number = int(choice_skill_number)
                            battle_end_flag = battle(player[0],f1.director[0])
                            print()
                            break
                        else:
                            print("1,2,3,4 중에 한개를 골라주세요!")

                elif choice == '2':
                    print("안돼! 싸움 중 등을 보일 순 없어!")

                elif choice == '3':
                    print("남의 것에 손대면 도둑!")

                if battle_end_flag == 1:
                    battle_end_flag = 0
                    [player[i].ability() for i in range(len(player))]  # 전투 종료후 플레이어의 능력치 재설정
                    break

        elif menu == '4':
            print(", ".join([player[i].name for i in range(len(player))]))
            decide_change = input("포켓몬 순서를 변경하시겠습니까? : 1)예\t2)아니요 : ")#change_sequence
            if decide_change == '1':
                change_sequence = input("몇번째 포켓몬을 첫번째로 하시겠습니까? : ")
                if change_sequence in ('2','3','4','5','6'):
                    if len(player) < int(change_sequence):
                        print("해당 위치에 포켓몬이 없습니다!")
                    else:
                        player[0], player[int(change_sequence)-1] = player[int(change_sequence)-1], player[0]
            else:
                print("포켓몬 순서변경을 취소하셨습니다. 메뉴로 돌아갑니다.")
        elif menu == '5':
            print('게임을 종료합니다.')
            break
        else:
            print("메뉴중에 선택하세요!")