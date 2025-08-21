def count_word(file_path:str) -> int:
    file = open(file_path)
    content = file.read()
    words = content.split()
    file.close()

    return len(words)

def main():
    path = "file.txt"

    words = count_word(path)
    print(f'The word count is: {words}')

main()    