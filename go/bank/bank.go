package main

import (
	"fmt"
	"log"
)

type bank struct {
	balance float64
}

//method on the bank

//add amount 
func(b *bank) add(amount float64)(bool){
	if(amount <= 0){
		return  false
	}
	
	b.balance  = b.balance + amount
	
	return true
}

//get balance 
func(b *bank)getBalance()(float64){
	return b.balance
}

func main(){
	bank := bank{
		balance: 300.69,
	}
	
	if ok := bank.add(400.0); !ok {
		log.Fatal("failed to amount")
	}
	
	fmt.Println("Money added");
	
	fmt.Println(bank.getBalance())
}