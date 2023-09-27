# 양 옆 학생에게 빌려줄 수 있다면 왼쪽부터
# 여벌의 체육복이 있는 학생(reverse)도 도난 가능성 O -> lost와 reserve에 동일값이 있다면 그 값은 reserve에서 제외


def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for i in set_reserve:
        if i - 1 in set_lost:
            set_lost.remove(i - 1)  # 왼쪽 학생부터 빌려주고
        elif i + 1 in set_lost:
            set_lost.remove(i + 1)  # 오른쪽 학생 빌려주기
    return n - len(set_lost)
