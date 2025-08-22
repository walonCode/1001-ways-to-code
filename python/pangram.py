def is_pangram(n:str) -> bool:
    if len(n) <= 5:
        raise ValueError("Invalid input string")
    
    # set in python only hold unqiue value and has many function
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    n = set(n.lower())
    
    for ch in alphabet:
        if ch not in n:
            return False
  
    return True


def main():
    sentence = "the quick brown fox jumps over the lazy dog"

    isPangram = is_pangram(sentence)

    print(f"The sentence is: {isPangram}")


if __name__ == "__main__":
    main()