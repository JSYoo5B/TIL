package _06_antlr_parser_gen

import (
	"fmt"
	"go-compiler/testdata/dsl/parser"
)

type AstBuilder struct {
	*parser.BaseDAGListener
	Program *Program
}

func NewAstBuilder() *AstBuilder {
	return &AstBuilder{
		Program: &Program{},
	}
}

func (b *AstBuilder) EnterDagStatement(ctx *parser.DagStatementContext) {
	name := ctx.GetName().GetText()
	typ := ctx.GetTyp().GetText()

	fmt.Printf("Listener: dag '%s' (type %s) declaration found\n", name, typ)

	dagStmt := &DagStatement{
		Name: name,
		Type: typ,
	}

	b.Program.DagStatements = append(b.Program.DagStatements, dagStmt)
}
