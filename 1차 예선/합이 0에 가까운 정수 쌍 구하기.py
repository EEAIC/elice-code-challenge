import math


def sum_0(data):
    # 아래에 코드를 작성해주세요!
    under = []
    over = []
    return_sum = 40000000
    over_sum = 0
    under_sum = 0
    for i in range(len(data)):
        if data[i] < 0:
            under.append(data[i])
        else:
            over.append(data[i])
    under.reverse()
    if not under:
        return_pair = [over[0], over[1]]
    elif not over:
        return_pair = [under[0], under[1]]
    else:
        i = 0
        j = 0
        while i != len(under) and j != len(over):
            if return_sum > abs(under[i] + over[j]):
                return_sum = abs(under[i] + over[j])
                return_pair = [under[i], over[j]]
            if abs(under[i]) >= over[j]:
                j += 1
            else:
                i += 1

    return return_pair


def main():
    # main()은 수정할 필요가 없습니다.

    given_data = input()

    data = [int(v.strip()) for v in given_data.split()]

    print(*sum_0(data))


if __name__ == "__main__":
    main()
