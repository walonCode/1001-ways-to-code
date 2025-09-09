package main

import (
	"fmt"
	"strings"
)

func longest_word(sentence string)string {
	word_list := strings.Split(sentence, " ")

	first_word := string(word_list[0])

	longest_word := ""

	for _, value := range word_list{
		if len(value) > len(first_word) {
			longest_word = string(value)
		}
	}

	return longest_word
}

func main(){
	sentence := "Walon is crazy and something else"
	longest_word := longest_word(sentence)

	fmt.Printf("Longest word is %s\n",longest_word)
}