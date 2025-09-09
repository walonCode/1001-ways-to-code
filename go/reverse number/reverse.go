package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func reverse(num int64)(int64, error){
	value_str := strconv.FormatInt(num,10)

	// fmt.Printf(string(value_str[1]))

	if len(value_str) <= 1{
		return num,nil
	}

	reverse_value := ""

	for i:=len(value_str) - 1; i>=0; i--{
		reverse_value += string(value_str[i])
	}


	reverse_num,err := strconv.ParseInt(reverse_value, 10, 64)
	if err != nil {
		return 0, err
	}

	return  reverse_num, nil
}


func main(){
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter a number: ")
	value,err := reader.ReadString('\n')
	value = strings.TrimSpace(value)

	if err != nil {
		fmt.Println(err)
		return
	}

	num, err := strconv.ParseInt(value,10,64)
	if err != nil {
		fmt.Println(err)
		return
	}

	reversed_value,err := reverse(num)
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Printf("The reverse of the value %v is: %v\n", num, reversed_value)
}