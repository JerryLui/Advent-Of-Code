package helpers

type Counter[T comparable] struct {
	counts map[T]int
}

func NewCounter[T comparable]() *Counter[T] {
	return &Counter[T]{
		counts: make(map[T]int),
	}
}

func (c *Counter[T]) Add(item T) {
	c.counts[item]++
}

func (c *Counter[T]) Get(item T) int {
	return c.counts[item]
}
