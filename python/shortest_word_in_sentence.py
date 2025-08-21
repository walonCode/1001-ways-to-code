def shortest_word(n:str) -> str:
    if len(n) <= 0:
        raise ValueError("invalid string")
    
    words = n.split()

    for i in range(len(words)):
        for j in range(len(words) - 1 - i):
            if len(words[j]) > len(words[j + 1]):
                words[j], words[j + 1] = words[j + 1],words[j]

    return words[0]           


def main():
    sentence = "Hello Walon is a great guy"

    word = shortest_word(sentence)
    print(f'Shortest word is {word}')


main()