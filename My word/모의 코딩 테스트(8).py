def solution(history, infected):
    find_infected = history.count(infected)
    abs_list = []
    print(find_infected)
    for i in range(find_infected):
        infect_index = history.index(infected)
        infect_index1 = history.index(infected*(-1))
        infect_list = history[infect_index+1:infect_index1]
        history.remove(infected)
        history.remove(infected*(-1))
        for j in infect_list:
            abs_list.append(abs(j))
        print(history, infect_list, abs_list)

    abs_list = list(set(abs_list))

    

    return abs_list

print(solution([3, 2, -3, 1, -1, -2, 4, -4, 1, -1, 2, 4, -4, 1, 5, -5, -2, -1], 1))

