import sys, math

input = sys.stdin.readline

n, k = map(int, input().split())

data = ["?"] * n
idx = 0
check = True

# 바퀴는 반시계 방향으로 문자 갱신, 출력은 시계방향으로
"""
    1. 같은 문자가 바퀴에 중복 X
    2. 한 자리에 여러개의 문자 X
"""
for i in range(k):
    num, alphabet = map(int, input().split())
    idx = (idx + int(num)) % n
    if data[idx] != "?":
        if data[idx] == alphabet:
            continue
        check = False
    else:
        data[idx] = alphabet

for i in range(n):
    if data[i] == "?":  # 무시
        continue
    for j in range(i + 1, n):
        if data[i] == data[j]:
            check = False
            break

if check:
    for _ in range(n):
        print(data[idx], end="")
        idx = (idx - 1) % n
else:
    print("!")
