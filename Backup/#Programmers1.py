def solution(new_id):
    temp = new_id.lower()
    answer = ""

    for i in temp:
        if i == '-' or i == '_' or i == '.' or i.isdigit() or i.isalpha():
            answer += i

    answer += '!'
    print(answer)
    for idx, count in enumerate(answer):
        if idx <= len(answer) - 1:
            while answer[idx] == '.' and answer[idx + 1] == '.':
                answer = answer[:idx] + answer[idx + 1:]
    print(answer)
    answer = answer[:-1]
    if answer[0] == '.' and len(answer) == 1:
        answer = ''
    elif answer[0] == '.':
        answer = answer[1:]
    elif answer[-1] == '.':
        answer = answer[:-1]

    if not len(answer):
        answer = 'a'
    else:
        answer = answer[:15]

    if answer[-1] == '.':
        answer = answer[:-1]
    print(answer)
    if len(answer) <= 2:
        t = answer[-1]
        while len(answer) != 3:
            answer += t

    return answer

solution("123_.def"
)
