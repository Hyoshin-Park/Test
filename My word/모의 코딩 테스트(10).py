# from collections import deque


# def solution(l):
    
#     while True:
#         stack = deque()
#         cnt = 0
#         for i in range(len(l)):
#             while len(stack) != 0 and l[stack[-1]] > l[i]:
#                 tmp = stack.pop
            
#             if len(stack) == 0:
#                 width = i
#             else:
#                 width = i - stack[-1] - 1
#             cnt = max(cnt, width * l[tmp])
#         stack.append(i)

#         while len(stack) != 0:
#             tmp = stack.pop

#             if len(stack) == 0:
#                 width = len(l)
#             else:
#                 width = len(l) - stack[-1] - 1
#             cnt = max(cnt, width* l[tmp])
    
#         return cnt
# print(solution([1, 10, 10, 10, 5]))

# import sys

# def solution(l):
#     while True:
#         tmp = list(map(int, sys.stdin.readline().split()))
#         if tmp[0] == 0:
#             break
#         max = tmp[0]
#         for i in range(tmp[0]):
#             for j in range(2, tmp[i + 1] + 1):
#                 k = 1
#                 while True:
#                     try:
#                         if j <= tmp[i + k + 1]:
#                             k += 1
#                         else:
#                             break
#                     except:
#                         break
#                 if k * j > max:
#                     max = k * j
#         print(max)

# import sys
# input = sys.stdin.readline



def solution(l):
    while True:
        answer = 0
        stack = []

        for val in l:
            tmp = 0
            while len(stack) != 0 and stack[-1][0] > val:
                tmp += stack[-1][1]  # 스택이 갖고 있던 밑변 값을 넘겨준다
                answer = max(answer, tmp * stack[-1][0])
                stack.pop()

            tmp += 1
            stack.append([val, tmp])  # 높이와 밑변

        tmp = 0
        while len(stack) != 0:  # 남은 값들 처리
            tmp += stack[-1][1]
            answer = max(answer, tmp*stack[-1][0])
            stack.pop()

        return(answer)

print(solution([1, 10, 10, 10, 5]))