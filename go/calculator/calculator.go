package main

import (
	"errors"
	"fmt"
)

type Calculator struct {
	ValueA float64
	ValueB float64
}

func (c *Calculator)add()(float64,error){
	if c.ValueA == 0 || c.ValueB == 0 {
		return 0, errors.New("invalid values of A or B")
	}

	return c.ValueA + c.ValueB, nil
}

func (c *Calculator)subract()(float64,error){
	if c.ValueA == 0 || c.ValueB == 0 {
		return 0, errors.New("invalid values of A or B")
	}

	return c.ValueA - c.ValueB, nil
}

func (c *Calculator)multiply()(float64,error){
	if c.ValueA == 0 || c.ValueB == 0 {
		return 0, errors.New("invalid values of A or B")
	}

	return c.ValueA * c.ValueB, nil
}

func (c *Calculator)division()(float64,error){
	if c.ValueA == 0 || c.ValueB == 0 {
		return 0, errors.New("invalid values of A or B")
	}

	return c.ValueA / c.ValueB, nil
}

func main(){

	cal := Calculator{
		ValueA: 35,
		ValueB: 40,
	}

	answer,err := cal.add()
	if err != nil {
		fmt.Println(err)
	}

	fmt.Println("hello")
	fmt.Println(answer)
}