def maxTriangle(triangle):
    # 숫자삼각형 triangle이 주어질 때, 최대 경로에 존재하는 숫자의 합을 반환하는 함수를 작성하세요.
    answer = triangle[0][0]
    for i in range(len(triangle) - 1, 0, -1):
        for pos in range(len(triangle[i]) - 1):
            if triangle[i][pos] >= triangle[i][pos + 1]:
                triangle[i - 1][pos] += triangle[i][pos]
            else:
                triangle[i - 1][pos] += triangle[i][pos + 1]
    return triangle[0][0]


def main():
    # main()은 수정할 필요가 없습니다.

    # print("터미널 입력을 기다리고 있습니다...")
    n = int(input())
    tri = []

    for i in range(n):
        tri.append([int(v) for v in input().split()])

    print(maxTriangle(tri))


if __name__ == "__main__":
    main()
