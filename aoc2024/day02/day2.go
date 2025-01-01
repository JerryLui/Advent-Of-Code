package day02

import (
	"strconv"
	"strings"
)

type Solver struct{}

func (s *Solver) SolvePart1(input []string) int {
	nSafeReports := 0
	for _, level := range input {
		strNums := strings.Fields(level)

		nums := make([]int, len(strNums))
		for i, number := range strNums {
			nums[i], _ = strconv.Atoi(number)
		}

		if isSafe(nums) {
			nSafeReports += 1
		}

	}
	return nSafeReports
}

func (s *Solver) SolvePart2(input []string) int {
	nSafeReports := 0
	for _, level := range input {
		strNums := strings.Fields(level)

		nums := make([]int, len(strNums))
		for i, number := range strNums {
			nums[i], _ = strconv.Atoi(number)
		}

		if isSafe(nums) {
			nSafeReports += 1
		} else if isFixableSafe(nums) {
			nSafeReports += 1
		}

	}
	return nSafeReports
}

func isSafe(numbers []int) bool {
	isIncreasing := false
	for i, number := range numbers {
		if i == 0 {
			continue
		}

		diff := number - numbers[i-1]
		if i == 1 {
			if diff > 0 {
				isIncreasing = true
			}
		}

		if diff == 0 || (isIncreasing && diff < 0) || (!isIncreasing && diff > 0) {
			return false
		}

		if diff < 0 {
			diff = -diff
		}

		if diff < 1 || diff > 3 {
			return false
		}
	}

	return true
}

func isFixableSafe(numbers []int) bool {
	for i := range numbers {
		tmp := make([]int, 0, len(numbers)-1)
		tmp = append(tmp, numbers[:i]...)
		tmp = append(tmp, numbers[i+1:]...)
		if isSafe(tmp) {
			return true
		}
	}
	return false
}
