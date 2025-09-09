package main

import "fmt"

func isPanlindrome(word string)bool{
	reverse_word := ""

	for i:=len(word)-1;i >= 0; i-- {
		reverse_word += string(word[i])
	}

	if reverse_word != word {
		return false
	}

	return true
}

func main(){
	word := "racecar"

	check := isPanlindrome(word)

	fmt.Printf("The word %s isPalindrome: %v\n",word, check)
}