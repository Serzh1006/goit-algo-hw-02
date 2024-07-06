def is_balanced(s):
    stack = []
    opening = "({["
    closing = ")}]"
    matches = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack[-1] != matches[char]:
                return False
            stack.pop()

    return not stack

def main():
    s = input("Enter a sequence of delimiters: ").strip()
    if is_balanced(s):
        print("Симетрично.")
    else:
        print("Несиметрично.")

if __name__ == "__main__":
    main()