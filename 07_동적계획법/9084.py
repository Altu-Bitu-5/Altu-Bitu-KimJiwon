# 주어진 금액을 만드는 모든 방법 - 모든 조합을 다 생각해야 함
# 이전 경우의 수를 저장하고, 현재의 경우와 이전의 경우를 합치는 게 핵심
# 1차원 배열 - N을 만들고자 한다면, 1~N까지의 배열


"""
    dp[6]: dp[6-2] + dp[6-3] + dp[6-5]
"""


import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    coin = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    dp = [0] * (M + 1)
    dp[0] = 1  # 동전을 안쓰는 가짓수 1 추가
    for i in coin:  # 동전 리스트 2,3,5
        for j in range(1, M + 1):  # 10까지 다 돌면서
            if j >= i:  # 2>2
                dp[j] += dp[j - i]  # DP[j - 해당동전] 의 가짓수를 dp[j]에 더해주면서 M까지 반복
                # dp[6] = dp[6]+dp[3], dp[6] = dp[6]+dp[3], dp[6] = dp[6]+dp[1]

    print(dp[M])
