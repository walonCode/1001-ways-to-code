def longest_word(n:str) -> str:
    if len(n) <= 0:
        raise ValueError("invalid string")
    
    currentword = ""
    longestword = ""

    for i in n:
        if i == " ":
            if len(currentword) > len(longestword):
                longestword = currentword
            currentword = ""
        else:
            currentword += i    

    if len(currentword) > len(longestword):
        longestword = currentword    

    return longestword        


def main():
    sentence = "My name is Walon-Jalloh"

    word = longest_word(sentence)

    print(f'Longest word is: {word}')


main()