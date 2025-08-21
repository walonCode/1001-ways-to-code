def longest_line(file_path:str) -> str:
    file = open(file_path, 'r')
    contents = file.readlines()
    # print(contents)
    
    for i in range(len(contents)):
        for j in range(len(contents) - 1 - i):
            if len(contents[j]) > len(contents[j + 1]):
                contents[j],contents[j + 1] = contents[j + 1],contents[j]

    return contents[-1]

def main():
    path = "file.txt"
    line = longest_line(path)

    print(f'Longest line is: {line}')


if __name__ == "__main__":
    main()