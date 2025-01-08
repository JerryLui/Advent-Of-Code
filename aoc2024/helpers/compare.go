package helpers

// CompareSlices compares two slices of comparable types for equality.
// Returns true if both slices have the same length and all elements match at corresponding indices.
func CompareSlices[T comparable](a []T, b []T) bool {
	if len(a) != len(b) {
		return false
	}

	for i, v := range a {
		if v != b[i] {
			return false
		}
	}
	return true
}

// All checks if all elements in a slice are equal to each other.
// Returns true if the slice has 0 or 1 elements, or if all elements are equal to the first element.
func All[T comparable](a []T) bool {
	if len(a) < 2 {
		return true
	}

	for _, v := range a {
		if a[0] != v {
			return false
		}
	}
	return true
}

func Any[T comparable](a []T, f func(T) bool) bool {
	for _, v := range a {
		if f(v) {
			return true
		}
	}
	return false
}
