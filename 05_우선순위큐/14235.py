import heapq

"""
    우선순위큐를 써야한다.
    입력이 0이면 우선순위큐에 값이 있는지 체크한다.
    우선순위 큐에 값이 없으면 줄 선물이 없으므로 -1을 출력한다.
    우선순위 큐에 값이 있으면 가장 가치가 높은 선물을 준다. 
    가치가 높은 선물을 주기 위해선 최대힙을 사용해야한다.
"""

n = int(input())
heap = []
temp = []

for _ in range(n):
    cur = input()
    if len(cur) == 1:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(-1)
    else:
        temp = list(map(int, cur.split()))
        for i in range(1, len(temp)):
            heapq.heappush(heap, (-temp[i], temp[i]))  # 최대힙

            """
                [1,3,5,7,9] 
                [(-9,9),(-7,7),(-5,5),(-3,3),(-1,1)]
                힙에 원소를 추가할 때 (-item, item)의 튜플 형태로 넣어주면 튜플의 첫 번째 원소를 우선순위로 힙을 구성하게 된다.  
                이때 원소 값의 부호를 바꿨기 때문에, 최소 힙으로 구현된 heapq 모듈을 최대 힙 구현에 활용하게 되는 것이다.
            """
