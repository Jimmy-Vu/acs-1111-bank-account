import random

class BankAccount:
    def __init__(self, full_name, account_number):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${amount} new balance: ${self.balance:.2f}")
        print("-----------------------")

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= 10  # charge overdraft fee
            print("Insufficent funds.")
            print("-----------------------")
        else:
            self.balance -= amount
            print(f"Amount withdrawn: ${amount} new balance: ${self.balance:.2f}")
            print("-----------------------")


    def get_balance(self):
        print(f"The current balance of the account is ${self.balance:.2f}")
        print("-----------------------")
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest

    def print_statement(self):
        print(f"{self.full_name}\nAccount No.: ****{self.account_number[-4:]}\nBalance: ${self.balance:.2f}")
        print("-----------------------")


def random_account_number_generator():
    # TODO: Need to make sure it's unique
    # converting to string to keep things consistent because of the Mitchell account number leading zero issue below
    return str(random.randint(10000000, 99999999))


james_account = BankAccount("James Smith", random_account_number_generator())
bob_account = BankAccount("Bob Anderson", random_account_number_generator())
mitchell_account = BankAccount("Mitchell", "03141592") # python won't allow ints with leading zeros

# Mitchell Demo
print("Mitchell Demo")
mitchell_account.deposit(400000)
mitchell_account.print_statement()
mitchell_account.add_interest()
mitchell_account.print_statement()
mitchell_account.withdraw(150)
mitchell_account.print_statement()

# James Demo
print("James Demo")
james_account.deposit(500)
james_account.print_statement()
james_account.add_interest()
james_account.print_statement()
james_account.withdraw(600)
james_account.print_statement()

# Bob Demo
print("Bob Demo")
bob_account.deposit(1200)
bob_account.print_statement()
bob_account.add_interest()
bob_account.print_statement()
bob_account.withdraw(500)
bob_account.print_statement()
