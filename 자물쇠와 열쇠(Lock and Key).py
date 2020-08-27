'''
name : ByeongJun Ahn
nation : KOREA
contact : 010-2736-5474 or ahnbj0@naver.com
source: 2020 KAKAO BLIND RECRUITMENT "자물쇠와 열쇠"
'''


def correct_check(key, lock):
    n = len(lock)
    for i in range(n):
        for j in range(n):
            if key[i][j] + lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    len_key = len(key)
    len_lock = len(lock)

    key1 = [[0] * len_lock for _ in range(len_lock)]
    key2 = [[0] * len_lock for _ in range(len_lock)]
    key3 = [[0] * len_lock for _ in range(len_lock)]
    key4 = [[0] * len_lock for _ in range(len_lock)]

    for i in range(len_key):
        for j in range(len_key):
            key1[i][j] = key[i][j]
            key2[j][len_key-i-1] = key[i][j]
            key3[len_key - i - 1][len_key - j - 1] = key[i][j]
            key4[len_key - j - 1][i] = key[i][j]

    for k in [key1, key2, key3, key4]:
        for i in range(len_lock):
            for j in range(len_lock):
                left_up_key = [row[i:] + [0]*i for row in k[j:]] + [[0]*len_lock]*j
                if correct_check(left_up_key, lock):
                    return True

                left_down_key = [[0]*len_lock]*j + [row[i:] + [0]*i for row in k[:len_lock - j]]
                if correct_check(left_down_key, lock):
                    return True

                right_up_key = [[0]*i + row[:len_lock - i] for row in k[j:]] + [[0]*len_lock]*j
                if correct_check(right_up_key, lock):
                    return True

                right_down_key = [[0]*len_lock]*j + [[0]*i + row[:len_lock - i] for row in k[:len_lock - j]]
                if correct_check(right_down_key, lock):
                    return True

    return False

# Example
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
print("key")
for i in key:
    print(i)
lock = [[1, 1, 1, 0], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
print("lock")
for i in lock:
    print(i)


print(solution(key, lock))

