def sum(arr) -> int:
    if len(arr) <= 0:
        raise ValueError("invalid array")
    
    sum:int = 0

    for i in arr:
        sum += i

    return sum

def main():
    arr = [1,2,3,4,5]

    total = sum(arr)

    print(f'Sum of the array is: {total}')    


if __name__ == "__main__":
    main()    