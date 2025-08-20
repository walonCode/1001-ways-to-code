def fibo(n:int) -> int:
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)


def main():
    print("Welcome to the world of fibonacci")
    value:int = int(input("Enter the number you want to find the fibonacci for: "))
    
    answer = fibo(value)
    print(f'Fibo for the {value} is: {answer}')

if __name__ == "__main__":
    main()    