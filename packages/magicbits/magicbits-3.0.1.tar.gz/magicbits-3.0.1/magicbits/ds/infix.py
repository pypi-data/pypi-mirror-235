PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities  
def infix_to_postfix(expression: str) -> str:
    stack = []
    output = ''
    for ch in expression:
        if ch.isnumeric():
            output += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    while stack:
        output += stack.pop()
    return output
if __name__ == '__main__':
    expression = input('Enter infix expression: ')
    print('infix expression: ',expression)
    print('postfix expression: ',infix_to_postfix(expression))
