package main


import "testing"

func TestSumOfOdd(t *testing.T){
	var test = []struct{
		value []int
		expected int
	}{
		{
			value: []int{1,2,3,4},
			expected: 4,
		},
		{
			value:[]int{12,13,14,15,16},
			expected: 28,
		},
	}

	for _, tt := range test {
		value,err := sumOfOdd(tt.value)
		if err != nil {
			t.Errorf("unexpected error: %v\n",err)
		}

		if value != tt.expected {
			t.Errorf("expected %v got %v\n",tt.expected, value)
		}
	}
}