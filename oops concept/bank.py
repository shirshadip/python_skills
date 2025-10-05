class bankaccount :
    def __init__(self, balance: float) -> None:
        self.__balance = balance
    

    def deposit(self, amount: float) -> None:
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount

    def getbalance (self) -> float:
        return self.__balance
#creating objects

acc = bankaccount(1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.getbalance())
