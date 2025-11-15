package main

import "fmt"

// LPS строит массив Longest Prefix-Suffix для шаблона
func buildLPS(pattern string) []int {
	m := len(pattern)
	lps := make([]int, m)
	length := 0 // длина текущего совпадения
	i := 1

	for i < m {
		if pattern[i] == pattern[length] {
			length++
			lps[i] = length
			i++
		} else {
			if length != 0 {
				// ⚡ не сбрасываем в 0, а откатываем к предыдущему совпадению
				length = lps[length-1]
			} else {
				lps[i] = 0
				i++
			}
		}
	}
	return lps
}

// KMP ищет все вхождения pattern в text
func KMP(text, pattern string) []int {
	n := len(text)
	m := len(pattern)
	lps := buildLPS(pattern)
	var result []int

	i, j := 0, 0 // i = текст, j = паттерн

	for i < n {
		if text[i] == pattern[j] {
			i++
			j++
		}

		if j == m {
			// Нашли совпадение: i-j — индекс начала
			result = append(result, i-j)
			j = lps[j-1] // продолжаем искать дальше
		} else if i < n && text[i] != pattern[j] {
			if j != 0 {
				j = lps[j-1]
			} else {
				i++
			}
		}
	}

	return result
}

func main() {
	text := "ABABAB"
	pattern := "ABABC"
	indices := KMP(text, pattern)
	fmt.Println("Found at indices:", indices)
}
