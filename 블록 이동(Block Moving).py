'''
name : ByeongJun Ahn
nation : KOREA
contact : 010-2736-5474 or ahnbj0@naver.com
source: 2020 KAKAO BLIND RECRUITMENT "블록 이동"
comment : 전형적인 BFS 문제이다.
'''

from collections import deque


def isSafe(x, y, vh, board):
    N = len(board)
    if vh == 0:
        return 0 <= x < N and 1 <= y < N and board[x][y] == 0 and board[x][y-1] == 0
    if vh == 1:
        return 1 <= x < N and 0 <= y < N and board[x][y] == 0 and board[x-1][y] == 0


def rotation(curr, board, visited_h, visited_v):
    N = len(board)
    x = curr[0]
    y = curr[1]
    result = []
    if curr[2] == 0:
        if isSafe(x, y - 1, 1, board) and visited_v[x][y - 1] == 0:
            if board[x - 1][y] == 0:
                result.append([x, y - 1, 1, curr[3] + 1])
                visited_v[x][y - 1] = 1

        if isSafe(x, y, 1, board) and visited_v[x][y] == 0:
            if board[x - 1][y - 1] == 0:
                result.append([x, y, 1, curr[3] + 1])
                visited_v[x][y] = 1

        if isSafe(x + 1, y - 1, 1, board) and visited_v[x + 1][y - 1] == 0:
            if board[x + 1][y] == 0:
                result.append([x + 1, y - 1, 1, curr[3] + 1])
                visited_v[x + 1][y - 1] = 1

        if isSafe(x + 1, y, 1, board) and visited_v[x + 1][y] == 0:
            if board[x + 1][y - 1] == 0:
                result.append([x + 1, y, 1, curr[3] + 1])
                visited_v[x + 1][y] = 1

    if curr[2] == 1:
        if isSafe(x - 1, y, 0, board) and visited_h[x - 1][y] == 0:
            if board[x][y - 1] == 0:
                result.append([x - 1, y, 0, curr[3] + 1])
                visited_h[x - 1][y] = 1

        if isSafe(x, y, 0, board) and visited_h[x][y] == 0:
            if board[x - 1][y - 1] == 0:
                result.append([x, y, 0, curr[3] + 1])
                visited_h[x][y] = 1

        if isSafe(x - 1, y + 1, 0, board) and visited_h[x - 1][y + 1] == 0:
            if board[x][y + 1] == 0:
                result.append([x - 1, y + 1, 0, curr[3] + 1])
                visited_h[x - 1][y + 1] = 1

        if isSafe(x, y + 1, 0, board) and visited_h[x][y + 1] == 0:
            if board[x - 1][y + 1] == 0:
                result.append([x, y + 1, 0, curr[3] + 1])
                visited_h[x][y + 1] = 1

    return result


def solution(board):
    N = len(board)
    deq = deque()
    deq.append([0, 1, 0, 0])
    # 3번재 요소는 로봇이 가로일 때 0, 세로일 때 1
    # 4번째 요소는 이동 횟수
    visited_h = [[0] * len(board) for _ in range(len(board))]  # 가로
    visited_h[0][1] = 1
    visited_v = [[0] * len(board) for _ in range(len(board))]  # 세로
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while True:
        curr = deq.popleft()
        for i in range(4):
            next_x = curr[0] + dx[i]
            next_y = curr[1] + dy[i]

            if isSafe(next_x, next_y, curr[2], board):
                if next_x == N - 1 and next_y == N - 1:
                    return curr[3] + 1
                if curr[2] == 0 and visited_h[next_x][next_y] == 0:
                    deq.append([next_x, next_y, curr[2], curr[3] + 1])
                    visited_h[next_x][next_y] = 1
                if curr[2] == 1 and visited_v[next_x][next_y] == 0:
                    deq.append([next_x, next_y, curr[2], curr[3] + 1])
                    visited_v[next_x][next_y] = 1
        deq.extend(rotation(curr, board, visited_h, visited_v))

# Example
board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
expected_result = 7

print(solution(board))