def solution(n, s, t):
    word = ("."*n) + s
    if t > len(word):
        t = t%len(word)
    answer = word[t:t+n]

    return answer

print(solution(5, "Snowball", 10))