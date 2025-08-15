package _04_ast_codegen

import (
	"bytes"
	_ "embed"
	"fmt"
	"go/ast"
	"go/parser"
	"go/token"
	"os"
	"testing"
	"text/template"
)

//go:embed method.tmpl
var methodTmpl string

var methodTemplate *template.Template

func init() {
	var err error
	if methodTemplate, err = template.New("method").Parse(methodTmpl); err != nil {
		panic(err)
	}
}

type TemplateData struct {
	ReceiverName string
	StructName   string
	FieldName    string
}

type CodeGenVisitor struct {
	GeneratedCode *bytes.Buffer
}

func (v *CodeGenVisitor) Visit(node ast.Node) ast.Visitor {
	typeSpec, ok := node.(*ast.TypeSpec)
	if !ok {
		return v
	}

	structType, ok := typeSpec.Type.(*ast.StructType)
	if !ok {
		return v
	}

	for _, field := range structType.Fields.List {
		if field.Tag == nil {
			continue
		}

		// tagStr, _ := strconv.Unquote(field.Tag.Value)
		// tag := reflect.StructTag(tagStr)
		//
		// if tag.Get("json") == "id" {
		data := TemplateData{
			ReceiverName: string(typeSpec.Name.Name[0]),
			StructName:   typeSpec.Name.Name,
			FieldName:    field.Names[0].Name,
		}

		if err := methodTemplate.Execute(v.GeneratedCode, data); err != nil {
			panic(err)
		}
		// }
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

	buf := new(bytes.Buffer)
	v := &CodeGenVisitor{GeneratedCode: buf}
	ast.Walk(v, astFile)

	fmt.Println("--- Generated code ---")
	fmt.Println(buf.String())
}
