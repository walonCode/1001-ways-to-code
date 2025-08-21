def sum_of_even(n:list) -> int:
    if len(n) <= 2:
        raise ValueError("invalid array")
    sum = 0
    for i in n:
        if i % 2 == 0:
            sum += i

    return sum


def main():
    arr = [1,2,3,4,5,6]

    sum = sum_of_even(arr)
    print(f'The sum of the odd number is: {sum}')


main()