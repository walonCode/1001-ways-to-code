def reverse(n:list) -> list:
    if len(n) <= 2:
        raise ValueError("invalid array")
    
    return n[::-1]

def main():
    arr = [1,2,3,4]

    reverseArr = reverse(arr)
    print(f"Reverse array is {reverseArr}")

main()    