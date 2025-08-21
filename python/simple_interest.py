def simpleInterest(amount:int, rate:float, year:int) -> int:
    if amount == 0 or rate == 0 or year == 0 :
        raise ValueError("Invalid amount,interest or year")
    
    interest = (amount * rate * year) / 100

    return interest



def main():
    print("Welcome to my simple interest calculator")
    amount = int(input("Enter the amount: "))
    rate = float(input("Enter the rate: "))
    year = int(input("Enter the amount of year: "))

    interest = simpleInterest(amount, rate, year)

    print(f"The simple interest is: {interest}")

if __name__ == "__main__":
    main()    