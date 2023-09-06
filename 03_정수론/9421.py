import sys, math


def prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def check(num):
    visit = {}
    while 1:
        n = str(num)  # 문자열로 바꿔
        num = 0
        for i in range(len(n)):  # 자리수만큼 돌며
            num += int(n[i]) ** 2  # 숫자로 바꿔 계산한 후,
        if num == 1:  # 1이 나오면 상근수
            return True

        if num in visit:
            return False
        else:
            visit[num] = 1 # num이라는 key에 value로 1주기


n = int(sys.stdin.readline())  # 20
for i in range(7, n + 1):  # 7부터 20까지 돌면서
    if prime(i):  # 소수인지 확인
        if check(i):  # 상근수인지 확인
            print(i)
