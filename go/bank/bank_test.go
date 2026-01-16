package main

import "testing"

func TestAdd(t *testing.T){
	newBank := bank{
		balance: 400.0,
	}
	
	var test = []struct{
	 	value float64
		expected bool
	}{
		{
			value:50.0,
			expected: true,
		},
		{
			value:0,
			expected:false,
		},
	}
	
	for _, tt := range test {
		ok := newBank.add(tt.value)
		if ok != tt.expected{
			t.Errorf("expected %v go %v", tt.expected, ok)
		}
	}
}

