def average(arr) -> int:
    if len(arr) <= 0:
        raise ValueError("invalid array")
    
    sum:int = 0

    for i in arr:
        sum += i

    average = sum / len(arr)

    return average


def main():
    arr = [1,2,3,4]

    arrAverage = average(arr)

    print(f'Average of the arr is: {arrAverage}')


if __name__ == "__main__":
    main()