# This function will check to see if parentheses are balanced.
# ie: It will check to see if opening and closing parentheses match.
# Ex: ()() is an example of a balanced string
# Ex: (() is an example of an unbalanced string
def balanced(s):
    b = []
    p = False
    for c in s:
        if c in ['(','[','{']:
            b.append(c)
        elif (((c == ')') and (peek(b) == '(')) or
              ((c == ']') and (peek(b) == '[')) or
              ((c == '}') and (peek(b) == '{'))):
                 b.pop()
        else: p = True
    return (len(b) == 0) and not p

def peek(A):
    if len(A) == 0: return ''
    else: return A[len(A) - 1]
