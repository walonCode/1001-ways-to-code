import json
import os
import time

class App:
    file_path:str 

    def __init__(self, path):
        self.file_path = path

    def create(self):
        title = input("Enter the task you want to do: ")

        content = self.load()

        id = len(content) + 1
        task = {
            "id":id,
            "title":title,
            "isCompleted":False,
            "time": time.time()
        }

        content.append(task)

        with open(self.file_path, 'w') as f:
            json.dump(content, f, indent=2)

        print('todo has being recorded ')


    def get(self):
        content = self.load()

        if not content:
            print("No todos have been added yet...")
            return

        print("-" * 72)
        print(f'| {"ID":<3} | {"Title":<20} | {"Status":<12} | {"Time":<24} |')
        print("-" * 72)

        for _, todo in enumerate(content, start=1):
            status = "Done" if todo["isCompleted"] else "Incomplete"
            print(f'| {todo["id"]:<3} | {todo["title"]:<20} | {status:<12} | {time.ctime(todo["time"]):<24} |')

        print("-" * 72)    



    def delete(self):
        value:int = int(input("Enter the id of the todo you want to delete: "))
        content = self.load()

        if not content:
            print("no todos at yet..")
            return

        if value < 1 or value > len(content):
            print("invalid id")
            return

        removed = content.pop(value - 1)

        for i, todo in enumerate(content, start=1):
            todo["id"] = i 

        with open(self.file_path, 'w') as f:
            json.dump(content, f, indent=2)

        print(f'Todo {removed["title"]} as being removed....')  



    def update(self):
        value:int = int(input("Enter the id of the todo: "))

        content = self.load()
        if not content:
            print("no todos at yet....")
            return 
        

        if value < 1 or value > len(content):
            print("invalid todo id")
            return
        
        for _, todo in enumerate(content, start=0):
            if todo["id"] == value:
                todo["isCompleted"] = True


        with open(self.file_path, 'w') as f:
            json.dump(content, f, indent=2)

        print("todo updated.........")        



    def load(self)  ->  list:
       if not os.path.exists(self.file_path):
           return []
       try:
           with open(self.file_path, 'r') as f:
               return json.load(f)
       except json.JSONDecodeError:
           return []   
          


def todo():
    app = App("file.json")
    while True:
        print('Welcome to my todo app')
        print("1.Create todo")
        print("2.Get todos")
        print("3.Delete todo")
        print("4.Update todo")
        print("5.exit the app")

        choice:int = int(input("Enter your choice: "))

        match choice:
            case 1: 
                app.create()
                continue
            case 2:
                app.get()
                continue
            case 3:
                app.delete()
                continue
            case 4:
                app.update()
                continue
            case 5:
                print("exiting the app........")
                exit(1)

def main():
    todo()


if __name__ == "__main__":
    main()