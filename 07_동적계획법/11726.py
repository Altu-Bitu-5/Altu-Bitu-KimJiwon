# 2*n 크기의 직사각형을 1*2와 2*1로 채우는 방법의 수

"""
    2*5를 만들고자 하면 

    n=1, 1개
    n=2, 2개
    n=3, 3개
    n=4, 5개
    n=5, 8개
"""

import sys

n = int(sys.stdin.readline())

# memoization 배열 생성
dp = [0] * 1001
# n이 1,2인 경우는 명확하니까 미리 선언 -> 이전값을 써먹는게 동적계획법
dp[1] = 1
dp[2] = 2


for i in range(3, 1001):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print(dp[n])
