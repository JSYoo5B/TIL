// Code generated from DAG.g4 by ANTLR 4.13.2. DO NOT EDIT.

package parser // DAG
import "github.com/antlr4-go/antlr/v4"

// A complete Visitor for a parse tree produced by DAGParser.
type DAGVisitor interface {
	antlr.ParseTreeVisitor

	// Visit a parse tree produced by DAGParser#program.
	VisitProgram(ctx *ProgramContext) interface{}

	// Visit a parse tree produced by DAGParser#importStatement.
	VisitImportStatement(ctx *ImportStatementContext) interface{}

	// Visit a parse tree produced by DAGParser#dagStatement.
	VisitDagStatement(ctx *DagStatementContext) interface{}

	// Visit a parse tree produced by DAGParser#parameters.
	VisitParameters(ctx *ParametersContext) interface{}

	// Visit a parse tree produced by DAGParser#parameter.
	VisitParameter(ctx *ParameterContext) interface{}

	// Visit a parse tree produced by DAGParser#nodesStatement.
	VisitNodesStatement(ctx *NodesStatementContext) interface{}

	// Visit a parse tree produced by DAGParser#nodeAssignment.
	VisitNodeAssignment(ctx *NodeAssignmentContext) interface{}

	// Visit a parse tree produced by DAGParser#successStatement.
	VisitSuccessStatement(ctx *SuccessStatementContext) interface{}

	// Visit a parse tree produced by DAGParser#errorStatement.
	VisitErrorStatement(ctx *ErrorStatementContext) interface{}

	// Visit a parse tree produced by DAGParser#abortStatement.
	VisitAbortStatement(ctx *AbortStatementContext) interface{}

	// Visit a parse tree produced by DAGParser#branchesStatement.
	VisitBranchesStatement(ctx *BranchesStatementContext) interface{}

	// Visit a parse tree produced by DAGParser#edgeStatement.
	VisitEdgeStatement(ctx *EdgeStatementContext) interface{}

	// Visit a parse tree produced by DAGParser#branchAssignment.
	VisitBranchAssignment(ctx *BranchAssignmentContext) interface{}

	// Visit a parse tree produced by DAGParser#branchPair.
	VisitBranchPair(ctx *BranchPairContext) interface{}

	// Visit a parse tree produced by DAGParser#stringLiteral.
	VisitStringLiteral(ctx *StringLiteralContext) interface{}
}
