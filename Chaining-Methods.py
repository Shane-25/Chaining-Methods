# This is called chaining. In order for this to work, each method must return self. By returning self, if we recall how functions work, each method call will now be equal to the instance that called it.

# For example if bob.make_deposit(100) returns its own instance (bob), then we can call one of that instance's methods after that call, like bob.make_deposit(100).make_withdrawal(50).

# The practice of having OOP return its own instance is pretty common and is done in other programming languages, though the variable name in some languages is not self, but instead this.

# Update your previous assignment so that each instance's methods are chained

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

    def display_user_balance(self):
        print(f'User: {self.name}, Balance: {self.account_balance}')
        return self

jonny = User("Jonny be Good", "jonny@codingdojo.com")
python = User("Python Monster", "python@codingdojo.com")
boaty = User("Boaty McBoatface", "boaty@codingdojo.com")

jonny.make_deposit(100).make_deposit(500).make_deposit(3000).make_withdrawal(200).display_user_balance()

python.make_deposit(100).make_deposit(800).make_withdrawal(100).make_withdrawal(50).display_user_balance()

boaty.make_deposit(2000).make_withdrawal(100).make_withdrawal(300).make_withdrawal(10).display_user_balance()

jonny.transfer_money(boaty,200).display_user_balance()
boaty.display_user_balance()