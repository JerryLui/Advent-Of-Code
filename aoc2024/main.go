package main

import (
	"aoc24/day01"
	"aoc24/day02"
	"aoc24/day03"
	"bufio"
	"fmt"
	"io"
	"net/http"
	"os"
	"path/filepath"
	"strconv"
)

type Solver interface {
	SolvePart1([]string) int
	SolvePart2([]string) int
}

var solvers = map[string]Solver{
	"1": &day01.Solver{},
	"2": &day02.Solver{},
	"3": &day03.Solver{},
}

func main() {
	if len(os.Args) < 3 {
		fmt.Fprintln(os.Stderr, "Usage: aoc24 <day> <part>")
		os.Exit(1)
	}

	day := os.Args[1]
	part := os.Args[2]

	solver, exists := solvers[day]
	if !exists {
		fmt.Fprintf(os.Stderr, "Solution not implemented for day %s\n", day)
		os.Exit(1)
	}

	input, err := readInput(day)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error reading input: %v\n", err)
		os.Exit(1)
	}

	var result int
	switch part {
	case "1":
		result = solver.SolvePart1(input)
	case "2":
		result = solver.SolvePart2(input)
	default:
		fmt.Fprintf(os.Stderr, "Invalid part: %s\n", part)
		os.Exit(1)
	}

	fmt.Println(result)
}

func readInput(day string) ([]string, error) {
	dayNum, err := strconv.Atoi(day)
	if err != nil {
		return nil, fmt.Errorf("invalid day number: %w", err)
	}

	path := fmt.Sprintf("day%02d/input.txt", dayNum)
	if _, err := os.Stat(path); os.IsNotExist(err) {
		if err := downloadInput(dayNum, path); err != nil {
			return nil, fmt.Errorf("downloading input: %w", err)
		}
	}

	file, err := os.Open(path)
	if err != nil {
		return nil, fmt.Errorf("opening input file: %w", err)
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		return nil, fmt.Errorf("reading input file: %w", err)
	}

	return lines, nil
}

func downloadInput(dayNum int, path string) error {
	token := os.Getenv("AOC_TOKEN")
	if token == "" {
		return fmt.Errorf("AOC_TOKEN environment variable not set")
	}

	fmt.Printf("%s not found, downloading input for day %d...\n", path, dayNum)
	client := &http.Client{}
	url := fmt.Sprintf("https://adventofcode.com/2024/day/%d/input", dayNum)
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return fmt.Errorf("creating request: %w", err)
	}

	req.AddCookie(&http.Cookie{
		Name:  "session",
		Value: token,
	})

	resp, err := client.Do(req)
	if err != nil {
		return fmt.Errorf("making request: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return fmt.Errorf("server returned error: %s", resp.Status)
	}

	if err := os.MkdirAll(filepath.Dir(path), 0755); err != nil {
		return fmt.Errorf("creating directory: %w", err)
	}

	out, err := os.Create(path)
	if err != nil {
		return fmt.Errorf("creating output file: %w", err)
	}
	defer out.Close()

	if _, err := io.Copy(out, resp.Body); err != nil {
		return fmt.Errorf("writing to file: %w", err)
	}

	return nil
}
