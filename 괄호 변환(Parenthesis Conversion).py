def correction(s):
    if not s:
        return ""
    u = ""
    sign = 0    # u에 저장된 "(", ")" 갯수 표현. "("이 많으면 양수
    v = ""
    for i in s:     # u, v 분리
        if not u:
            u += i
            if i == "(":
                sign += 1
            else: sign -= 1
        else:
            if i == "(":
                sign += 1
                u += "("
                if sign == 0:
                    break
            else:
                sign -= 1
                u += ")"
                if sign == 0:
                    break

    len_v = len(s)-len(u)
    if len_v == 0:
        v = ""
    else: v = s[-len_v:]

    if u[0] == "(":
        return u + correction(v)

    else:
        new_u = ""
        for i in u[1:len(u) - 1]:
            if i == "(":
                new_u += ")"
            else:
                new_u += "("

        result = "(" + correction(v) + ")" + new_u
        return result


def solution(p):
    answer = correction(p)
    return answer

# Example1
p = "(()())()"
expected_result = "(()())()"
print(solution(p))

# Example2
p = "()))((()"
expected_result = "()(())()"
print(solution(p))