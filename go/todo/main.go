package main

import (
	"bufio"
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type todo struct {
	ID          int    `json:"id"`
	Name        string `json:"name"`
	IsCompleted bool   `json:"is_completed"`
}

var (
	fileName = "todo.json"
	Todos    = []todo{}
)

func add() error {
	fmt.Printf("Enter the name of the todo: ")
	reader := bufio.NewScanner(os.Stdin)
	reader.Scan()
	name := strings.TrimSpace(reader.Text())

	if name == "" {
		return errors.New("invalid name")
	}

	todos, err := get()
	if err != nil {
		if os.IsNotExist(err) {
			todos = []todo{}
		} else {
			return err
		}
	}

	id := len(todos) + 1

	newTodo := todo{
		ID:          id,
		Name:        name,
		IsCompleted: false,
	}

	todos = append(todos, newTodo)
	Todos = todos
	return save()
}

func save() error {
	data, err := json.MarshalIndent(Todos, "", "  ")
	if err != nil {
		return err
	}

	err = os.WriteFile(fileName, data, 0644)
	return err
}

func get() ([]todo, error) {
	_, err := os.Stat(fileName)
	if err != nil {
		return nil, err
	}

	file, err := os.ReadFile(fileName)
	if err != nil {
		return nil, err
	}

	if len(file) == 0 {
		return []todo{}, nil
	}

	var todos []todo
	err = json.Unmarshal(file, &todos)
	return todos, err
}

func update(id int) error {
	if id < 1 || id > len(Todos) {
		return errors.New("invalid ID")
	}

	for i := range Todos {
		if Todos[i].ID == id {
			Todos[i].IsCompleted = true
			return save()
		}
	}
	return errors.New("todo not found")
}

func deleteTodo(id int) error {
	if id < 1 || id > len(Todos) {
		return errors.New("invalid ID")
	}

	var newTodos []todo
	for _, t := range Todos {
		if t.ID != id {
			newTodos = append(newTodos, t)
		}
	}

	Todos = newTodos
	return save()
}

func printTodos() {
	if len(Todos) == 0 {
		fmt.Println("No todos yet...")
		return
	}

	fmt.Printf("\n%-5s | %-30s | %-10s |\n", "ID", "Name", "Completed")
	fmt.Println(strings.Repeat("-", 55))
	for _, t := range Todos {
		fmt.Printf("%-5d | %-30s | %-10t |\n", t.ID, t.Name, t.IsCompleted)
	}
	fmt.Println()
}

func main() {
	var err error
	Todos, err = get()
	if err != nil && !os.IsNotExist(err) {
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(os.Stdin)

	for {
		fmt.Println("Welcome to Todo App")
		fmt.Println("1. Get Todo")
		fmt.Println("2. Add Todo")
		fmt.Println("3. Delete Todo")
		fmt.Println("4. Update Todo")
		fmt.Println("5. Exit App")

		fmt.Print("Enter your choice: ")
		scanner.Scan()
		choice, err := strconv.Atoi(scanner.Text())
		if err != nil {
			fmt.Println("Invalid input, try again.")
			continue
		}

		switch choice {
		case 1:
			Todos, _ = get()
			printTodos()
		case 2:
			if err := add(); err != nil {
				fmt.Println("Error adding todo:", err)
			}
		case 3:
			fmt.Print("Enter the ID of the todo to delete: ")
			scanner.Scan()
			id, err := strconv.Atoi(scanner.Text())
			if err != nil {
				fmt.Println("Invalid ID")
				continue
			}
			if err := deleteTodo(id); err != nil {
				fmt.Println("Error deleting todo:", err)
			}
		case 4:
			fmt.Print("Enter the ID of the todo to mark completed: ")
			scanner.Scan()
			id, err := strconv.Atoi(scanner.Text())
			if err != nil {
				fmt.Println("Invalid ID")
				continue
			}
			if err := update(id); err != nil {
				fmt.Println("Error updating todo:", err)
			}
		case 5:
			fmt.Println("Exiting...")
			os.Exit(0)
		default:
			fmt.Println("Invalid choice.")
		}
	}
}
