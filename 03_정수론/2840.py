import sys, math

input = sys.stdin.readline

n, k = map(int, input().split())

data = ["?"] * n
idx = 0
check = True

# 바퀴는 반시계 방향으로 문자 갱신, 출력은 시계방향으로
# 시계방향으로 인덱스를 (+)로
"""
    1. 같은 문자가 바퀴에 중복 X
    2. 한 자리에 여러개의 문자 X
"""
for i in range(k):
    num, alphabet = map(int, input().split())
    idx = (idx + int(num)) % n # 회전한 후 화살표가 가리키는 인덱스, 전체 칸을 벗어나지 못함
    if data[idx] != "?":
        if data[idx] == alphabet: # 해당 칸이 이미 알파벳으로 채워져있는 경우
            continue
        check = False
    else: # 아니라면
        data[idx] = alphabet # 알파벳 적기

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
        idx = (idx - 1) % n # 인덱스 하나씩 줄여가며 적기
else:
    print("!")
