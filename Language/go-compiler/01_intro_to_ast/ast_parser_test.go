package _01_intro_to_ast

import (
	"go/ast"
	"go/parser"
	"go/token"
	"os"
	"testing"
)

func TestAstPrint(t *testing.T) {
	srcBytes, err := os.ReadFile("../testdata/simple_main.go")
	if err != nil {
		t.Fatal("Failed to read source file: ", err)
	}

	fileSet := token.NewFileSet()
	astFile, err := parser.ParseFile(fileSet, "simple_main.go", srcBytes, 0)
	if err != nil {
		t.Fatal("Failed to parse source file: ", err)
	}

	_ = ast.Print(fileSet, astFile)
}
