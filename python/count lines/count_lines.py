def count_lines(file_path:str) -> int:
    file = open(file_path)
    lines = file.readlines()

    return len(lines)

def main():
    path = 'file.txt'
    count = count_lines(path)

    print(f'The number of lines in the files are: {count}')

main()    