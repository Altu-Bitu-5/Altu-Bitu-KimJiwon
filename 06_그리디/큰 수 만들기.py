def solution(number, k):
    answer = []

    for i in number:
        while k > 0 and answer and answer[-1] < i:
            answer.pop()
            k -= 1
        answer.append(i)

    return "".join(answer[:-k])


"""
    sliding window와 비슷한 방법으로 사용, 
    앞에서부터 시작하여 [뺄 수 있는 숫자가 남아 있는 범위 안]에서 최댓값을 선택한다.
"""
