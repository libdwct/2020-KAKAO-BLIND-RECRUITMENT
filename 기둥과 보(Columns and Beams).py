'''
name : ByeongJun Ahn
nation : KOREA
contact : 010-2736-5474 or ahnbj0@naver.com
source: 2020 KAKAO BLIND RECRUITMENT "기둥과 보"
comment : 기둥과 보 제거 알고리즘을 조건 별로 따져서 구현 했더니 코드 길이가 길어졌다.
다른 아이디어를 보니 제거 후 역으로 남은 것들이 설치가 가능한지를 따지는 알고리즘이 있었는데,
시간복잡도는 증가하지만 코드가 훨씬 간결해진다.
'''

from collections import defaultdict

def construct(build):
    global data
    x = build[0]
    y = build[1]
    if build[2] == 0:  # 기둥 설치
        if y == 0:  # 바닥일 경우
            data[(x, y)][0] = 1
            data[(x, y + 1)][1] = 1
            return

        if data[(x, y)][1] == 1:  # 아래에 기둥이 있을 경우
            data[(x, y)][0] = 1
            data[(x, y + 1)][1] = 1
            return

        if data[(x, y)][2] == 1 or data[(x, y)][3] == 1:  # 보 위인 경우
            data[(x, y)][0] = 1
            data[(x, y + 1)][1] = 1
            return

        return  # 설치 실패

    else:  # 보 설치
        if data[(x, y)][1] == 1 or data[(x + 1, y)][1] == 1:  # 기둥 위
            data[(x, y)][3] = 1
            data[(x + 1, y)][2] = 1
            return

        if data[(x, y)][2] == 1 and data[(x + 1, y)][3] == 1:  # 양쪽 보
            data[(x, y)][3] = 1
            data[(x + 1, y)][2] = 1
            return

        return  # 보 설치 실패


def delete(build):
    global data
    x = build[0]
    y = build[1]
    if build[2] == 0:  # 기둥 삭제
        if data[(x, y + 1)][0] == 1:  # 위에 기둥이 있을 경우
            if data[(x, y + 1)][2] == 0 and data[(x, y + 1)][3] == 0:  # 지탱해 줄 보가 없을 경우
                return  # 삭제 실패

        if data[(x, y + 1)][2] == 1:  # 기둥 위에 왼쪽 보 존재 시
            if data[(x - 1, y)][0] == 0:
                if data[(x - 1, y + 1)][2] == 0 or data[(x, y + 1)][3] == 0:
                    return
        if data[(x, y + 1)][3] == 1:  # 기둥 위에 오른쪽 보 존재 시
            if data[(x + 1, y)][0] == 0:
                if data[(x, y + 1)][2] == 0 or data[(x + 1, y + 1)][3] == 0:
                    return

        data[(x, y)][0] = 0
        data[(x, y + 1)][1] = 0

        return  # 삭제 성공

    else:  # 보 삭제
        if data[(x, y)][0] == 1:  # 보 왼쪽 위에 기둥 존재 시
            if data[(x, y)][1] == 0:  # 아래 기둥 부재 시
                if data[(x, y)][2] == 0:  # 지탱해 줄 다른 보 부재 시
                    return  # 삭제 실패

        if data[(x + 1, y)][0] == 1:  # 보 오른쪽 위에 기둥 존재 시
            if data[(x + 1, y)][1] == 0:
                if data[(x + 1, y)][3] == 0:
                    return

        if data[(x, y)][2] == 1:  # 왼쪽에 이어진 보 존재 시
            if data[(x - 1, y)][1] == 0 and data[(x, y)][1] == 0:  # 기둥 부재 시
                return

        if data[(x + 1, y)][3] == 1:  # 오른쪽에 이어진 보 존재 시
            if data[(x + 1, y)][1] == 0 and data[(x + 2, y)][1] == 0:
                return

        data[(x, y)][3] = 0
        data[(x + 1, y)][2] = 0

        return  # 삭제 성공


def solution(n, build_frame):
    global data
    """
    좌표에 기둥과 보의 설치 여부를 담는 딕셔너리
    좌표 기준으로 [위쪽 기둥, 아래쪽 기둥, 왼쪽 보, 오른쪽 보] 순서로
    설치되어 있을 시 1, 그렇지 않으면 0 값을 가짐
    """
    data = defaultdict(lambda: [0, 0, 0, 0])
    for build in build_frame:
        if build[3] == 1:
            construct(build)
        else:
            delete(build)

    temp = list(data.keys())
    temp.sort(key=lambda x: x[1])
    temp.sort(key=lambda x: x[0])
    answer = []
    for t in temp:
        if data[t][0] == 1:
            answer.append([t[0], t[1], 0])
        if data[t][3] == 1:
            answer.append([t[0], t[1], 1])

    return answer


# Example 1
n= 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
expected_result = [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
print(solution(n, build_frame))

# Example 2
n=5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
expected_result = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
print(solution(n, build_frame))