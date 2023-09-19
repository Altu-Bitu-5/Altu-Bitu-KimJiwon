import sys, heapq  # 오름차순으로 정렬

input = sys.stdin.readline
n = int(input())
heap = []

for _ in range(n):
    arr = list(map(int, input().split()))
    if not heap:  # heap에 아무것도 없는 첫번째 입력 시
        for a in arr:
            heapq.heappush(heap, a)
    else:
        for a in arr:
            if heap[0] < a:  # heap 최소값보다 현재 숫자가 클경우, n번째로 큰 수가 바뀌어야하므로
                heapq.heappush(heap, a)  # 현재 숫자를 push 하고
                heapq.heappop(heap)  # 기존 최솟값 pop

print(heap[0])
