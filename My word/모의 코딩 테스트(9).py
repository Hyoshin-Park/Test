
import numpy as np

def solution(lineUp, level):
    posi = np.where(np.array(lineUp) == 1)[0]
    print(posi)
    posi.sort(reverse=True)
    bool_list = []
    for i in range(len(posi)):
        if abs(posi[i] - posi[i+1]) >= level:
            bool_list.append("True")
        else:
            bool_list.append("False")
        
    if "False" in bool_list:
        return False
    else:
        return True
        

print(solution([1, 0, 0, 0, 1, 0, 0, 1], 2))