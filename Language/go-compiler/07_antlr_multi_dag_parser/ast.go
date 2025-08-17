package _07_antlr_multi_dag_parser

type Program struct {
	DagStatements []*DagStatement
}

type DagStatement struct {
	Name      string
	Type      string
	Generates string
	Nodes     []*NodeAssignment
}

type NodeAssignment struct {
	Name       string
	Expression string
}
