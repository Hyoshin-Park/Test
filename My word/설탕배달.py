N = int(input())

bag = 0

while True:
    if N % 5 == 0:
        bag += N //5
        print(bag)
        break
    N -= 3
    bag += 1

    if N < 0:
        print("-1")
        break