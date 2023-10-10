from collections import deque
import sys

input = sys.stdin.readline


# bfs
def graph(n):
    queue = deque([n])
    cnt = 0
    visited = [0] * (N + 1)
    visited[n] = 1
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 원소 하나를 뽑아
        q = queue.popleft()
        cnt += 1
        # 해킹가능한 컴퓨터가 존재하지 않을 때(연결된 컴퓨터가 없을 때) 까지 탐색
        for i in comArr[q]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
    return cnt


N, M = map(int, input().split())
comArr = [[] for _ in range(N + 1)]

# 컴퓨터의 A 와 B 관계를 2차원 배열로 정리
for _ in range(M):
    A, B = map(int, input().split())
    comArr[B].append(A)

# 각 컴퓨터마다 최대 해킹 가능한 컴퓨터의 수 저장
answer = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    answer[i] = graph(i)

# 해킹 가능한 컴퓨터가 가장 많은 컴퓨터의 번호 출력
for i in range(1, N + 1):
    if answer[i] == max(answer):
        print(i, end=" ")
