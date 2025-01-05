package day04

import (
	"aoc24/helpers"
)

type Solver struct{}

func (s *Solver) SolvePart1(input []string) int {
	res := 0
	for i, line := range input {
		for j := range line {
			iNotAtBoundrary := i+3 < len(input)
			jNotAtBoundrary := j+3 < len(line)
			if jNotAtBoundrary {
				if checkSequence([]byte(input[i][j : j+4])) {
					res += 1
				}
			}

			if iNotAtBoundrary {
				colStr := make([]byte, 0, 4)
				for ii := i; ii < i+4; ii++ {
					colStr = append(colStr, input[ii][j])
				}
				if checkSequence(colStr) {
					res += 1
				}
			}

			if iNotAtBoundrary && jNotAtBoundrary {
				rDiag := make([]byte, 0, 4)
				for ii, jj := i, j; ii < i+4; ii, jj = ii+1, jj+1 {
					rDiag = append(rDiag, input[ii][jj])
				}
				if checkSequence(rDiag) {
					res += 1
				}
			}

			if iNotAtBoundrary && j-2 > 0 {
				lDiag := make([]byte, 0, 4)
				for ii, jj := i, j; ii < i+4; ii, jj = ii+1, jj-1 {
					lDiag = append(lDiag, input[ii][jj])
				}
				if checkSequence(lDiag) {
					res += 1
				}
			}

		}
	}
	return res
}

func (s *Solver) SolvePart2(input []string) int {
	res := 0
	for i, line := range input {
		for j, char := range line {
			if char == 'A' {
				if i-1 >= 0 && j-1 >= 0 && i+1 < len(input) && j+1 < len(line) {
					rDiag := []byte{input[i-1][j-1], 'A', input[i+1][j+1]}
					lDiag := []byte{input[i-1][j+1], 'A', input[i+1][j-1]}
					if checkSequence2(rDiag) && checkSequence2(lDiag) {
						res += 1
					}
				}
			}
		}
	}
	return res
}

func checkSequence(str []byte) bool {
	xmas := []byte{'X', 'M', 'A', 'S'}
	samx := []byte{'S', 'A', 'M', 'X'}
	return helpers.CompareSlices(str, xmas) || helpers.CompareSlices(str, samx)
}

func checkSequence2(str []byte) bool {
	mas := []byte{'M', 'A', 'S'}
	sam := []byte{'S', 'A', 'M'}
	return helpers.CompareSlices(str, mas) || helpers.CompareSlices(str, sam)
}

// func (s *Solver) SolvePart1(input []string) int {
// 	result := 0
// 	searchStrings := make(map[string]string)

// 	for i, line := range input {
// 		for j, letter := range line {
// 			searchStrings["col_"+strconv.Itoa(j)] += string(letter)
// 			if i == 0 || j == 0 || j == 9 {

// 				diagKey := fmt.Sprintf("right_%d+%d", i, j)
// 				for di, dj := 0, 0; i+di < len(input) && j+dj < len(input[0]); di, dj = di+1, dj+1 {
// 					searchStrings[diagKey] += string(input[i+di][j+dj])
// 				}

// 				diagKey = fmt.Sprintf("left_%d+%d", i, j)
// 				for di, dj := 0, 0; i+di < len(input) && j-dj >= 0; di, dj = di+1, dj+1 {
// 					searchStrings[diagKey] += string(input[i+di][j-dj])
// 				}
// 			}
// 		}
// 		searchStrings["row_"+strconv.Itoa(i)] = line
// 	}

// 	// var pattern = regexp.MustCompile(`XMAS`)
// 	// var reversePattern = regexp.MustCompile(`SAMX`)
// 	keys := make([]string, 0, len(searchStrings))
// 	for k := range searchStrings {
// 		keys = append(keys, k)
// 	}
// 	sort.Strings(keys)

// 	for _, key := range keys {
// 		line := searchStrings[key]
// 		if len(line) < 4 {
// 			continue
// 		}
// 		n1 := strings.Count(line, "XMAS")
// 		n2 := strings.Count(line, "SAMX")
// 		// matches := pattern.FindAllString(line, -1)
// 		// reverseMatches := reversePattern.FindAllString(line, -1)
// 		// if len(matches) > 0 || len(reverseMatches) > 0 {
// 		// 	result += len(matches) + len(reverseMatches)
// 		// }
// 		// result += n1 + n2
// 		// fmt.Println(key)
// 		if n1 > 0 || n2 > 0 {
// 			fmt.Println(line)
// 		}
// 	}

// 	return result
// }

// func (s *Solver) SolvePart2(input []string) int {
// 	return 0
// }
