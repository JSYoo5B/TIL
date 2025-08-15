package _05_get_function_info

type Graph struct {
	Name  string
	Nodes map[string]bool
	Edges []Edge
}

type Edge struct {
	Source string
	Dest   string
	Label  string
}

func NewGraph(name string) *Graph {
	return &Graph{
		Name:  name,
		Nodes: make(map[string]bool),
		Edges: make([]Edge, 0),
	}
}
