import heapq
import sys

"""
    1. leftheap과 rightheap의 길이 같다면 중간값의 기준이 되는 leftheap에 수를 넣는다.
    반면, 같지 않다면 길이를 맞춰주기 위해 rightheap에 수를 넣는다.

    2. 만약에 leftheap의 루트가 rightheap의 루트보다 크면 leftheap의 루트와 rightheap의 루트를 바꿔준다.

    3. leftheap은 최대힙, 오른쪽 힙은 최소힙으로 정렬시, 왼쪽 힙의 첫번째 요소(가장 큰값)는 항상 중앙값이 된다.


    left = 최대 힙(내림차순), right = 최소 힙(오름차순)
    ex) [1, 5, 2, 10, -99, 7, 5]
    num = 1 👉 left = [-1] / right = []
    num = 5 👉 left = [-1], right = [5]
    num = 2 👉 left = [-2,-1], right = [5]
    num = 10 👉 left = [-2,-1], right = [5,10]
    num = -99 👉 left = [-2,-1,99], right = [5,10]
    num = 7 👉 left = [-2,-1,99], right = [5,7,10]
    num = 5 👉 left = [-5,-2,-1,99], right = [5,7,10]
"""


n = int(sys.stdin.readline())

leftHeap = []
rightHeap = []
for i in range(n):
    num = int(sys.stdin.readline())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
    else:
        heapq.heappush(rightHeap, num)

    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftValue = heapq.heappop(leftHeap)
        rightValue = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -rightValue)
        heapq.heappush(rightHeap, -leftValue)

    print(-leftHeap[0])
