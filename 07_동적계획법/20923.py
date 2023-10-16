# 카드의 개수와 게임 진행횟수

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
do_queue = deque()
su_queue = deque()

for _ in range(N):
    do, su = map(int, sys.stdin.readline().split())
    do_queue.append(do)
    su_queue.append(su)

do_check = 0
su_check = 0

do_tmp = deque()
su_tmp = deque()

for m in range(M):
    if m % 2 == 0:  # do 차례
        do_check = do_queue.pop()
        do_tmp.append(do_check)  #  앞으로 추가하고
    else:  # su 차례
        su_check = su_queue.pop()
        su_tmp.append(su_check)

    if len(do_queue) == 0:
        print("su")
        exit()
    elif len(su_queue) == 0:
        print("do")
        exit()

    if (
        (do_check + su_check == 5) and (do_check != 0) and (su_check != 0)
    ):  # 두 카드를 합쳐서 5가 나오면,
        if do_tmp:
            su_queue.extendleft(do_tmp)  # 뒤에서 제거한다.
            do_check = 0
            do_tmp = deque()
        if su_tmp:
            su_queue.extendleft(su_tmp)
            su_check = 0
            su_tmp = deque()

    elif (do_check == 5) or (su_check == 5):  # 5짜리 카드가 나오면,
        if su_tmp:
            do_queue.extendleft(su_tmp)
            su_check = 0
            su_tmp = deque()
        if do_tmp:
            do_queue.extendleft(do_tmp)
            do_check = 0
            do_tmp = deque()

if len(do_queue) > len(su_queue):
    print("do")
elif len(do_queue) < len(su_queue):
    print("su")
elif len(do_queue) == len(su_queue):
    print("dosu")
