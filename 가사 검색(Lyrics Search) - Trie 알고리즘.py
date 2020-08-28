'''
name : ByeongJun Ahn
nation : KOREA
contact : 010-2736-5474 or ahnbj0@naver.com
source: 2020 KAKAO BLIND RECRUITMENT "가사 검색"
comment : trie 자료구조를 이용해 효율성 테스트까지 통과한 알고리즘이다.
          자료 입력 시 특정 철자를 지나친 문자열의 길이를 저장시킨다는 아이디어를 생각하는게 어려웠다.
'''

from collections import defaultdict


class Node(object):
    def __init__(self, key, passnumber=None, isEnd=None):
        self.key = key
        self.passnumber = defaultdict(int)
        self.isEnd = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        curr_node.passnumber[len(string)] += 1
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]
            curr_node.passnumber[len(string)] += 1

        curr_node.isEnd = True

    def search(self, query):
        curr_node = self.head
        for q in query:
            if q == "?":
                break
            if q in curr_node.children:
                curr_node = curr_node.children[q]
            else:
                return 0

        return curr_node.passnumber[len(query)]


def solution(words, queries):
    trie = Trie()
    r_trie = Trie()  # "?"가 앞에 있는 단어들을 뒤에서 부터 검사하기 위한 trie
    r_words = [w[::-1] for w in words]
    dic = {}
    answer = []

    for word in words:
        trie.insert(word)
    for word in r_words:
        r_trie.insert(word)
    for query in queries:
        if query in dic:
            answer.append(dic[query])
            continue
        if query.endswith("?"):
            result = trie.search(query)
            answer.append(result)
            dic["query"] = result

        else:
            result = r_trie.search(query[::-1])
            answer.append(result)
            dic["query"] = result

    return answer

# Example
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
expected_result = [3, 2, 4, 1, 0]

print(solution(words, queries))