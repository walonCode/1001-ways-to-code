def max_of_3_value(n:int) -> int:
    if n <= 0:
        raise ValueError("invalid input value")
    
    value:str = str(n)
    if len(value) < 2:
        raise ValueError("invalid number length")
    
    sortedArr = [int(d) for d in value]

    for i in range(len(sortedArr)):
        for j in range(1, len(sortedArr) - 1 - i):
            if sortedArr[j] > sortedArr[j + 1]:
                sortedArr[j + 1],sortedArr[j] = sortedArr[j],sortedArr[j+1]
    print(sortedArr)
    return sortedArr[-1]


def main():
    print("Maximun number finder of three values")
    value:int = int(input("Enter the value you want to find the max of: "))
    answer = max_of_3_value(value)

    print(f"The max of the value {value} is: {answer}")


if __name__ == "__main__":
    main()