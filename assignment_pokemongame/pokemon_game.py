#플레이어의 포켓몬은 4세대 스타팅 포켓몬으로 하였다.
#데미지 계산 공식은 1세대 기준을 참고하여 설정하였다.
#전투가 종료되면 플레이어의 포켓몬들은 자동 치료
#능력치 설정 기준 : (종족값 * 2 + 개체값(15로 고정) / 4 ) / 2 + 10 + 레벨
#추후 개발 예정
#타입 상성, 기술 상성
#가상의 트레이너와 승부, 포켓몬 관장, 갤럭시단, 전설의 포켓몬, 사천왕, 챔피언

#포켓몬 관장 - 콜벳지(강석), 포리스트벳지(유채), 코블벳지(자두),팬벳지(맥실러), 레릭벳지(멜리사), 마인벳지(동관), 글레이셔벳지(무청), 비컨벳지(전진)
#사천왕 - 충호, 들국화, 대엽, 오엽
#챔피언 - 난천

#강석 - 꼬마돌,롱스톤,두개도스
#유채 - 모부기,체리꼬,로즈레이드
#자두 - 요가랑, 근육몬, 루카리오
#맥실러 - 갸라도스,누오,플로젤
#멜리사 - 둥실라이드, 팬텀, 무우마직
#동관 - 동미러,강철톤,바리톱스
#무청 - 눈쓰개, 포푸니, 요가램, 눈설왕
#전진 - 쥬피썬더,라이츄,렌트라,에레키블

#충호 - 메가자리,핫삼,비퀸,헤라크로스,드래피온
#들국화 - 누오,꼬지모,딱구리,메깅,하마돈
#대엽 - 헬가,부스터,날쌩마,초염몽,마그마번
#오엽 - 마임맨,에브이,동탁군,후딘,엘레이드
#난천 - 화강돌,로즈레이드,밀로틱,루카리오,토게키스,한카리아스
import copy
import random
import sys

from assignment_pokemongame.pokemons import gible, onix, chimchar, cranidos, piplup, turtwig, geodude,cherubi,roserade,\
    lucario, machoke, meditite, floatzel,quagsire,gyrados,fandom,mismagius,drifblim,coil,bastiodon,sneasel,piloswine,abomasnow,froslass\


from assignment_pokemongame.trainers import uchae, kangsuk, melisa, jadu, maxillar,dongkwan,muchung

def select_starting():
    while True:  # select player's starting pokemon
        print("포켓몬을 선택하세요", end=' ')
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
def wild_pokemon(level): #나중에 포켓몬 랜덤으로 바꾸기
    if level < 10:
        random_num = random.randrange(2)
        if random_num == 1:
            monster = cranidos.Cranidos()
        else:
            monster = onix.Onix()
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
def change_pokemon(change):
    if change in ('2', '3', '4', '5', '6'):
        if len(player) < int(change):
            print("해당 위치에 포켓몬이 없습니다!")
        else:
            player[0], player[int(change) - 1] = player[int(change) - 1], player[0]
def set_director(badge):
    if badge == 0:
        champion = kangsuk.Kangsuk()
    elif badge == 1:
        champion = uchae.Uchae()
    elif badge == 2:
        champion = jadu.Jadu()
    elif badge == 3:
        champion = maxillar.Maxillar()
    elif badge == 4:
        champion = melisa.Melisa()
    elif badge == 5:
        champion = dongkwan.Dongkwan()
    elif badge == 6:
        champion = muchung.Muchung()
    return champion

if __name__ == '__main__':

    # print_delay('흐음!! 잘왔다! 포켓몬스터의 세계에 온 것을 환영한다!')
    # print_delay('내 이름은 마박사! 모두가 포켓몬 박사님이라고 부르고 있단다. 이 세계에는 포켓몬스터, 줄여서 포켓몬이라 불리는 생명체가 도처에 살고 있다!')
    # print_delay('우리 인간은 포켓몬과 사이좋게 살고 있지. 함께 놀기도 하고 힘을 합쳐 일하기도 하고 그리고 포켓몬끼리 싸우게 하여 유대감을 돈독히 다지기도 하고...')
    # print_delay('나는 그런 포켓몬들을 자세히 알기 위해 연구하고 있는 것이란다!')
    # print_delay('이제부터 너만의 이야기가 시작된다!')
    # print_delay('거기서 너는 여러 포켓몬이나 많은 사람들과 만나 무언가를 발견하게 되겠지.')
    # print_delay('그럼 포켓몬스터의 세계로!')
    # time.sleep(1)

    #global pokemon_badge #포켓몬 벳지 수
    pokemon_badge = 5
    lose_flag = 0
    player = [] #포켓몬 포획시 리스트에 담기. 개발 진행중
    select_starting() #스타팅 포켓몬 고르기
    print(f'스타팅 포켓몬으로 {player[0].name}을(를) 선택하셨습니다.')
    while True:
        [player[i].ability() for i in range(len(player))] #플레이어의 능력치 재설정
        print(player[0].hp)
        print(player[0].attack_rate)
        menu = input(f'"메뉴를 선택하세요 : 1)야생포켓몬과 전투\t2)포켓몬 트레이너와 전투'
                     f'\t3)포켓몬 관장에게 도전하기({pokemon_badge+1}번째 관장)"\t4)내 포켓몬 확인하기\t5)게임 종료 : ')
        if menu == '1':
            enemy = wild_pokemon(int((sum(player[i].level for i in range(len(player))))/len(player)))
            enemy.ability()
            print(f'"앗! 야생의 {enemy.name}이(가) 나타났다! Lv{enemy.level}"')
            print(f'"가랏 {player[0].name}! Lv{player[0].level}"')
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
                            print(player[0].hp)
                            if player[0].hp == 0:
                                if sum([player[i].hp for i in range(len(player))])/len(player) == 0:
                                    print("더이상 전투할 포켓몬이 없습니다. 포켓몬 센터로 이동합니다.")
                                    break
                                else:
                                    while True:
                                        print("어느 포켓몬으로 교체하시겠습니까?")
                                        print(", ".join([(f'{i+1})Lv{player[i].level} : ') + player[i].name for i in range(len(player))]))
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
                            break
                        else:
                            print("1,2,3,4 중에 한개를 골라주세요!")

                elif choice == '2':
                    if player[0].speed_rate <= enemy.speed_rate:
                        print("도망칠 수 없습니다!")
                        continue
                    else:
                        print("무사히 도망쳤다!")
                        break

                elif choice == '3':
                    if len(player) > 5:
                        print("더 이상 포켓몬을 포획할 수 없습니다.")
                        continue
                    else:
                        if random.randrange(0,3) == 0: #포켓몬 잡을 확률 1/3
                            catch = copy.deepcopy(enemy)
                            player.append(catch)
                            print("포획 성공 !")
                        else:
                            print("포획에 실패했습니다!")
                            continue
                    break
                else:
                    print("메뉴 중 선택하세요.")
                    continue
                if battle_end_flag == 1:
                    battle_end_flag = 0
                    [player[i].ability() for i in range(len(player))]  # 전투 종료후 플레이어의 능력치 재설정
                    break

        elif menu == '2':
            print("개발 진행중입니다.")

        elif menu == '3':
            rival = set_director(pokemon_badge)
            #.director
            print(f'포켓몬 관장 {rival.name}이(가) 승부를 걸어왔다!')
            i = 0
            while i < len(rival.director):
                print(f'{rival.name}은 {rival.director[i].name}을(를) 내보냈다!')
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
                                battle_end_flag = battle(player[0], rival.director[i])
                                if player[0].hp == 0:
                                    if sum([player[i].hp for i in range(len(player))])/len(player) == 0:
                                        print("더이상 전투할 포켓몬이 없습니다. 포켓몬 센터로 이동합니다.")
                                        lose_flag = 1
                                        break
                                    else:
                                        while True:
                                            print("어느 포켓몬으로 교체하시겠습니까?")
                                            print(", ".join([(f'{i+1})Lv{player[i].level} : ') + player[i].name for i in range(len(player))]))
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
                                break
                            else:
                                print("1,2,3,4 중에 한개를 골라주세요!")
                        if rival.director[i].hp == 0:
                            i += 1
                            break

                    elif choice == '2':
                        print("안돼! 싸움 중 등을 보일 순 없어!")
                        continue

                    elif choice == '3':
                        print("남의 것에 손대면 도둑!")
                        continue

                    else:
                        print("다시선택하세요!")
                        continue

                    if battle_end_flag == 1:
                        battle_end_flag = 0
                        break
                if lose_flag == 1:
                    break
            if lose_flag == 1:
                lose_flag = 0
            else:
                pokemon_badge += 1
                rival.lose_dialogue() #포켓몬 관장들 패배 대사
                print("포켓몬 벳지를 1개를 획득하셨습니다.")
        elif menu == '4':
            print(", ".join([(f'{i+1})Lv{player[i].level} : ') + player[i].name for i in range(len(player))]))
            decide_change = input("포켓몬 순서를 변경하시겠습니까? : 1)예\t2)아니요 : ")#change_sequence
            if decide_change == '1':
                change_sequence = input("몇번째 포켓몬을 첫번째로 하시겠습니까? : ")
                change_pokemon(change_sequence)
            else:
                print("포켓몬 순서변경을 취소하셨습니다. 메뉴로 돌아갑니다.")
        elif menu == '5':
            print('게임을 종료합니다.')
            break
        else:
            print("메뉴중에 선택하세요!")
