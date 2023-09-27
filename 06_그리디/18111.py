"""
    1. 땅고르기의 기준이 될 블럭 높이를 정한다.
    2. 기준 블럭보다 높으면 깎는다.
    3. 기준 블럭보다 낮으면 쌓는다.
    4. 인벤토리에 있는 블럭들로 기준 높이를 맞출 수 있는지 확인한다.
    5. 같은 시간이라면 가장 높은 기준높이로 답을 유지한다. 
"""

import sys

input = sys.stdin.readline


row, col, inventory = map(int, input().split())
blocks = []
for i in range(row):
    blocks += list(map(int, input().split()))

min_time = 500 * 500 * 2 * 257  # O(1억) 넘으면 시간초과
ans_height = blocks[0]
blocks_out = sum(blocks)
for target_h in range(
    max(blocks), min(blocks) - 1, -1
):  # 최대 높이는 0-256이지만, 주어진 블럭의 min과 max값 사이의 높이만 검사하는게 더 효율적
    if blocks_out + inventory >= target_h * row * col:  # 인벤토리에 충분한 블럭이 있다면
        time = 0
        for b in blocks:
            diff = b - target_h  # 63-64 = -1
            if diff > 0:  # 깎는다.
                time += diff * 2
            elif diff < 0:  # 채운다
                time -= diff * 1

        if time < min_time:
            min_time = time
            ans_height = target_h

print(min_time, ans_height)
