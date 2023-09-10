import sys, math

num = 1000001
arr = [True for _ in range(num)]
for i in range(2, int(math.sqrt(num)) + 1):
    if arr[i]:
        for k in range(i + i, num, i):
            arr[k] = False  # 1000000 까지의 소수를 모두 삭제

while True:
    n = int(sys.stdin.readline())  # 20

    if n == 0:
        break

    flag = 0

    for a in range(3, len(arr)):
        if arr[a] and arr[n - a]:  # 17과 3이 있다면
            print(str(n) + " = " + str(a) + " + " + str(n - a))
            flag = 1
            break
    if flag == 0:
        print("Goldbach's conjecture is wrong.")
