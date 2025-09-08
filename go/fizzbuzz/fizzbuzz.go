package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func fizzbuzz(value int) {
	if value <= 0 {
		log.Panic("Invalid number")
	}

	for  k := range(value + 1){
		if k % 5 == 0 && k % 3 == 0 {
			fmt.Printf("%d: fizzbuzz\n",k)
		}else if k % 5 == 0 {
			fmt.Printf("%d: fizz\n",k)
		}else if k % 3 == 0 {
			fmt.Printf("%d: buzz\n",k)
		}else {
			fmt.Printf("%d\n",k)
		}
	}
}


func main() {
	fmt.Println("Welcome to fizzbuzz")
	fmt.Print("Enter the value: ")
	reader := bufio.NewScanner(os.Stdin)
	reader.Scan()

	value := reader.Text()

	num,err := strconv.Atoi(value)
	if err != nil {
		log.Fatal(err)
	}

	fizzbuzz(num)
}