def count_word(n:str) -> int:
    if len(n) <= 0:
        raise ValueError("Invalid input string")
    
    word = n.split()
    count = len(word)  
    
    return count    


def main():
    sentence = "My name is Walon-Jalloh"

    count = count_word(sentence)

    print(f'Word count in the sentence is {count}')

main()