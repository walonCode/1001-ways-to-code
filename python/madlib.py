def create_sentence(noun:str, verb:str, adjective:str) -> str:
    return f'The person was called {noun} and he was {verb} and doing it {adjective}'


def main():
    print("Welcome to madlib")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")

    sentence = create_sentence(noun, verb, adjective)

    print(sentence)


if __name__ == "__main__":
    main()