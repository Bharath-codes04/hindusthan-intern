balance = 5000
pin = "1234"
def check_balance():
    print("Balance :", balance)

def deposit():
    global balance
    amt = float(input("Enter amount : "))
    if amt > 0:
        balance = balance + amt
        print("Amount Deposited")
    else:
        print("Invalid Amount")

def withdraw():
    global balance
    amt = float(input("Enter amount : "))
    if amt <= balance:
        balance = balance - amt
        print("Please collect cash")
    else:
        print("Insufficient Balance")

def change_pin():
    global pin
    old = input("Enter old pin : ")
    if old == pin:
        new = input("Enter new pin : ")
        pin = new
        print("PIN Changed")
    else:
        print("Wrong PIN")

while True:
    print("\n1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Change PIN")
    print("5.Exit")

    ch = int(input("Enter choice : "))
    if ch == 1:
        check_balance()
    elif ch == 2:
        deposit()
    elif ch == 3:
        withdraw()
    elif ch == 4:
        change_pin()
    elif ch == 5:
        break
    else:
        print("Invalid Choice")