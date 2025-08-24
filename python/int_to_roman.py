def int_to_roman(value: int) -> str:
    if not isinstance(value, int) or value <= 0:
        raise ValueError("Invalid input value (must be positive integer)")

    roman_map = [
        (1000, "M"),
        (900,  "CM"),
        (500,  "D"),
        (400,  "CD"),
        (100,  "C"),
        (90,   "XC"),
        (50,   "L"),
        (40,   "XL"),
        (10,   "X"),
        (9,    "IX"),
        (5,    "V"),
        (4,    "IV"),
        (1,    "I")
    ]

    result = ""
    for num, symbol in roman_map:
        while value >= num:
            result += symbol
            value -= num

    return result
            

def main():
    print("Welcome to int to roman converter")

    value:int = int(input("Enter the interger to be converted: "))
    answer = int_to_roman(value)

    print(f'The roman value is: {answer}')


if __name__ == "__main__":
    main()