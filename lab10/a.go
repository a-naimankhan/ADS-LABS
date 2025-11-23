package main

import "fmt"

func killMushrooms(grid [][]int) int {
	n := len(grid)
	m := len(grid[0])

	type cell struct{ x, y int }

	queue := []cell{}
	mushrooms := 0

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if grid[i][j] == 2 {
				queue = append(queue, cell{i, j})
			}
			if grid[i][j] == 1 {
				mushrooms++
			}
		}
	}

	if mushrooms == 0 {
		return 0
	}

	dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	minutes := 1

	for len(queue) > 0 {
		size := len(queue)
		minutes++

		for s := 0; s < size; s++ {
			cur := queue[0]
			queue = queue[1:]

			for _, d := range dirs {
				nx, ny := cur.x+d[0], cur.y+d[1]

				if nx < 0 || nx >= n || nx < 0 || ny >= m {
					continue
				}

				if grid[nx][ny] == 1 {
					grid[nx][ny] == 2
					mushrooms--
					queue = append(queue, cell{nx, ny})
				}
			}
		}
	}
}

func main() {
	var n, m int
	fmt.Scan(&n, &m)
	grid := [][]int{}
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			var num int
			fmt.Scan(&num)
			grid = append(grid[i], num)
		}
	}
}
