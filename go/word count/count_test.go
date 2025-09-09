package main

import "testing"

func TestCount(t *testing.T){
	var test = []struct{
		input string
		expected int
	}{
		{
			input: "Walon is crazy",
			expected: 3,
		},
		{
			input: "Walon is great and calm",
			expected: 5,
		},
	}

	for _, tt := range test {
		count, err := count(tt.input)
		if err != nil {
			t.Errorf("unexpected error: %v\n",err)
		}

		if count != tt.expected {
			t.Errorf("expected %v got %v\n", tt.expected, count)
		}
	}
}