#플레이어의 포켓몬은 4세대 스타팅 포켓몬으로 하였다.
#데미지 계산 공식은 1세대 기준을 참고하여 설정하였다.
import chimchar, piplup, turtwig

c1 = chimchar.Chimchar()
p1 = piplup.Piplup()
t1 = turtwig.Turtwig()

c1.attack(p1,1)
p1.attack(t1,1)
t1.attack(c1,1)
