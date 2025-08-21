
with open('file.txt', 'a') as file:
    file.write("\nHello this is awesome\n")
    file.write("\nthis is great\n")
    file.close()


with open('file.txt', 'r') as file:
    content = file.read()
    print(content)
    file.close()