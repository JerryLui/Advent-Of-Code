package day06

import (
	"aoc24/helpers"
	"errors"
	"fmt"
)

type Solver struct{}

type Direction int

const (
	North Direction = iota
	East
	South
	West
)

type Guard struct {
	x, y      int
	direction Direction
}

var directionDeltas = map[Direction][2]rune{
	North: {-1, 0},
	East:  {0, 1},
	South: {1, 0},
	West:  {0, -1},
}

var directionRunes = map[rune]Direction{
	'^': North,
	'>': East,
	'v': South,
	'<': West,
}

func (p Guard) step() Guard {
	dirDelta := directionDeltas[p.direction]
	return Guard{p.x + int(dirDelta[0]), p.y + int(dirDelta[1]), p.direction}
}

func (p Guard) turn() Guard {
	return Guard{p.x, p.y, p.direction.next()}
}

func (d Direction) next() Direction {
	return (d + 1) % 4
}

func (s *Solver) SolvePart1(input []string) int {
	visited := map[[2]int]bool{}

	pos := helpers.Must(findStart(input))

	for {
		visited[[2]int{pos.x, pos.y}] = true
		newPos := pos.step()
		if isOutOfBounds(newPos, input) {
			return len(visited)
		} else if input[newPos.x][newPos.y] == '#' {
			newPos = pos.turn()
		}
		pos = newPos
	}
}

func (s *Solver) SolvePart2(input []string) int {
	visited := map[[2]int]Direction{}
	blockablePositions := map[Guard]bool{}

	guard := helpers.Must(findStart(input))
	for {
		newPos := guard.step()
		if isOutOfBounds(newPos, input) {
			return len(blockablePositions)
		}

		if input[newPos.x][newPos.y] == '#' {
			newPos = guard.turn()
		} else {
			tmpInput := make([]string, len(input))
			copy(tmpInput, input)
			tmpInput[newPos.x] = tmpInput[newPos.x][:newPos.y] + string('#') + tmpInput[newPos.x][newPos.y+1:]

			if search(guard.turn(), tmpInput, visited) {
				blockablePositions[guard] = true
			}
		}

		visited[[2]int{newPos.x, newPos.y}] = guard.direction
		guard = newPos
	}
}

func search(guard Guard, input []string, visited map[[2]int]Direction) bool {
	ogg := Guard{guard.x, guard.y, guard.direction}
	visitedCount := make(map[Guard]int)

	for i := 0; i < 1_000_000; i++ {
		visitedCount[guard] += 1
		if visitedCount[guard] > 4 {
			return true
		}

		newGuard := guard.step()
		if isOutOfBounds(newGuard, input) {
			return false
		} else if input[newGuard.x][newGuard.y] == '#' {
			newGuard = guard.turn()
		}
		guard = newGuard
	}
	fmt.Println(ogg)
	return false
}

func printInputWithPath(input []string, visited map[[2]int]Direction) {
	tmpInput := make([]string, len(input))
	copy(tmpInput, input)

	for k := range visited {
		tmpInput[k[0]] = tmpInput[k[0]][:k[1]] + string('+') + tmpInput[k[0]][k[1]+1:]
	}
	for _, row := range tmpInput {
		fmt.Println(row)
	}
}

func findStart(input []string) (Guard, error) {
	for i, line := range input {
		for j, char := range line {
			if dir, ok := directionRunes[char]; ok {
				return Guard{i, j, dir}, nil
			}
		}
	}
	return Guard{}, errors.New("no starting position found")
}

func isOutOfBounds(pos Guard, input []string) bool {
	if pos.x < 0 || pos.x >= len(input) || pos.y < 0 || pos.y >= len(input[0]) {
		return true
	}
	return false
}
