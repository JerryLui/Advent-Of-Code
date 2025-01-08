package day07

import (
	"aoc24/helpers"
	"strconv"
	"strings"
)

type Solver struct{}

var operations = map[string]func(int, int) int{
	"+": func(a, b int) int { return a + b },
	"*": func(a, b int) int { return a * b },
}

var operations2 = map[string]func(int, int) int{
	"+": func(a, b int) int { return a + b },
	"*": func(a, b int) int { return a * b },
	"||": func(a, b int) int {
		return helpers.Must(strconv.Atoi(strconv.Itoa(a) + strconv.Itoa(b)))
	},
}

func (s *Solver) SolvePart1(input []string) int {
	res := 0
	for _, line := range input {
		parts := strings.Split(line, ": ")
		num, _ := strconv.Atoi(parts[0])
		parts = strings.Split(parts[1], " ")

		values := make([]int, len(parts))
		for i, part := range parts {
			val, _ := strconv.Atoi(part)
			values[i] = val
		}

		sums := performOperation(0, values[0], values, []int{})
		if helpers.Any(sums, func(sum int) bool {
			return sum == num
		}) {
			res += num
		}
	}
	return res
}

func performOperation(idx int, value int, values []int, sums []int) []int {
	if idx >= len(values)-1 {
		return append(sums, value)
	}

	results := []int{}
	for _, operation := range operations {
		newValue := operation(value, values[idx+1])
		results = append(results, performOperation(idx+1, newValue, values, []int{})...)
	}

	return results
}

func (s *Solver) SolvePart2(input []string) int {
	res := 0
	for _, line := range input {
		parts := strings.Split(line, ": ")
		num, _ := strconv.Atoi(parts[0])
		parts = strings.Split(parts[1], " ")

		values := make([]int, len(parts))
		for i, part := range parts {
			val, _ := strconv.Atoi(part)
			values[i] = val
		}

		sums := performOperation2(0, values[0], values, []int{})
		if helpers.Any(sums, func(sum int) bool {
			return sum == num
		}) {
			res += num
		}
	}
	return res
}

func performOperation2(idx int, value int, values []int, sums []int) []int {
	if idx >= len(values)-1 {
		return append(sums, value)
	}

	results := []int{}
	for _, operation := range operations2 {
		newValue := operation(value, values[idx+1])
		results = append(results, performOperation2(idx+1, newValue, values, []int{})...)
	}

	return results
}
