line = input()

stack = ''
ans = True

for char in line:
    if char in '([{':
        stack += char
    elif char == ')' and stack and stack[-1] == '(':
        stack = stack[:-1]
    elif char == ']' and stack and stack[-1] == '[':
        stack = stack[:-1]
    elif char == '}' and stack and stack[-1] == '{':
        stack = stack[:-1]
    else:
        ans = False
        break

if len(stack) == 0 and ans:
    print('yes')
else:
    print('no')