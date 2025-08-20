def addDigit(n:int) -> int:
    #this function first convert the value to string nd later back to int
    if n <= 0:
        raise ValueError("Invalid value of n")
    
    value:str = str(n)

    sum:int = 0
    for i in value:
        sum += int(i)
    return sum


def addDigitNumber(n:int) -> int:
    if n <= 0:
        raise ValueError("invalid input value")
    sum:int = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n //= 10
    return sum    

def main():
    print("Welcome to add digit")
    value:int = int(input("Enter the digit to be add: "))

    answer = addDigitNumber(value)

    print(f'{10 // 10}')
    

    print(f'The answer for the value {value} is {answer}')


if __name__ == "__main__":
    main()