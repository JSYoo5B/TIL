package _05_get_function_info

import (
	"go/ast"
	"go/parser"
	"go/token"
	"os"
	"testing"
)

func TestAnalyzeNewPipeline(t *testing.T) {
	srcBytes, err := os.ReadFile("../testdata/chain_collatz.go")
	if err != nil {
		t.Fatal("Failed to read source file: ", err)
	}

	fileSet := token.NewFileSet()
	astFile, err := parser.ParseFile(fileSet, "chain_collatz.go", srcBytes, 0)
	if err != nil {
		t.Fatal("Failed to parse source file: ", err)
	}

	v := &DagVisitor{Graph: NewGraph("")}
	ast.Walk(v, astFile)
}
