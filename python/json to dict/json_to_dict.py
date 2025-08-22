import json

def json_to_dict(file_path:str) -> dict:
    file = open(file_path, 'r')
    content = json.load(file)

    return content


def main():
    path = "db.json"

    my_dict = json_to_dict(path)
    print(f'Json to dict: {my_dict}')


if __name__ == "__main__":
    main()