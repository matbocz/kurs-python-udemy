class Account:
    def __init__(self, filepath):
        self.filepath = filepath

        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    """This class generates checking account objects."""

    type = "checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)

        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


checking = Checking("balance.txt", 10)
print(checking.balance)

checking.deposit(500)
print(checking.balance)

checking.transfer(200)
print(checking.balance)

print(checking.type)

checking.commit()
