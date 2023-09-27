# 빨리 끝나는 회의 순서대로 정렬 -> 오름차순
# 끝나는 시간이 같다면 빨리 시작하는 순서대로 정렬 -> 오름차순
"""
    그리디 알고리즘은 아래 두 개의 속성을 만족

    1. 탐욕적 선택 속성: 탐욕적으로 선택하더라도 문제의 최적해가 보장될 때
        - 가장 빨리 끝나는 회의를 선택 시, 다른 회의에서 사용할 수 있는 남은 시간이 커진다.
    2. 최적 부분 구조: 부분 문제의 최적해가 전체 문제의 최적해로 확장될 수 있을 때
        - 매번 남은 회의 중 가장 빨리 끝나는 회의를 선택한다. 
"""
import sys

input = sys.stdin.readline
N = int(input())
time = []

for _ in range(N):
    start, end = map(int, input().split())
    time.append([start, end])  # 이중리스트 사용

time = sorted(time, key=lambda a: a[0])  # 시작 시간을 기준으로 오름차순
time = sorted(time, key=lambda a: a[1])  # 끝나는 시간을 기준으로 다시 오름차순

last = 0  # 회의의 마지막 시간을 저장할 변수
conut = 0  # 회의 개수를 저장할 변수

for i, j in time:
    if i >= last:  # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
        conut += 1
        last = j  # 마지막 시간 대입

print(conut)
