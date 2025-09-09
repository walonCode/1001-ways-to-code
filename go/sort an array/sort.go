package main

import (
	"fmt"
	"log"
)


func sort(arr []int)([]int, error){
	if len(arr) <= 1 {
		return arr,nil
	}

	for i := range len(arr) {
		for j  := range len(arr) - 1 - i {
			if arr[j]  > arr[j +1]{
				arr[j],arr[j + 1] = arr[j +1],arr[j]
			}
		}
	}
	
	return arr,nil
}


func main(){
	arr := []int{2,1,3,2,7,6,4,20,29,20,12}

	sorted,err := sort(arr)

	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("Sorted array is: %v\n", sorted)
}