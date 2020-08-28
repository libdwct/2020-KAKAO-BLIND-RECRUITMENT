'''
name : ByeongJun Ahn
nation : KOREA
contact : 010-2736-5474 or ahnbj0@naver.com
source: 2020 KAKAO BLIND RECRUITMENT "가사 검색"
comment : 문자열 검색 시 Trie 자료구조에 대한 지식이 없는 상태로 선형 구조로 구현하였는데,
효율성 테스트를 통과하지 못하였다. 아래는 선형 검색 구조로 구현한 알고리즘이다.
'''

def match(q, w):
    N = 0
    if q.startswith("?"):
        for i in range(len(q)):
            if q[i] != "?":
                N = i
                break
        for letter1, letter2 in zip(q[N:], w[N:]):
            if letter1 != letter2:
                return False

    else:
        for i in range(len(q)):
            if q[len(q) - i - 1] != "?":
                N = i
                break
        for letter1, letter2 in zip(q[:len(q) - N], w[:len(q) - N]):
            if letter1 != letter2:
                return False

    return True


def counting(q, words):
    cnt = 0
    for w in words:
        if len(w) != len(q):
            continue
        if match(q, w):
            cnt += 1

    return cnt


def solution(words, queries):
    answer = []
    for q in queries:
        answer.append(counting(q, words))

    return answer


# Example
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
expected_result = [3, 2, 4, 1, 0]

print(solution(words, queries))