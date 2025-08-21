def isArmstrong(n:int) -> bool:
    if n <= 0:
        raise ValueError("Invalid input number")
    
    value:str = str(n)
    sum:int = 0

    for i in range(len(value)):
        sum += int(value[i]) ** len(value)


    if sum != int(value):
        return False

    return True    


def main():
    print("Welcome to Armstrong checker")

    value:int = int(input("Enter the number you want to check: "))
    answer = isArmstrong(value)

    print(f'The value {value} isArmstrong? {answer}')


if __name__ == "__main__":
    main()