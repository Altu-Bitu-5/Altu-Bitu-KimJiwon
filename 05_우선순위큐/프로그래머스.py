import heapq

"""
    먼저 문제 풀이 로직은 가장 마지막에 시작한 작업의 시작시간과 종료되었을 때 시간(현재 시간) 사이에서 가장 처리 시간이 적은 작업을 차례대로 시작하면 된다.
    처리 대상이 되는 작업의 후보군은 가장 마지막에 시작한 작업의 시작시간과 종료시간(현재 시간) 사이에 요청이 들어온 모든 작업으로 
    처리 소요 시간이 적은 작업을 우선적으로 처리하기 위해 최소 힙을 사용하고 요청 시간과 소요 시간의 자리를 변경하여 힙에 push 한다.
    힙에 삽입된 작업을 하나씩 pop 하며 작업의 시작시간과 종료시간(현재 시간)을 갱신하며 모든 작업을 처리할 때까지 반복한다.
"""


def solution(jobs):
    n_jobs = len(jobs)
    h = []
    result, current_time, i = 0, 0, 0

    start = -1
    while i < n_jobs:
        for job in jobs:
            if start < job[0] <= current_time:
                heapq.heappush(h, [job[1], job[0]])
        if len(h) > 0:
            et, st = heapq.heappop(h)
            start = current_time
            current_time += et
            result += current_time - st
            i += 1
        else:
            current_time += 1
    return int(result / n_jobs)
