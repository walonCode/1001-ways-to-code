from random import randint

def game():
    words = ['man', "go", "app", 'favor', 'nyash', "hello", "python", 'walon', 'jalloh', 'alpha','snake', "rust",'sql','name'] 
    user_turn = 7
    score = 0

    while user_turn > 0:
        dice = randint(0, len(words)-1)
        word_to_guess = words[dice]
        user_guess = input("Enter your guess: ")
        if len(user_guess) <= 0:
            break

        if user_guess == word_to_guess:
            print("Correct guess..")
            score += 1
            break
        else:
            print("Wrong guess...")
            user_turn -=1
            continue

    print(f'User score is: {score}')        

def main():
    print("*" * 72)
    print("Welcome to the guess word the game".center(72))
    print("*" * 72) 

    game()
    print()
    print("*" * 72)


main()