import sys

A, B = map(int, sys.stdin.readline().split())  # 피드백 받은 부분
a, b = A, B

# 유클리드 호제법:
"""
    두 정수 a, b가 주어짐(a > b)
    a와 b의 a%b와 b의 최대공약수와 같음
    a%b를 구한 후, 왼쪽값 > 오른쪽값 이어야 하므로 위치를 바꿈
    b가 0일때, a의 값이 최대 공약수
"""
while b != 0:
    a = a % b  # 나머지
    a, b = b, a

# gcd(최대공약수)
print(a)

# lcm(최소공배수)
print(A * B // a)
