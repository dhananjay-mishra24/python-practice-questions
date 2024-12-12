balance = 0

def withdrawl(balance):
    amount_to_withdraw = float(input("What is the amount you want to withdraw: "))
    if amount_to_withdraw > balance:
        return "Insufficient Funds"
    else:
        return balance - amount_to_withdraw

def deposit(balance):
    amount_to_deposit = float(input("What is the amount you want to deposit: "))
    if amount_to_deposit < 0:
        return "Check your amount"
    else:
        return balance + amount_to_deposit

def show_balance(balance):
    return balance


while True:
    print("Hello, Welcome to your Bank")
    print("Please read the instructions before proceeding")
    print("Press 1 for Withdrawl")
    print("Press 2 for Deposit")
    print("Press 3 for Checking Balance")
    print("Press 4 to Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        balance = withdrawl(balance)
        
        print("="*50)
        print(f"Your Total Balance is : {balance}")
        print("="*50)
    elif choice == '2':
        balance = deposit(balance)
        print("="*50)
        print(f"Your Total Balance is : {balance}")
        print("="*50)
    elif choice == '3':
        show_balance(balance)
        print("="*50)
        print(f"Your Total Balance is : {balance}")
        print("="*50)
    elif choice == '4':
        print("="*50)
        print("Thank you for using the Banking System. Goodbye!")
        print("="*50)
        break
    else:
        print("Wrong input, please read instruction again")
      
