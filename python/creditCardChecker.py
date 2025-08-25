def check_card(value:int) -> bool:
    value_str:str = str(value)
    if len(value_str) < 16:
        raise ValueError("invalid card number") 
    
    total:int = 0

    reverse_str = value_str[::-1]

    for i, digit in enumerate(reverse_str, start=0):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n    


    print(f"sum is: {total}")  

    return total % 10 == 0   
        


def main():
    print("Welcome to Credit card checker")
    value = int(input("Enter the number of the card: "))
    answer = check_card(value)

    print(f"The card is valid?: {answer}")

main()    