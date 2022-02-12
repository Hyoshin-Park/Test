def solution(lottos, win_nums):

    answer = [6, 6, 5, 4, 3, 2, 1]

    together = set(win_nums) - set(lottos)
    min = len(lottos) - len(together)
    max = 0
    cnt0 = lottos.count(0)
    max = min + cnt0

    return [answer[max], answer[min]]
