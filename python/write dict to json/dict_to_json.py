import json

def write_json_file(path):

    my_dict:dict = {
        "name" :"walon",
        "age" : 24,
        "address":"FBC"
    }
   
    file = open(path, 'w')
    json.dump(my_dict, file, indent=3)
    file.close()

    print("File has being written")

def main():
    path = 'file.json'
    write_json_file(path)


if __name__ == "__main__":
    main()