def sort(arr) -> list:
    if len(arr) <= 0:
        raise ValueError("Invalid array")
    
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j],arr[j +1] = arr[j +1],arr[j]

    return arr


def main():
    myArray = [1,5,7,4,2,4,3,1,8]

    sortedArray = sort(myArray)

    print(f"Sorted array: {sortedArray}")


if __name__ == "__main__":
    main()