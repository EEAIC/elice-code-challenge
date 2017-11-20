# 토끼와 당근밭을 불러올 모듈을 호출합니다.
from elicerabbits2 import *
from time import *


def hurry_rabbit_hurry(rabbit):
    # 토끼가 서둘러 비를 막을 수 있도록 아래에 코드를 작성해주세요!
    rabbit.turn_left()
    front_move = 0
    pick_crt = 0
    if rabbit.front_is_clear():
        rabbit.move()
    else:
        rabbit.turn_right()
        rabbit.move()
    while rabbit.get_pos() != (3, 6):
        if rabbit.left_is_clear() == True and rabbit.on_carrot() == False:
            if rabbit.front_is_clear() == True:
                if front_move > 1:
                    rabbit.drop_carrot()
                    front_move = 0
                elif pick_crt == 0:
                    rabbit.turn_left()
                    rabbit.turn_left()
                    rabbit.move()
                    rabbit.pick_carrot()
                    pick_crt += 1
                    rabbit.turn_right()
                    rabbit.move()
                    front_move = 1
                else:
                    rabbit.turn_left()
                    rabbit.move()
                    front_move += 1
        elif rabbit.front_is_clear() == True:
            rabbit.move()
            front_move += 1
            pick_crt = 0
        else:
            rabbit.turn_right()


def main():
    # main()은 수정할 필요가 없습니다.
    # 토끼굴을 소환합니다.
    load_world("rain0.wld")

    # 당근 10개를 들고 있는 토끼를 3, 6에 소환합니다.
    rabbit = Rabbit(carrots=10, avenue=3, street=6, orientation="E")
    rabbit.set_trace("blue")
    rabbit.set_pause(0.1)

    hurry_rabbit_hurry(rabbit)


if __name__ == "__main__":
    main()