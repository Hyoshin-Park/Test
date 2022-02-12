string = input()
stack = []
for i in string:
    if i == ')':
        while stack.pop() != '(':
            pass
    else:
        stack.append(i)
print(''.join(stack))
