package main

import "fmt"

func fact(n int)int{
	if n == 1 || n == 0 {
		return n
	}

	return n * fact(n - 1)
}

func main(){
	num := fact(20)

	fmt.Printf("Factorial of 20 is: %v \n",num)
}