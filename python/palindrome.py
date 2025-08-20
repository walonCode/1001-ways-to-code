def palindrome(n:str) -> bool:
    if len(n) == 0:
        raise ValueError("Invalid string value")
    
    value = n[::-1]

    if n != value:
        return False
    
    return True
    

def main():
    print("Welcome to Panlindrome checker")
    
    value = input("Enter the value you want to check: ")
    answer = palindrome(value)

    print(f'The value {value} is palindrome {answer}')

if __name__ == "__main__":
    main()