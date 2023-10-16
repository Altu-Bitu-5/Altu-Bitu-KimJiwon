from sys import stdin

input = stdin.readline
N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
temp = []


def solve():
    if len(temp) == M:
        print(*temp)  # temp 전부 출력
        return
    overlap = 0
    for i in range(N):
        if overlap != L[i]:  # 중복된 순열 방지
            temp.append(L[i])
            overlap = L[i]  # 현재 순열에서 이미 사용한 숫자 기억
            solve()
            temp.pop()  # 재귀 호출이 끝나면, temp에서 제거 후 다음 숫자 선택


solve()
