print("Write an equation. Press Enter after each number and symbol.")
num1 = float(input())
mode = str(input())
num2 = float(input())
if mode in ('+', '-', '*', '/'):
    if mode == '+':
        print(num1, "+", num2, "=", (num1 + num2))
    elif mode == '-':
        print(num1, "-", num2, "=", (num1 - num2))
    elif mode == '*':
        print(num1, "*", num2, "=", (num1 * num2))
    elif mode == '/':
        print(num1, "/", num2, "=", (num1 / num2))
else:
    print("Invalid input.")
