"""
    처음 스피드는 가장 마지막 데이터로 두고, 역방향 순차 탐색 실시

"""

n = int(input())
nums = list(map(int, input().split()))
speed = nums[-1]

for i in range(n - 2, -1, -1):  # 뒤에서 두번째부터 역순으로
    if nums[i] > speed:  # speed보다 행성 속력이 크다면
        speed = nums[i]  # speed를 현재 행성 속력으로 업데이트
    else:
        if speed % nums[i]:  # 정수배가 되지 않는다면
            speed = (speed // nums[i] + 1) * nums[i]  # 배수이면서 최소값으로 업데이트
print(speed)
