import heapq

"""
    먼저 문제 풀이 로직은 가장 마지막에 시작한 작업의 시작시간과 종료되었을 때 시간(현재 시간) 사이에서 가장 처리 시간이 적은 작업을 차례대로 시작하면 된다.
    처리 대상이 되는 작업의 후보군은 가장 마지막에 시작한 작업의 시작시간과 종료시간(현재 시간) 사이에 요청이 들어온 모든 작업으로 
    처리 소요 시간이 적은 작업을 우선적으로 처리하기 위해 최소 힙을 사용하고 요청 시간과 소요 시간의 자리를 변경하여 힙에 push 한다.
    힙에 삽입된 작업을 하나씩 pop 하며 작업의 시작시간과 종료시간(현재 시간)을 갱신하며 모든 작업을 처리할 때까지 반복한다.
"""


def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []

    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])

        if len(heap) > 0:  # 처리할 작업이 있는 경우
            cur = heapq.heappop(heap)  # 우선순위가 가장 높은 job을 수행 -> [0,3]
            start = now
            now += cur[0]  # 0
            answer += now - cur[1]  # 작업 요청시간부터 종료시간까지의 시간 계산
            i += 1
        else:  # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1

    return answer // len(jobs)
