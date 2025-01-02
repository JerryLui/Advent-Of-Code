package day03

import (
	"regexp"
	"strconv"
	"strings"
)

type Solver struct{}

func (s *Solver) SolvePart1(input []string) int {
	pattern := regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)`)
	total := 0
	for _, line := range input {
		matches := pattern.FindAllStringSubmatch(line, -1)
		for _, match := range matches {
			n0, _ := strconv.Atoi(match[1])
			n1, _ := strconv.Atoi(match[2])
			total += n0 * n1
		}
	}
	return total
}

func (s *Solver) SolvePart2(input []string) int {
	// for i, line := range input {
	// 	input[i] = stripBetweenDoDonts(line)
	// }
	// return s.SolvePart1(input)
	return s.SolvePart1([]string{stripBetweenDoDonts(strings.Join(input, ""))})
}

func stripBetweenDoDonts(input string) string {
	pattern := regexp.MustCompile(`don't\(\)(.*?)(:?do\(\)|$)`)
	input = pattern.ReplaceAllString(input, "")
	return input
}
