import math

"""
    n1=s1*m+r
    n2=s2*m+r
    m3=s3*m+r

    n2-n1=m(s2-s1)
    n3-n2=m(s3-s2)

    n1=6, n2=34, n3=38
    n2-n1=28, n3-n2=4

    28과 4의 최대공약수와, 해당 최대공약수의 약수
"""
n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()

import math

gcd = lst[1] - lst[0]
for i in range(2, n):
    gcd = math.gcd(lst[i] - lst[i - 1], gcd)

divisor_lst = []
for i in range(2, int(gcd**0.5) + 1):
    if gcd % i == 0:
        divisor_lst.append(i)
        divisor_lst.append(gcd // i)

divisor_lst.append(gcd)
divisor_lst = list(set(divisor_lst))
divisor_lst.sort()

print(*divisor_lst)
