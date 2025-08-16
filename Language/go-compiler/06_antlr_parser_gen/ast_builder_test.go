package _06_antlr_parser_gen

import (
	"fmt"
	"github.com/antlr4-go/antlr/v4"
	"go-compiler/testdata/dsl/parser"
	"os"
	"testing"
)

func TestAstBuilder_DagStatement(t *testing.T) {
	srcBytes, err := os.ReadFile("../testdata/dsl/example/single-dag.dag")
	if err != nil {
		t.Fatal("Failed to read source file: ", err)
	}

	is := antlr.NewInputStream(string(srcBytes))
	lexer := parser.NewDAGLexer(is)
	stream := antlr.NewCommonTokenStream(lexer, antlr.TokenDefaultChannel)
	p := parser.NewDAGParser(stream)

	tree := p.Program()

	builder := NewAstBuilder()

	antlr.ParseTreeWalkerDefault.Walk(builder, tree)

	fmt.Println("--- Built AST ---")
	for _, dag := range builder.Program.DagStatements {
		fmt.Printf("DAG Name: %s, Type: %s\n", dag.Name, dag.Type)
	}
}

func TestAstBuilder_DagStatementWithMultipleDags(t *testing.T) {
	srcBytes, err := os.ReadFile("../testdata/dsl/example/multiple-dag.dag")
	if err != nil {
		t.Fatal("Failed to read source file: ", err)
	}

	is := antlr.NewInputStream(string(srcBytes))
	lexer := parser.NewDAGLexer(is)
	stream := antlr.NewCommonTokenStream(lexer, antlr.TokenDefaultChannel)
	p := parser.NewDAGParser(stream)

	tree := p.Program()

	builder := NewAstBuilder()

	antlr.ParseTreeWalkerDefault.Walk(builder, tree)

	fmt.Println("--- Built AST ---")
	for _, dag := range builder.Program.DagStatements {
		fmt.Printf("DAG Name: %s, Type: %s\n", dag.Name, dag.Type)
	}
}
