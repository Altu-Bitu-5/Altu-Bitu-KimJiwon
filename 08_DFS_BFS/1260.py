from collections import deque


def dfs(start):
    # 현재 노드를 방문 처리
    visited[start] = True
    print(start, end=" ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


def bfs(start):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=" ")
        # 해당 원소와 연결된, 아직 방문하지 않은 원소를 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


# n: 정점의 개수, m: 간선의 개수, v: 탐색을 시작할 정점의 번호
N, M, V = map(int, input().split())  # 4 5 1
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())  # 1 2, 1 3, 1 4, 2 4, 3 4
    graph[a].append(b)  # graph[1] = [2,3,4]
    graph[b].append(a)  # graph[2] = 1

# 정렬(정점이 작은 것부터)
for i in graph:
    i.sort()

# dfs
visited = [False] * (N + 1)
dfs(V)
print()

# bfs
visited = [False] * (N + 1)
bfs(V)
