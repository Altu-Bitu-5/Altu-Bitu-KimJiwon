import sys, math

input = sys.stdin.readline

a1, a2 = map(int, input().split())  # 2 7
b1, b2 = map(int, input().split())  # 3 5

"""
    분수를 더함
    분자와 분모의 최대공약수(GCD)를 구함
    분자와 분모를 GCD로 나눔
"""

bunjja = a1 * b2 + a2 * b1  # 31
bunmo = a2 * b2  # 35

gcd = math.gcd(bunjja, bunmo)  # math 내장함수 사용 1
bunjja //= gcd  # 31
bunmo //= gcd  # 35

print(bunjja, bunmo)
