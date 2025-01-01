package day01

import (
	"aoc24/helpers"
	"sort"
	"strconv"
	"strings"
)

type Solver struct{}

func (s *Solver) SolvePart1(input []string) int {
	nums1 := make([]int, len(input))
	nums2 := make([]int, len(input))

	for i, line := range input {
		nums := strings.Fields(line)
		nums1[i], _ = strconv.Atoi(nums[0])
		nums2[i], _ = strconv.Atoi(nums[1])
	}

	sort.Ints(nums1)
	sort.Ints(nums2)

	result := 0
	for i := range nums1 {
		diff := nums1[i] - nums2[i]
		if diff > 0 {
			result += diff
		} else {
			result -= diff
		}
	}

	return result
}

func (s *Solver) SolvePart2(input []string) int {
	nums1 := make([]int, len(input))
	nums2 := helpers.NewCounter[int]()

	for i, line := range input {
		nums := strings.Fields(line)
		nums1[i], _ = strconv.Atoi(nums[0])
		n, _ := strconv.Atoi(nums[1])
		nums2.Add(n)
	}

	result := 0
	for _, n := range nums1 {
		result += n * nums2.Get(n)
	}

	return result
}
