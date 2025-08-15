package _05_get_function_info

import (
	"fmt"
	"go/ast"
	"strconv"
)

type DagVisitor struct {
	Graph *Graph
}

func (v *DagVisitor) Visit(node ast.Node) ast.Visitor {
	callExpr, ok := node.(*ast.CallExpr)
	if !ok {
		return v
	}

	selector, ok := callExpr.Fun.(*ast.SelectorExpr)
	if !ok {
		return v
	}

	if selector.Sel.Name == "NewPipeline" {
		fmt.Println("Found NewPipeline call!")

		pipelineName, _ := strconv.Unquote(callExpr.Args[0].(*ast.BasicLit).Value)
		v.Graph.Name = pipelineName

		actions := callExpr.Args[1:]
		var nodeNames []string

		for _, arg := range actions {
			if ident, ok := arg.(*ast.Ident); ok {
				v.Graph.Nodes[ident.Name] = true
				nodeNames = append(nodeNames, ident.Name)
			}
		}

		// 기본 Success 간선을 연결합니다.
		for i := 0; i < len(nodeNames)-1; i++ {
			edge := Edge{
				Source: nodeNames[i],
				Dest:   nodeNames[i+1],
				Label:  "Success", // NewPipeline의 기본 연결은 Success입니다.
			}
			v.Graph.Edges = append(v.Graph.Edges, edge)
		}
		fmt.Printf("Initial nodes: %v\n", nodeNames)
		fmt.Printf("Initial edges: %v\n", v.Graph.Edges)
	}

	return v
}
