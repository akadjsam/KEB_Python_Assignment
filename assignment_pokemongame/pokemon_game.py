#플레이어의 포켓몬은 4세대 스타팅 포켓몬으로 하였다.
#데미지 계산 공식은 1세대 기준을 참고하여 설정하였다.
import sys
import time

import chimchar, piplup, turtwig

# c1 = chimchar.Chimchar()
# p1 = piplup.Piplup()
# t1 = turtwig.Turtwig()
#
# c1.attack(p1,1)
# p1.attack(t1,1)
# t1.attack(c1,1)
def print_delay(message):
    print(message)
    time.sleep(2)

if __name__ == '__main__':
    # print_delay('흐음!! 잘왔다! 포켓몬스터의 세계에 온 것을 환영한다!')
    # print_delay('내 이름은 마박사! 모두가 포켓몬 박사님이라고 부르고 있단다. 이 세계에는 포켓몬스터, 줄여서 포켓몬이라 불리는 생명체가 도처에 살고 있다!')
    # print_delay('우리 인간은 포켓몬과 사이좋게 살고 있지. 함께 놀기도 하고 힘을 합쳐 일하기도 하고 그리고 포켓몬끼리 싸우게 하여 유대감을 돈독히 다지기도 하고...')
    # print_delay('나는 그런 포켓몬들을 자세히 알기 위해 연구하고 있는 것이란다!')
    # print_delay('이제부터 너만의 이야기가 시작된다!')
    # print_delay('거기서 너는 여러 포켓몬이나 많은 사람들과 만나 무언가를 발견하게 되겠지.')
    # print_delay('그럼 포켓몬스터의 세계로!')
    # time.sleep(2)
    while True:
        print("포켓몬을 선택하세요",end=' ')
        try:
            select_pokemon = input('1)모부기\t2)팽도리\t3)불꽃숭이 : ')
            if select_pokemon == '1':
                player = turtwig.Turtwig()
                break
            elif select_pokemon == '2':
                player = piplup.Piplup()
                break
            elif select_pokemon == '3':
                player = chimchar.Chimchar()
                break
            else:
                print("다시 선택하세요")
        except Exception as e:
            sys.exit("프로그램의 오류로 인하여 강제 종료됩니다.",e)