def solution(area):
    width = []
    height = []
    area_list = []
    
    for i in range(1, 100000):
        if area % i == 0:

            width.append(i)
            height.append(area // i)
            area_list.append(height[-1] - width[-1])
            print(width, height, area_list)
        if area_list[-1] < 0:
            area_list.pop()
            break

    m = min(area_list)
    min_index = area_list.index(m)

    return [width[min_index], height[min_index]]
print(solution(100000))