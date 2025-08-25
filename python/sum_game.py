def sum_of_n(n:int) -> int:
    if n <= 1:
        return
    sum:int = 0
    
    for i in range(n+1):
        sum += i

    return sum    

def main():
    print("Welcome to the sum game")
    n = int(input("Enter the value of n: "))
    sum = sum_of_n(n)

    print(f"The sum is: {sum}")

main()    