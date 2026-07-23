class BankAccount():
    def __init__(self, balance:float = 0):
        self.balance = balance

    def deposit_money(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}. New balance: ${self.balance}\n")

    def withdraw_money(self, amount):
        self.balance -= amount
        print(f"Withdrew: ${amount}. New balance: ${self.balance}\n")

class SavingsAccount(BankAccount):
    def __init__(self,balance, min_balance:float = 0):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw_savings(self, amount):
        if (self.balance - amount) < self.min_balance:
            print(f"\n[ERROR] Cannot withdraw ${amount}")
            print(f"Your current balance is ${self.balance}, and the minimum allowed is ${self.min_balance}\n")
        else:
            self.withdraw_money(amount)


if __name__=="__main__":
    print("===============Bank Account System===============")
    print("=================================================\n")
    new_account = SavingsAccount(balance = 100, min_balance = 20)
    while True:
        choice = input("Do you want to Deposit (d), Withdraw (w), Check Balance (b) or Exit (e): ").lower()

        if choice == "e":
            print("Thanks for using the Bank System, GoodBye\n")
            break
        elif choice == "w":
            withdraw = float(input("Enter the Amount you want to Withdraw: "))
            new_account.withdraw_savings(withdraw)
        elif choice == "d":
            deposit = float(input("Enter the Amount of your Deposit: "))
            new_account.deposit_money(deposit)
        elif choice == "b":
            print(f"Current Balance: ${new_account.balance}\n")
        else:
            print("Invalid Option. Try Again")