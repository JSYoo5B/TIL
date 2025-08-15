package _03_ast_struct_visitor

import (
	"fmt"
	"go/ast"
	"go/parser"
	"go/token"
	"os"
	"reflect"
	"strconv"
	"testing"
)

type StructVisitor struct{}

func (v *StructVisitor) Visit(node ast.Node) ast.Visitor {
	if typeSpec, ok := node.(*ast.TypeSpec); ok {
		if structType, ok := typeSpec.Type.(*ast.StructType); ok {
			fmt.Printf("Found struct: %s\n", typeSpec.Name.Name)

			for _, field := range structType.Fields.List {
				if field.Tag != nil {
					tagStr, _ := strconv.Unquote(field.Tag.Value)

					tag := reflect.StructTag(tagStr)

					fieldName := field.Names[0].Name
					fmt.Printf("  - Field: %s,JSON Tag: '%s', \tDB Tag: '%s'\n",
						fieldName,
						tag.Get("json"),
						tag.Get("db"),
					)
				}
			}
			fmt.Println("-----")
		}
	}

	return v
}

func TestVisitStructTags(t *testing.T) {
	srcBytes, err := os.ReadFile("../testdata/struct_tags.go")
	if err != nil {
		t.Fatal("Failed to read source file: ", err)
	}

	fileSet := token.NewFileSet()
	astFile, err := parser.ParseFile(fileSet, "struct_tags.go", srcBytes, 0)
	if err != nil {
		t.Fatal("Failed to parse source file: ", err)
	}

	v := &StructVisitor{}
	ast.Walk(v, astFile)
}
