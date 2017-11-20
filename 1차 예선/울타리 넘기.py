# 토끼와 당근밭을 불러올 모듈을 호출합니다.
from elicerabbits2 import *


def run_rabbit_run(rabbit):
    # 토끼가 당근을 모두 수확할 수 있도록 아래에 코드를 작성해주세요!
    while rabbit.on_carrot() == False:
        while rabbit.front_is_clear():
            rabbit.move()
        if rabbit.front_is_clear() == False and rabbit.on_carrot() == False:
            rabbit.turn_left()
            rabbit.move()
            rabbit.turn_right()
            rabbit.move()
            rabbit.turn_right()
            rabbit.move()
            rabbit.turn_left()
    rabbit.pick_carrot()


def main():
    # main()은 수정할 필요가 없습니다.
    # 울타리가 있는 당근밭을 소환합니다.
    load_world('hurdles0.wld')

    # 토끼를 소환합니다.
    rabbit = Rabbit()
    rabbit.set_trace("blue")
    rabbit.set_pause(0.1)

    run_rabbit_run(rabbit)


if __name__ == "__main__":
    main()
