def shortest_word(file_path:str) -> str:
    file = open(file_path, 'r')
    lines = file.read()

    words = lines.split()

    for i in range(len(words)):
        for j in range(len(words) - 1 - i):
            if len(words[j]) > len(words[j + 1]):
                words[j], words[j + 1] = words[j + 1], words[j]

    file.close()
    return words[0]

def main():
    path = "file.txt"

    word = shortest_word(path)

    print(f'Shortest word is: {word}')


main()
            