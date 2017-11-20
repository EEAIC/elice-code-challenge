def checkParen(p):
    # 괄호 문자열 p의 쌍이 맞으면 "YES", 아니면  "NO"를 반환하도록 아래에 코드를 작성해주세요!
    tmp_p = list(p)
    stack = []
    while tmp_p:
        tmp = tmp_p.pop(0)
        if tmp == '(':
            stack.append('(')
        elif tmp == ')':
            if stack:
                stack.pop(len(stack) - 1)
            else:
                return "NO"
    if not stack:
        return "YES"
    else:
        return "NO"


def main():
    # main()은 수정할 필요가 없습니다. 

    x = input()
    print(checkParen(x))


if __name__ == "__main__":
    main()


