#Yoo 1

n1 = input("Enter a number: ")
n2 = input("Enter a number: ")

try:
    n2 = int(n2)
    n1 = int(n1)

except:
    print("Error print a number")
else:
    num = n1 + n2
    print(num)

#JYJ 1

n1 = 10; n2 = 0

try:
    print(n1 / n2)
except Exception:
    print("예상치 못한 예외가 발생했습니다")

print(n1 * n2)
print(n1 - n2)
print(n1 + n2)
