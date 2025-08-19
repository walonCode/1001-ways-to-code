def fizzbuzz(n:int):
    if n < 1:
        return
    
    for i in range(n+1):
        if i % 5 == 0 and i % 3 == 0 :
            print(f'{i}: FizzBuzz')
        elif i % 5 == 0 :
            print(f'{i}: Buzz')
        elif i % 3 == 0:
            print(f'{i}: Fizz')
        else:
            print(f'{i}')            

def main():
    print("Welcome to FizzBuzz")
    value:int = int(input("Enter a number: "))

    if value <= 0:
        return
    
    fizzbuzz(value)


if __name__ == "__main__":
    main()