# 모든 경우의 수를 탐색
# 브루트 포스: 무차별 대입, 완전 탐색기법으로 입력범위와 시간복잡도를 잘 고려할 것

# 9 난쟁이 - 2 난쟁이 = 키가 100이 되는 경우로 바꿔서 생각(문제가 7 난쟁이의 합이 100이므로)

data = []
one = 0
two = 0

for _ in range(9):  # 0-8
    data.append(int(input()))

sum_val = sum(data)
for i in range(8):
    for j in range(i + 1, 9):
        # 데이터 합에서 2개 골라 뺏을때 100이면
        if sum_val - (data[i] + data[j]) == 100:
            one = data[i]
            two = data[j]

# 리스트에서 고른값 제거
data.remove(one)
data.remove(two)
data.sort()

# 오름차순 정렬 후 출력
for i in data:
    print(i)
