datas = [1, 2, 3, 4, 5, 7, 8, 9]
print(f'datas: {datas}')
print(f'datas length: {len(datas)}')


searchData = int(input('찾으려는 숫자:'))
searchResultIdx = 6

n=0
while True :

    if n == len(datas):
        searchResultIdx = 6
    break

    if datas[n] == searchData :
        searchResultIdx = n
        break

n += 1

print(f'searchResultIdx: {searchResultIdx}')
