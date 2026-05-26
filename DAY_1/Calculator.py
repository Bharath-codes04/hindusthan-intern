def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot Divide by Zero"
    else:
        return a / b

while True:
    print("\n1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    ch = int(input("Enter choice : "))
    if ch >= 1 and ch <= 4:
        n1 = float(input("Enter first number : "))
        n2 = float(input("Enter second number : "))

        if ch == 1:
            print("Result :", add(n1, n2))
        elif ch == 2:
            print("Result :", sub(n1, n2))
        elif ch == 3:
            print("Result :", mul(n1, n2))
        elif ch == 4:
            print("Result :", div(n1, n2))

    elif ch == 5:
        break
    else:
        print("Invalid Choice")