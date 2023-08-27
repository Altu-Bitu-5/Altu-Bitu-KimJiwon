import sys

n = int(input())

def sum_num(inputs):
    result = 0
    for i in inputs:
        if i.isdigit(): # 숫자일 때만
            result+=int(i)
    return result

arr = []
for i in range(n):
    a = input()
    arr.append(a)

# lambda는 간단한 함수를 정의할 때 사용되며, 여기서 x는 정렬될 리스트 arr의 각 요소를 의미합니다. 이 익명 함수는 세 가지 값을 반환하는데, 이 값들은 정렬의 기준이 됩니다.
# len(x): x의 길이를 반환합니다. 길이가 짧은 순서대로 정렬됩니다.
# sum_num(x): x 문자열에 포함된 숫자들의 합을 반환합니다. 합이 작은 순서대로 정렬됩니다.
# x: 원래의 x 문자열을 반환합니다. 사전순으로 정렬됩니다.
arr.sort(key = lambda x:(len(x), sum_num(x), x))
for i in arr:
    print(i)