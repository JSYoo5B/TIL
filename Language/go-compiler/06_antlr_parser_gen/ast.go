package _06_antlr_parser_gen

type Program struct {
	DagStatements []*DagStatement
}

type DagStatement struct {
	Name string
	Type string
	// TODO: Parameters, body, etc...
}
