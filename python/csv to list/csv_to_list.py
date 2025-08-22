import csv

#the csv reader function return an iterator which u need to for loop through to see the values in it
# the csv dictreader work is a dictionary kind of way making it easier to pass the csv file

def read_csv_file(file_path:str) -> list:
    file = open(file_path, 'r')

    # content = csv.reader(file)
    # file.close

    # # header = next(content)

    # for rows in content:
    #     print(rows)

    content = csv.DictReader(file)
    # file.close()

    for rows in content:
        print(f"Rows: {rows}")
        print(f'Name: {rows['Name']}, Age: {rows['Age']} City: {rows['City']}')

    file.close()    

def main():
    path = "employee.csv"
    read_csv_file(path)

main()