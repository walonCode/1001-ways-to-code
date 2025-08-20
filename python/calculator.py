class Calculator:

    def add():
        print("Welcome to the addition function")
        value1 = int(input("Enter the first value: "))
        value2 = int(input("Enter the second value: "))

        sum = value1 + value2

        print(f'Sum of the values {value1, value2} is {sum}')

    def minus():
        print("Welcome to the minus function")
        value1 = int(input("Enter the first value: "))
        value2 = int(input("Enter the second value: "))    

        minus = value1 - value2

        print(f'Minus for the value {value1, value2} is {minus}')

    def divide():
        print("Welcome to the divide function")
        value1 = int(input("Enter the first value: "))
        value2 = int(input("Enter the second value: ")) 

        divide = value1 / value2

        print(f'Division for value {value1, value2} is: {divide}')   

    def multiply():
        print("Welcome to the divide function")
        value1 = int(input("Enter the first value: "))
        value2 = int(input("Enter the second value: ")) 

        multiply = value1 * value2

        print(f'The Multiplication of value {value1, value2} is {multiply}')

def calculator():
    calculator = Calculator
    while True:
        print('-------------------------------------------------------')
        print('-------------------Calculator World--------------------')
        print('-------------------------------------------------------')
        print()
        print("1.Add")
        print("2.Minus")
        print("3.Division")
        print("4.Multiply")
        print('5.exit')
        
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                calculator.add()
                continue
            case 2:
                calculator.minus()
                continue
            case 3:
                calculator.divide()
                continue
            case 4: 
                calculator.multiply()
                continue
            case 5:
                print("exiting the calculator............")
                exit(1)
            case _:
                print("Enter a valid choice")
                continue    



def main():
    calculator()


if __name__ == "__main__":
    main()