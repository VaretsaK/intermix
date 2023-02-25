from datetime import datetime

accounts = []


def sign_in():
    name = input("Enter name: ")
    balance = int(input("Enter balance: "))
    password = input("Enter password: ")
    num = len(accounts) + 1
    account = {
        "name": name,
        "balance": balance,
        "account_num": num,
        "transactions": [],
        "password": password
    }
    accounts.append(account)
    print(f"Your account number is {num}")


def get_our_account(acc_num, acc_password):
    for acc in accounts:
        if acc["account_num"] == acc_num and acc["password"] == acc_password:
            return acc
    print("You've entered invalid account's number or password, please, try again!")
    return


def deposit(acc, dep):
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    acc["balance"] += dep
    acc["transactions"].append({"type": "Deposit", "amount": dep, "time": date_time})


def withdraw(acc, wth):
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    if wth > acc["balance"]:
        print("You don't have enough money!")
        return
    acc["balance"] -= wth
    acc["transactions"].append({"type": "Withdraw", "amount": wth, "time": date_time})


def transactions(acc):
    counter = 0
    for trans in acc["transactions"]:
        counter += 1
        print(f"{counter}.{trans['time']} {trans['type']} of {trans['amount']} USD")


def operations():
    print("Enter the type of operation: ")
    print("1 if you want to Withdraw")
    print("2 if you want to Deposit")
    print("3 if you want to see Transactions")
    print("4 if you want to check the current Balance")
    print("Q if you want to Log Out")
    option = input(">>>  ")
    return option


def menu():
    print("\nEnter the type of operation: ")
    print("1 if you want to Sign In")
    print("2 if you want to Log In")
    print("Q if you want to Quit")
    option = input(">>>  ")
    return option


if __name__ == "__main__":
    while True:
        choice_1 = menu()
        if choice_1 == "1":
            sign_in()
        elif choice_1 == "2":
            while True:
                account_num = int(input("Enter account number: "))
                acc_pass = input("Enter your password: ")
                current_account = get_our_account(account_num, acc_pass)
                if current_account:
                    break
            while True:
                print(f"\nGreetings, {current_account['name']}!")
                choice_2 = operations()
                if choice_2 == "1":
                    how_much_withdraw = int(input("How much do you want to withdraw?: "))
                    withdraw(current_account, how_much_withdraw)
                elif choice_2 == "2":
                    depo = int(input("How much do you want to deposit?: "))
                    deposit(current_account, depo)
                elif choice_2 == "3":
                    transactions(current_account)
                elif choice_2 == "4":
                    print(f'You keep here {current_account["balance"]} USD')
                elif choice_2 == "Q":
                    break
        elif choice_1 == "Q":
            break
