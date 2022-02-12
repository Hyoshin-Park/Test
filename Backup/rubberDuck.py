cars = ("Truck", "SUV", "miniVan")

n = 0
while n < len(cars):
    print(cars[n])
    n += 1

n= 0
flag = True
while flag:
    print(cars[n])
    n +=1

    if n == len(cars):
        flag = False

n = 0
while True:
    print(cars[n])
    n += 1

    if n == len(cars):
        break

minscore = 60

scores = (("국어", 62), ("수학", 58))

n = 0
while n < len(scores):
    if scores[n][1] >= minscore:
        n +=1
        continue
    print(scores[n][0], scores[n][1])
    n += 1





dict = {"s1":"전영주", "s2": "유민우", "s3": "박효신"}
# s1 key 이름은 value  key:value 자체가 아이템(요소)
key 에는 변경 불가능한거 value 변경 가능한 것도

print(dict["s1"])

print(dict.get("s1"))

dict["s4"] = "김지현"
