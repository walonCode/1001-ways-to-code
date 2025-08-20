def factorical(n:int) -> int :
    if n == 1 or n == 0:
        return n
    return n * factorical(n -1)


def main():
    print("Welcome to the factorial calculator")
    value = int(input("Enter the value you want the factorial for: "))

    answer = factorical(value)

    print(f'The answer for the factorial of {value} is: {answer}')



if __name__ == "__main__":
    main()

    