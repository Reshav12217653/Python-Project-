name_of_client = "Reshav Singh"
balance = 10000
account_number = 1234567891


def init():
    print("Welcome Mr.", name_of_client)
    print("Your Account Number:", account_number)
    print("Available Balance:", balance)
    action()


def action():
    print("\n\tChoose your action\n")
    print("\tKey\t\t\tAction")
    print("\t 1\t\tCash Withdrawal")
    print("\t 2\t\tCash Deposit")
    print("\t 3\t\tDisplay Balance")
    key = int(input("Action: "))
    if 3 >= key >= 1:
        if key == 1:
            withdrawal()
        elif key == 2:
            deposit()
        else:
            display()
    else:
        print("Invalid Key Entered ! \nEnter valid key again")
        action()


def withdrawal():
    global balance
    amount = int(input("Enter amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient Balance")
    else:
        balance -= amount
        print("Amount withdrawal successful !")
        display()


def deposit():
    global balance
    amount = int(input("Enter amount to be deposited: "))
    balance += amount
    print("Amount deposited successfully !")
    display()


def display():
    print("Your clearing balance:", balance)
    if balance < 5000:
        print("Low Balance !")
    print("Thank You for using ABC Bank ATM !")


init()