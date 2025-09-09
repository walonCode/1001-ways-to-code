package main

import "testing"

func TestSort(t *testing.T){
	var test = []struct {
		value []int
		expected []int
	}{
		{
			value: []int{5,4,3,2,1},
			expected: []int{1,2,3,4,5},
		},
		{
			value: []int{9,8,7,6,5},
			expected: []int{5,6,7,8,9},
		},
	}

	for _, tt := range test {
		value,err := sort(tt.value)
		if err != nil {
			t.Errorf("unexpected error: %v\n",err)
		}

		for i := range value {
			if value[i] != tt.expected[i]{
				t.Errorf("expected %v got %v\n", tt.expected[i], value[i])
			}
		}
	}
}