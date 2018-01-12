class Account():
    def __init__(self, filePath):
        self.filePath = filePath
        with open(filePath,'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def commit(self):
        with open(self.filePath,'w') as file:
            file.write(str(self.balance))

# Checking inherits Account
# class CHILD_CLASS(PARENT_CLASS)
class Checking(Account):
    """ This extends Account class """

    bank_name = "Shinhan"

    def __init__(self, filePath, fee):
        Account.__init__(self,filePath)
        self.fee = fee

    def transfer(self, amount):
        self.balance -= (amount + self.fee)
        print(self.bank_name)

if __name__=="__main__":
    filePath = "balance.txt"
    acc = Account(filePath)
    acc.withdraw(100)
    acc.deposit(200)

    checking = Checking("balance.txt",1)
    checking.deposit(10)
    checking.transfer(20)
    print(checking.balance)
    checking.commit()
    print(checking.bank_name)
