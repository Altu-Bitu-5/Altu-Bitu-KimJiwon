import sys

input = sys.stdin.readline

"""
    두 단어가 같은 구성을 갖는 경우 👉 두 단어의 길이가 같고, 구성하는 문자의 종류가 모두 같은 경우
    한 단어의 한 문자를 다른 문자로 바꾸어 같은 구성을 갖게 하는 경우 👉 두 단어의 길이가 같고, 구성하는 문자의 종류가 하나 차이나는 경우
    한 단어에서 한 문자를 더하거나, 빼서 같은 구성을 갖게 하는 경우 👉 두 단어의 길이가 1 차이가 나고, 구성하는 문자의 종류가 하나 차이나는 경우
"""


N = int(input())
target_str = input().strip()  # 양 끝 공백 삭제
str_list = [input().strip() for _ in range(N - 1)]
ans = 0

for alpha_str in str_list:
    if (
        abs(len(alpha_str) - len(target_str)) > 1
        or len(set(target_str).difference(set(alpha_str))) > 1
    ):  # alpha_str이 target_str과 길이와 구성하는 문자의 종류가 하나 넘게 차이가 나면 무시 -> set에 문자열을 넣으면 문자 단위로 쪼개짐
        continue
    for t in target_str:
        if t in alpha_str:
            alpha_str = alpha_str.replace(t, "", 1)
    if len(alpha_str) <= 1:
        ans += 1

print(ans)
