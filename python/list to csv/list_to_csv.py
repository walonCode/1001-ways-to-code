import csv

def list_to_csv(file_path:str):
    data = [
    {'Name': 'David', 'Age': 40, 'City': 'Houston'},
    {'Name': 'Eve', 'Age': 22, 'City': 'Miami'},
    {'Name': 'Frank', 'Age': 50, 'City': 'Phoenix'}]

    field_name = ['Name', 'Age', 'City']

    file = open(file_path, 'w', newline='')

    writer = csv.DictWriter(file, field_name)

    writer.writeheader()

    writer.writerows(data)

    file.close()

    print('csv file has being written....')


def main():
    path = "file.csv"
    list_to_csv(path)


if __name__ == "__main__":
    main()