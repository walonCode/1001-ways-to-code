def roman_to_int(value:str) -> int:
    if len(value) <= 0:
        return ValueError("invalid input value")
    
    value = value.upper()

    roman = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "L":500,
        "M":1000
    }

    prev = 0
    total = 0

    for c in reversed(value):
        value = roman[c]
        if value < prev:
            total -= value
        else:
            total += value
        prev = total 
    return total  
          

def main():
    print("Welcome to Roman to integers converter")

    value:str = input("Enter the roman you to convert: ")
    answer = roman_to_int(value)

    print(f'The integer is: {answer}')


if __name__ == "__main__":
    main()