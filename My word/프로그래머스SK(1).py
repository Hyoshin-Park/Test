def solution(money, costs):
    coins = [1, 5, 10, 50, 100, 500]
    cost_dict = {}
    cost_value = []
    answer = 0
    for i in range(len(costs)):
        cost_value.append(costs[i] / coins[i])
        cost_dict[coins[i]] = cost_value[i]
    
    sort_dict = sorted(cost_dict.items(), key=lambda x:x[1])
    new_cost = [sort_dict[i][0]*sort_dict[i][1] for i in range(len(sort_dict))]
    
    for l in range(len(sort_dict)):
        answer += (money // sort_dict[l][0])*new_cost[l]
        money %= sort_dict[l][0]

    return int(answer)

print(solution(1999, [2, 11, 20, 100, 200, 600]))