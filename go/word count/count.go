package main

import (
	"fmt"
	"log"
	"strings"
)


func count(sentence string)(int, error){
	word := strings.Split(sentence, " ")

	// fmt.Println(word)

	return len(word),nil
}

func main(){
	sentence := "Hello my name is walon"	
	count,err := count(sentence)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("The word count in the sentence \" %s\" is: %v\n",sentence, count)
}