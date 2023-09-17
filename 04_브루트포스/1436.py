# 완전탐색

n = int(input())  # 2

Num = 666
count = 0
while True:
    if "666" in str(Num):  # 만약 종말번호안에 666이 포함되어 있으면
        count += 1
        if count == n:  # 그 카운트값이 입력값과 같다면
            break  # 반복문 탈출
    Num += 1

print(Num)
