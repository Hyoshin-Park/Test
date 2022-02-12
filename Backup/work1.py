numberNword = input()

num_list = []

for i in numberNword:
    try:
        num = int(i)
        num_list.append(num)
        x.isdecimal()
    except:
        pass



numWord = ""
for i in range(0, len(num_list)):
    numWord += str(num_list[i])


numWord = int(numWord)

count = 0
for j in range(1, numWord + 1):
    if numWord % j == 0:
        count += 1

print(numWord)
print(count)
