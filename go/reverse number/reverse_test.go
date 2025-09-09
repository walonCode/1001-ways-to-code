package main

import "testing"

func TestReverse(t *testing.T){
	var test = []struct{
		value int64
		required int64
	}{
		{
			value: 40,
			required: 04,
		},
		{
			value: 100,
			required: 001,
		},
		{
			value: 4000,
			required: 00004,
		},
	}

	for _,tt := range test {
		value, err := reverse(tt.value)
		if err != nil {
			t.Errorf("unexpected error: %v\n",err)
		}

		if value != tt.required {
			t.Errorf("required %v but go %v\n", tt.required, value)
		}
	}
}