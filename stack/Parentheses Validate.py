
def solve(s):
    stack = []
    for it in s:
        if it == '(':
            stack.append(')')
        elif it == ')':
            if len(stack) == 0 or stack.pop() != ')':
                return 0
    return 1 if len(stack) == 0 else 0


if __name__ == "__main__":
    print(solve('()'))  # 1
    print(solve('()()'))  # 1
    print(solve('((()))'))  # 1
    print(solve(')('))  # 0
    print(solve(')))'))  # 0
    print(solve('((('))  # 0
