package day05

import (
	"aoc24/helpers"
	"sort"
	"strconv"
	"strings"
)

type Solver struct{}

func (s *Solver) SolvePart1(input []string) int {
	res := 0
	ruleArr, updates := splitInput(input)
	ruleMap := createLargerThanMap(ruleArr)
	for _, update := range updates {
		pages := strings.Split(update, ",")
		if isCorrect(pages, ruleMap) {
			res += getMiddleValue(pages)
		}
	}

	return res
}

func (s *Solver) SolvePart2(input []string) int {
	res := 0
	ruleArr, updates := splitInput(input)
	ruleMap := createLargerThanMap(ruleArr)

	for _, update := range updates {
		pages := strings.Split(update, ",")
		if !isCorrect(pages, ruleMap) {
			fixOrdering(pages, ruleMap)
			res += getMiddleValue(pages)
		}
	}

	return res
}

func fixOrdering(arr []string, rules map[string]map[string]struct{}) {
	sort.Slice(arr, func(i, j int) bool {
		if _, ok := rules[arr[i]][arr[j]]; ok {
			return true
		}
		return false
	})
}

func splitInput(arr []string) ([]string, []string) {
	for i, val := range arr {
		if val == "" {
			return arr[:i], arr[i+1:]
		}
	}
	return arr, []string{}
}

func createLargerThanMap(arr []string) map[string]map[string]struct{} {
	lmap := make(map[string]map[string]struct{})
	for _, line := range arr {
		res := strings.Split(line, "|")
		if _, ok := lmap[res[0]]; !ok {
			lmap[res[0]] = make(map[string]struct{})
		}
		lmap[res[0]][res[1]] = struct{}{}
	}
	return lmap
}

func isCorrect(pages []string, rules map[string]map[string]struct{}) bool {
	for j, page := range pages {
		for k := j + 1; k < len(pages); k++ {
			if _, exists := rules[page][pages[k]]; !exists {
				return false
			}
		}
	}
	return true
}

func getMiddleValue(pages []string) int {
	middle := pages[len(pages)/2]
	return helpers.Must(strconv.Atoi(middle))
}
