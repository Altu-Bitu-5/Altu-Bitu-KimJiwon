import sys, math

input = sys.stdin.readline

n, k = map(int, input().split())

array = [True for _ in range(n + 1)]
num = 1


# 에라토스테네스의 체
"""
    2부터 n**(1/2)까지 해당 숫자의 배수에 해당하는 숫자를 지워나감
"""
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        for j in range(i, n + 1, i):  # 마지막 인자는 간격
            if array[j] == False:
                continue

            if num == k:
                print(j)

            array[j] = False
            num += 1
