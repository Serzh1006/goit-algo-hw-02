from collections import deque

def is_palindrome(text):
    d = deque()
    format_text = "".join([i.lower() for i in text if i.isalpha()])
    for i in format_text:
        d.append(i)
    
    while len(d)>1:
        if d.pop() != d.popleft():
            return "\nНе Паліндром"
    return "\nПаліндром"


print(is_palindrome("QWff  JHB42"))
print(is_palindrome("ra dar__"))
print(is_palindrome("lev535el"))
print(is_palindrome("cIVic"))
print(is_palindrome("rotor"))
print(is_palindrome("elephant"))
print(is_palindrome("Tomato"))
print(is_palindrome("Computer"))