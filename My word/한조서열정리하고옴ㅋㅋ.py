N = int(input())
num = list(map(int, input().split()))

list = []

max_i = 0

for i in num:
    if i > max_i:
        count = 0
        max_i = i 
    else:
        count += 1
    list.append(count)
print(max(list))


# for i in range(N):
#     count = 0
#     for j in range(i + 1, N):
#         if num[i] > num[j]:
#             count += 1
#         else:
#             break
#     list.append(count)
# print(max(list))



# while True:
#     if N == 1:
#         print(count)
#         break
#     if num[i] > num[i+1]:
#         count += 1
#         num.pop(i+1)
#         continue
#     elif num[i] < num[i+1]:
#         if len(num[i+1:-1]) > count :
        
#             count = 0
#             i += 1
#             num.pop(0)
#     if len(num) == 1:
#         print(count)
#         break
    

