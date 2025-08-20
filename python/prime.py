def isPrime(n: int) -> bool:
    if n <= 1:
        raise ValueError("Input must be greater than 1")

    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True



def main():
    print("Welcome to prime checker")
    try:
        value: int = int(input("Enter the value to be checked: "))
        answer = isPrime(value)
        print(f'The value {value} is a prime?: {answer}')
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()