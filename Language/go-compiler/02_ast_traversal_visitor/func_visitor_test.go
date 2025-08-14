package _02_ast_traversal_visitor

import (
	"fmt"
	"go/ast"
	"go/parser"
	"go/token"
	"os"
	"testing"
)

type FuncVisitor struct{}

func (v *FuncVisitor) Visit(node ast.Node) ast.Visitor {
	if node == nil {
		return nil
	}

	if fn, ok := node.(*ast.FuncDecl); ok {
		fmt.Printf("Found function: %s\n", fn.Name.Name)

		if fn.Type.Params != nil && len(fn.Type.Params.List) > 0 {
			fmt.Println("  Parameters:")
			for _, param := range fn.Type.Params.List {
				paramNames := []string{}
				for _, name := range param.Names {
					paramNames = append(paramNames, name.Name)
				}

				if paramType, ok := param.Type.(*ast.Ident); ok {
					fmt.Printf("  - Names: %v, Type: %s\n", paramNames, paramType.Name)
				}
			}
		} else {
			fmt.Println("  Parameters: None")
		}

		if fn.Type.Results != nil && len(fn.Type.Results.List) > 0 {
			fmt.Println("  Return values:")
			for _, result := range fn.Type.Results.List {
				paramNames := []string{}
				for _, name := range result.Names {
					paramNames = append(paramNames, name.Name)
				}

				if paramType, ok := result.Type.(*ast.Ident); ok {
					fmt.Printf("  - Names: %v, Type: %s\n", paramNames, paramType.Name)
				}
			}
		} else {
			fmt.Println("  Return values: None")
		}
		fmt.Println("-----")
	}

	return v
}

func TestVisitFuncDecl(t *testing.T) {
	srcBytes, err := os.ReadFile("../testdata/main_with_func_declare.go")
	if err != nil {
		t.Fatal("Failed to read source file: ", err)
	}

	fileSet := token.NewFileSet()
	astFile, err := parser.ParseFile(fileSet, "main_with_func_declare.go", srcBytes, 0)
	if err != nil {
		t.Fatal("Failed to parse source file: ", err)
	}

	v := &FuncVisitor{}
	ast.Walk(v, astFile)
}
