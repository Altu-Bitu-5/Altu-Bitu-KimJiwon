import sys
from collections import deque


def solution(N, E, M, firstInfected):
    queue = deque([])  # 감염된 사람의 번호를 큐에 저장
    answer = [-1] * (N + 1)  # solution 함수에서 리턴할 배열
    turn = [0] * (N + 1)  # 감염까지 남은 주변 비감염 사람 수

    # 최조생성자 처리
    for t in firstInfected:
        queue.append(t)  # 최조생성자는 감염된 사람이고 주변인에게 영향을 주므로 큐에 넣어주고
        answer[t] = 0  # 0분에 감염

    # 주변인의 절반 이상이 루머를 믿을 때 본인도 루머를 믿으므로
    # 몇 명이 감염되었을 때 자신이 감염되는지에 대한 정보를
    # 사람 i의 주변인물 수 + 1 / 2의 몫으로 저장해둔다.
    # 사람의 번호가 아닌 입력의 끝을 말하는 0이 adj 배열에 포함되어 있으므로 + 1은 안해도 된다.
    for i in range(1, N + 1):
        turn[i] = (len(E[i])) // 2  # 1

    while queue:  # 큐가 빌 때까지 탐색 -> 비어있다면 모든 탐색 종료
        current = queue.popleft()  # 현재, 가장 먼저 감염된 사람의
        for next in E[current]:  # 주변인물들에게
            if next == 0:
                break
            turn[next] -= 1  # 자신(주변인물)이 감염되기까지 남은 사람 수를 1 빼고
            if (
                answer[next] == -1 and turn[next] <= 0
            ):  # 만약 아직 감염되지 않았고 주변인의 반 이상이 감염되었다면
                queue.append(next)  # 감염되었기에 큐에 자신의 번호를 넣어주고
                answer[next] = answer[current] + 1
                # 자신을 감염시킨 마지막 주변인의 감염된 시간 + 1분을 더해 저장

    return answer[1:]  # 배열 인덱스 1부터 저장했으니 1부터 반환


input = sys.stdin.readline
N = int(input())  # 7
E = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    E[i] = list(map(int, input().split()))
    """
        E=[[2,3,0], [1,3,0], [1,2,4,0], [3,5,0], [4,0], [0], [0]]
    """

M = int(input())  # 2
firstInfected = list(map(int, input().split()))  # 1 6
print(" ".join(map(str, solution(N, E, M, firstInfected))))  # 0 1 2 3 4 0 -1
