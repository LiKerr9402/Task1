print("Введите числа:")

r = 0
a = int(input())
z = input()
b = int(input())


if z in ("+", "-", "*", "/", "^"):
    if z == "+":
        r = a + b
    elif z == "-":
        r = a - b
    elif z == "*":
        r = a * b
    elif z == "/":
        if b == 0:
            print("Делить на ноль нельзя!")
            exit(0)
        r = a / b
    elif z == "^":
        r = a ** b
        if b == 0:
            r = 1
else:
    print("Неверный знак.")
    exit(1)

z = input()
while z != "=":
    if z in ("+", "-", "*", "/", "^"):
        a = int(input())
        if z == "+":
            r = r + a
        elif z == "-":
            r = r - a
        elif z == "*":
            r = r * a
        elif z == "/":
            if a == 0:
                print("Делить на ноль нельзя!")
                exit(1)
            r = r / a
        elif z == "^":
            r = r ** a
            if a == 0:
                r = 1
    else:
        print("Неверный знак.")
        exit(1)
    z = input()

print(r)
