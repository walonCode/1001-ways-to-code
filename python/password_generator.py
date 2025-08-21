import random

def password_gen(n:int) -> str:
    letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    number = list("1234567890")
    symbols = ['@',',','.','\\','/','$',"#",'!']

    allChar = letter + number + symbols

    password = "".join(random.choice(allChar) for _ in range(n))

    return password 
   

def main():
    print("Welcome to password generator")
    length = int(input("Enter the length of the password: "))
    password = password_gen(length)

    print(password)

if __name__ == "__main__":
    main()