'''
name : ByeongJun Ahn
nation : KOREA
contact : 010-2736-5474 or ahnbj0@naver.com
source: 2020 KAKAO BLIND RECRUITMENT "문자열 찹축"
'''

def solution(s):
    candidate = []
    if len(s) == 1:
        return 1
    for cut_len in range(1, len(s) // 2 + 1):
        cnt = len(s)  # 반복 문자열이 나오면 차감하는 방식
        rep = 1  # 문자열 반복 횟수(기본:1)
        idx = 0  # 현 위치
        while True:
            if idx + 2 * cut_len - 1 >= len(s):
                if rep != 1:
                    cnt += len(str(rep))  # 문자열 반복 횟수의 길이 추가
                break
            if s[idx:idx + cut_len] == s[idx + cut_len:idx + 2 * cut_len]:
                cnt -= cut_len
                rep += 1
                idx += cut_len
            else:
                if rep != 1:
                    cnt += len(str(rep))
                rep = 1
                idx += cut_len

        candidate.append(cnt)

    return min(candidate)

# Example1
s = "aabbaccc"
expected_result = 7
print(solution(s))

# Example2
s = "ababcdcdababcdcd"
expected_result = 9
print(solution(s))