"""
    처음 스피드는 가장 마지막 데이터로 두고, 역방향 순차 탐색 실시

"""

n = int(input())  # 5
nums = list(
    map(int, input().split())
)  # 300 400 500 400 300 (900 < 800 < 500 < 400 < 300)
speed = nums[-1]  # 맨 마지막 원소 300

for i in range(n - 1, -1, -1):  # 뒤에서 두번째부터 역순으로
    if nums[i] > speed:  # speed보다 행성 속력이 크다면
        speed = nums[i]  # speed를 현재 행성 속력으로 업데이트
    else:
        if speed % nums[i]:  # 정수배가 되지 않는다면
            speed = (speed // nums[i] + 1) * nums[i]  # 배수이면서 최소값으로 업데이트
print(speed)
