package main

import "testing"


func TestAdd(t *testing.T){
	c := Calculator{
		ValueA: 50,
		ValueB: 80,
	}

	answer,err := c.add()
	if err != nil {
		t.Errorf("unexpected err: %v",err)
	}

	if answer != 130 {
		t.Errorf("expected %v got %v", 130, answer)
	}
}

func TestSubtract(t *testing.T){
	c := Calculator{
		ValueA: 50,
		ValueB: 80,
	}

	answer,err := c.subract()
	if err != nil {
		t.Errorf("unexpected err: %v",err)
	}

	if answer != -30{
		t.Errorf("expected %v got %v", 130, answer)
	}
}

func TestMultiply(t *testing.T){
	c := Calculator{
		ValueA: 50,
		ValueB: 80,
	}

	answer,err := c.multiply()
	if err != nil {
		t.Errorf("unexpected err: %v",err)
	}

	if answer != 4000 {
		t.Errorf("expected %v got %v", 130, answer)
	}
}

func TestDivide(t *testing.T){
	c := Calculator{
		ValueA: 50,
		ValueB: 10,
	}

	answer,err := c.division()
	if err != nil {
		t.Errorf("unexpected err: %v",err)
	}

	if answer != 5 {
		t.Errorf("expected %v got %v", 130, answer)
	}
}