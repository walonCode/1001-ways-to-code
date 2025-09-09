package main

import "fmt"

func sumOfEven(arr []int)(int,error){
	if len(arr) <= 1 {
		return arr[0], nil
	}

	sum := 0

	for _, value := range arr {
		if value % 2 == 0 {
			sum += value
		}
	}

	return sum, nil
}

func main(){
	arr := []int{1,2,3,4,5,6}
	sum,err := sumOfEven(arr)

	if err != nil{
		fmt.Println(err)
		return
	}

	fmt.Printf("The sum of even number is: %v\n", sum)
}