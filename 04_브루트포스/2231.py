n = int(input())  # 분해합: 256

for i in range(1, n + 1):  # 1-256
    num = sum((map(int, str(i))))  # i의 각 자릿수를 더함: 13
    num_sum = i + num  # 분해합 = 생성자 + 각 자릿수의 합
    # i가 작은 수(1-256)부터 차례로 들어가므로 처음으로 분해합과 입력값이 같을때가 가장 작은 생성자를 가짐
    if num_sum == n:
        print(i)
        break
    if i == n:  # 생성자 i와 입력값이 같다는 것은 생성자가 없다는 뜻
        print(0)
