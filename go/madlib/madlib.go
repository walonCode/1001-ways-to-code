package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main(){
	fmt.Print("Enter a noun,verb and adjective: ")
	reader := bufio.NewReader(os.Stdin)
	words, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}

	words = strings.TrimSpace(words)
	word_list := strings.Split(words, ",")

	if len(word_list) != 3 {
		log.Fatal("words should be 3 in number")
	}

	fmt.Printf("The %s was doing %s and that person was doing it %s\n", word_list[0], word_list[1], word_list[2])
}