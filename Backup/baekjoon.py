alp = input().lower()

word = list(set(alp))
alp_list = []

for i in word:
    count = alp.count(i)
    alp_list.append(count)

if alp_list.count(max(alp_list)) >= 2:
    print("?")
else:
    print(word[alp_list.index(max(alp_list))].upper())
