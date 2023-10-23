# 백트래킹: 답이 될만한지 판단하고, 그렇지 않다면 탐색하지 않고(가지치기)
# 다시 전으로 넘어가서 탐색을 계속 하는 것
# 탐색 중 조건에 맞지 않는 경우 이전으로 가야하기 때문에, 재귀를 사용
# 단 주어진 N이 20보다 작을때 사용

from sys import stdin

input = stdin.readline
from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * n)
res = 0

while 1:
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0  # 로봇이 내려가는 부분이니 0
    if sum(robot):  # 로봇이 존재하면
        for i in range(n - 2, -1, -1):  # 로봇 내려가는 부분 인덱스 i-1 이므로 그 전인 i-2부터
            if robot[i] == 1 and robot[i + 1] == 0 and belt[i + 1] >= 1:
                robot[i + 1] = 1
                robot[i] = 0
                belt[i + 1] -= 1
        robot[-1] = 0  # 이 부분도 로봇 out -> 0임
    if robot[0] == 0 and belt[0] >= 1:
        robot[0] = 1
        belt[0] -= 1
    res += 1
    if belt.count(0) >= k:
        break

print(res)
