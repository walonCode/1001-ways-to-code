def reverse_number(n:int) -> int:
    if n <= 0 :
        raise ValueError("invalid number")
    
    value:str = str(n)

    return value[::-1]


def main():
    n = 123

    answer = reverse_number(n)

    print(f'The reverse of the number is: {answer}')


if __name__ == "__main__":
    main()