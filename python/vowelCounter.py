def vowelCounter(n:str) -> int:
    if len(n) == 0:
        raise ValueError("invalid input error")
    
    value = n.lower()
    vowel = ['a', 'e', 'i', 'o', 'u']
    count:int = 0

    for i in value:
        if i in vowel:
            count += 1

    return count




def main():
    print("Welcome to vowel counter")
    value = input("Enter the value to be check: ")

    answer = vowelCounter(value)

    print(f'The numeber of vowels in the word {value} is {answer}')


if __name__ == "__main__":
    main()