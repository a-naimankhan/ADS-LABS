package main

type Node struct {
	val  int
	next *Node
}

func (n *Node) push(val int) {
	n.next.val = val

}
