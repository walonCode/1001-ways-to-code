class Bank:
    Balance:int = 0
    
    #constructor
    def __init__(self,balance):
        self.Balance = balance


    #method
    def getBalance(self):
        print(f'Account balance is: {self.Balance}')  

    def Deposit(self):
        value:int = int(input("Enter the amount to be deposited: "))
        if value <= 0:
           raise ValueError("Invalid amount")

        self.Balance += value
        print(f'Amount {value} has being deposited')

    def withdraw(self):
        value:int = int(input("Enter the amount to be withdraw: "))

        if value > self.Balance:
            raise ValueError(f"This amount {value} cannot be withdrawn")

        self.Balance -= value
        print(f'The amount {value} has being withdraw')    


def bank():
    person = Bank(400)
    while True:
        print('--------------------------------------------------------')
        print("              Welcome to Walon Bank                     ")
        print('--------------------------------------------------------')
        print("Choice from the following")
        print("1. get balance")
        print("2. deposited in to the account")
        print("3. withdraw from the account")
        print("4. exit the app")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                person.getBalance()
                continue
            case 2:
                person.Deposit()
                continue
            case 3:
                person.withdraw()
                continue
            case 4:
                print('Exiting the app.............')
                exit(1)
                break
            case _:
                print("please pick a valid choice")
        
        


def main():
    bank()

if __name__ == "__main__":
    main()