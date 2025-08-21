
def main():
    file = open("file.txt", 'r')
    content = file.readline()

    words = content.split()

    count = len(words)
    print(f'Word count in the file is: {count}')

main()