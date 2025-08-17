package _07_antlr_multi_dag_parser

import (
	"fmt"
	"go-compiler/testdata/dsl/parser"
)

type AstBuilder struct {
	*parser.BaseDAGListener
	Program    *Program
	currentDag *DagStatement
}

func NewAstBuilder() *AstBuilder {
	return &AstBuilder{
		Program: &Program{},
	}
}

func (b *AstBuilder) EnterDagStatement(ctx *parser.DagStatementContext) {
	name := ctx.GetName().GetText()
	typ := ctx.GetTyp().GetText()

	dagStmt := &DagStatement{
		Name: name,
		Type: typ,
	}
	b.Program.DagStatements = append(b.Program.DagStatements, dagStmt)
	b.currentDag = dagStmt
}

func (b *AstBuilder) ExitDagStatement(ctx *parser.DagStatementContext) {
	b.currentDag = nil
}

func (b *AstBuilder) EnterNodeAssignment(ctx *parser.NodeAssignmentContext) {
	if b.currentDag == nil {
		return
	}

	name := ctx.GetName().GetText()
	expression := ctx.GetInitializer().GetText()

	fmt.Printf("Listener: Node '%s' (constructor: %s)!\n", name, expression)

	nodeAssign := &NodeAssignment{
		Name:       name,
		Expression: expression,
	}
	b.currentDag.Nodes = append(b.currentDag.Nodes, nodeAssign)
}
