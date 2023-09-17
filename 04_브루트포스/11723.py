# 비트마스킹: int형의 각 비트를 o/x로 사용하는 기법으로,
#            DP나 백트래킹 등 방문여부를 저장해야할 때 사용

# set{1,2,4,10,15}는 10001000100110 으로 표현
# 시프트 연산을 통해 비트를 옮김
# 1<<num: 비트1를 num만큼 왼쪽으로 이동시킴

import sys

m = int(sys.stdin.readline())

bit = 0
for i in range(m):
    comm = sys.stdin.readline().rstrip().split()  # add 1, add가 comm[0]이고 1이 comm[1]임

    if comm[0] == "all":
        bit = (1 << 20) - 1  # 0001 -> 1000 -> 1000+1111 = 1111(2의 보수법으로 계산)
    elif comm[0] == "empty":
        bit = 0
    else:
        op = comm[0]
        num = int(comm[1]) - 1

        if op == "add":
            bit |= 1 << num
        elif op == "remove":
            bit &= ~(1 << num)
        elif op == "check":
            if bit & (1 << num) == 0:
                print(0)
            else:
                print(1)

        elif op == "toggle":
            bit = bit ^ (1 << num)
