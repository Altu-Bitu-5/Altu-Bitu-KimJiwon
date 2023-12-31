"""
    좌표의 값을 1씩 누적해가면서 구하면 된다.
"""


def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i > 0) and (j > 0) and (board[i][j] != 0):
                board[i][j] = (
                    min(board[i][j - 1], board[i - 1][j], board[i - 1][j - 1]) + 1
                )

                answer = max(answer, board[i][j])
            return answer**2  # 넓이 구하기
