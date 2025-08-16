// Code generated from DAG.g4 by ANTLR 4.13.2. DO NOT EDIT.

package parser // DAG
import "github.com/antlr4-go/antlr/v4"

type BaseDAGVisitor struct {
	*antlr.BaseParseTreeVisitor
}

func (v *BaseDAGVisitor) VisitProgram(ctx *ProgramContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseDAGVisitor) VisitImportStatement(ctx *ImportStatementContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseDAGVisitor) VisitDagStatement(ctx *DagStatementContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseDAGVisitor) VisitParameters(ctx *ParametersContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseDAGVisitor) VisitParameter(ctx *ParameterContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseDAGVisitor) VisitNodesStatement(ctx *NodesStatementContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseDAGVisitor) VisitNodeAssignment(ctx *NodeAssignmentContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseDAGVisitor) VisitSuccessStatement(ctx *SuccessStatementContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseDAGVisitor) VisitErrorStatement(ctx *ErrorStatementContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseDAGVisitor) VisitAbortStatement(ctx *AbortStatementContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseDAGVisitor) VisitBranchesStatement(ctx *BranchesStatementContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseDAGVisitor) VisitEdgeStatement(ctx *EdgeStatementContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseDAGVisitor) VisitBranchAssignment(ctx *BranchAssignmentContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseDAGVisitor) VisitBranchPair(ctx *BranchPairContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseDAGVisitor) VisitStringLiteral(ctx *StringLiteralContext) interface{} {
	return v.VisitChildren(ctx)
}
