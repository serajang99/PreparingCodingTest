import sys
input = sys.stdin.readline


while True:
    stack = []
    s = input().rstrip()
    if s == '.':
        break
    for l in s:
        if l in ['(', '{', '[']:
            stack.append(l)
        if l == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(l)
                    break
            else:
                stack.append(l)
                break
        elif l == '}':
            if stack:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(l)
                    break
            else:
                stack.append(l)
                break
        elif l == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(l)
                    break
            else:
                stack.append(l)
                break

    if stack:
        print("no")
    else:
        print("yes")
