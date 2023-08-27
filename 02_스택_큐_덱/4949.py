while 1:
    str = input()
    if str == ".":
        break

    stack = []
    result = True

    for syl in str:  # 괄호 외 다른 음절은 모두 무시
        if syl == "(" or syl == "[":
            stack.append(syl)
        elif syl == ")":
            if len(stack) == 0 or stack[-1] == "[":
                result = False
                break
            elif stack[-1] == "(":
                stack.pop()
        elif syl == "]":
            if len(stack) == 0 or stack[-1] == "(":
                result = False
                break
            elif stack[-1] == "[":
                stack.pop()
    if len(stack) == 0 and result == True:
        print("yes")
    else:
        print("no")
