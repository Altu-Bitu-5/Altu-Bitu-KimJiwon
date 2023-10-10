from sys import stdin
from collections import deque

input = stdin.readline
# → ← ↓ ↑ ↘ ↖ ↙ ↗
dx = [1, -1, 0, 0, 1, -1, 1, -1]  # 열
dy = [0, 0, 1, -1, 1, -1, -1, 1]  # 행


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[y][x] = 0
    while queue:
        a, b = queue.pop()
        for i in range(8):  # 주변 다 둘러보면서
            ny = b + dy[i]
            nx = a + dx[i]
            if (
                0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1
            ):  # 그래프의 탐색조건(주변에 땅 또있으면)
                queue.append((nx, ny))  # 큐에 그 땅 추가
                graph[ny][nx] = 0  # 그 땅 다신 안오게 0처리 하기


result = []
while True:
    res = 0
    m, n = map(int, input().split())  # 5 5
    if n == 0 and m == 0:  # 종료
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    """
        1 0 1 0 1
        0 0 0 0 0
        1 0 1 0 1
        0 0 0 0 0
        1 0 1 0 1
        graph = [ [1,0,1,0,1], [0,0,0,0,0], [1,0,1,0,1], [0,0,0,0,0], [1,0,1,0,1]]
    """

    for i in range(n):  # 5
        for j in range(m):  # 5
            if graph[i][j] == 1:  # 해당지점이 땅인 경우만 탐색
                bfs(j, i)  # 인접한 땅 다 찾음
                res += 1  # 땅 개수 +1
    result.append(res)  # 결과 리스트에 추가

for i in result:
    print(i)  # 결과 출력
