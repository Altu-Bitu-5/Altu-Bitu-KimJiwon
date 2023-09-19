# 움직이는 경우의 수 8가지에 대한 dx와 dy를 정하기
# 체스판을 벗어나는지, 킹이 돌 위에 올라가는지 예외 검사하기

king, stone, N = input().split()
k = list(
    map(int, [ord(king[0]) - 64, king[1]])
)  # A1, ord는 문자열을 아스키코드로 바꿔주며 A-64의 경우 1이 됨
s = list(map(int, [ord(stone[0]) - 64, stone[1]]))  # A2

# 이때 k와 s는 [1,1] [1,2]

# 딕셔너리 (이동 타입에 따라 dx와 dy 설정)
move = {
    "R": [1, 0],
    "L": [-1, 0],
    "B": [0, -1],
    "T": [0, 1],
    "RT": [1, 1],
    "LT": [-1, 1],
    "RB": [1, -1],
    "LB": [-1, -1],
}

# 움직이는 횟수 만큼 실행
for _ in range(int(N)):
    m = input()  # 지금 이동 R

    # 킹 움직였을 경우의 위치: nx, ny
    nx = k[0] + move[m][0]  # 1
    ny = k[1] + move[m][1]  # 0

    # 킹 조건 검사
    if 0 < nx <= 8 and 0 < ny <= 8:
        # 돌 위에 얹히는지
        if nx == s[0] and ny == s[1]:
            # 돌 움직였을 경우의 위치: sx, sy
            sx = s[0] + move[m][0]
            sy = s[1] + move[m][1]
            # 돌 조건 검사
            if 0 < sx <= 8 and 0 < sy <= 8:
                k = [nx, ny]  # 킹 이동
                s = [sx, sy]  # 돌 이동
        else:
            k = [nx, ny]  # 킹만 이동
print(f"{chr(k[0] + 64)}{k[1]}")
print(f"{chr(s[0] + 64)}{s[1]}")
