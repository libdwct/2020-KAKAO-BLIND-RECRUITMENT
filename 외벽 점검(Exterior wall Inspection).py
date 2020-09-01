'''
name : ByeongJun Ahn
nation : KOREA
contact : 010-2736-5474 or ahnbj0@naver.com
source: 2020 KAKAO BLIND RECRUITMENT "외벽 점검"
comment : weak를 점검하는 친구들의 경우의 수를 모두 permutation으로 구하여 완전검색하였다.
dist <= 8이라는 조건이 있어서 완전검색이 가능했지만, 크기가 커진다면 비효율적인 방법이다.
'''

from collections import deque
from itertools import permutations


def match(r, case):
    start = r[0]
    idx = 1
    for i in range(len(case)):
        end = start + case[i]
        while True:
            if r[idx] <= end:
                idx += 1
            else:
                break
            if idx >= len(r):
                return True

        start = r[idx]

    return False


def solution(n, weak, dist):
    deq = deque(weak)
    rotated = []
    rotated.append(weak[:])
    for _ in range(len(deq) - 1):
        temp = deq.popleft()
        deq.append(temp + n)
        lt = list(deq)
        rotated.append(lt[:])

    cnt = 1
    while True:
        friends = dist[-cnt:]
        cases = permutations(friends, cnt)
        for case in cases:
            for r in rotated:
                if match(r, case):
                    return cnt
        cnt += 1
        if cnt > len(dist):
            return -1

# Example1
n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
expected_result = 2

print(solution(n, weak, dist))

# Example2
n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]
expected_result = 1

print(solution(n, weak, dist))