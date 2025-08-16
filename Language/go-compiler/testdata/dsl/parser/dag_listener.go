// Code generated from DAG.g4 by ANTLR 4.13.2. DO NOT EDIT.

package parser // DAG
import "github.com/antlr4-go/antlr/v4"

// DAGListener is a complete listener for a parse tree produced by DAGParser.
type DAGListener interface {
	antlr.ParseTreeListener

	// EnterProgram is called when entering the program production.
	EnterProgram(c *ProgramContext)

	// EnterImportStatement is called when entering the importStatement production.
	EnterImportStatement(c *ImportStatementContext)

	// EnterDagStatement is called when entering the dagStatement production.
	EnterDagStatement(c *DagStatementContext)

	// EnterParameters is called when entering the parameters production.
	EnterParameters(c *ParametersContext)

	// EnterParameter is called when entering the parameter production.
	EnterParameter(c *ParameterContext)

	// EnterNodesStatement is called when entering the nodesStatement production.
	EnterNodesStatement(c *NodesStatementContext)

	// EnterNodeAssignment is called when entering the nodeAssignment production.
	EnterNodeAssignment(c *NodeAssignmentContext)

	// EnterSuccessStatement is called when entering the successStatement production.
	EnterSuccessStatement(c *SuccessStatementContext)

	// EnterErrorStatement is called when entering the errorStatement production.
	EnterErrorStatement(c *ErrorStatementContext)

	// EnterAbortStatement is called when entering the abortStatement production.
	EnterAbortStatement(c *AbortStatementContext)

	// EnterBranchesStatement is called when entering the branchesStatement production.
	EnterBranchesStatement(c *BranchesStatementContext)

	// EnterEdgeStatement is called when entering the edgeStatement production.
	EnterEdgeStatement(c *EdgeStatementContext)

	// EnterBranchAssignment is called when entering the branchAssignment production.
	EnterBranchAssignment(c *BranchAssignmentContext)

	// EnterBranchPair is called when entering the branchPair production.
	EnterBranchPair(c *BranchPairContext)

	// EnterStringLiteral is called when entering the stringLiteral production.
	EnterStringLiteral(c *StringLiteralContext)

	// ExitProgram is called when exiting the program production.
	ExitProgram(c *ProgramContext)

	// ExitImportStatement is called when exiting the importStatement production.
	ExitImportStatement(c *ImportStatementContext)

	// ExitDagStatement is called when exiting the dagStatement production.
	ExitDagStatement(c *DagStatementContext)

	// ExitParameters is called when exiting the parameters production.
	ExitParameters(c *ParametersContext)

	// ExitParameter is called when exiting the parameter production.
	ExitParameter(c *ParameterContext)

	// ExitNodesStatement is called when exiting the nodesStatement production.
	ExitNodesStatement(c *NodesStatementContext)

	// ExitNodeAssignment is called when exiting the nodeAssignment production.
	ExitNodeAssignment(c *NodeAssignmentContext)

	// ExitSuccessStatement is called when exiting the successStatement production.
	ExitSuccessStatement(c *SuccessStatementContext)

	// ExitErrorStatement is called when exiting the errorStatement production.
	ExitErrorStatement(c *ErrorStatementContext)

	// ExitAbortStatement is called when exiting the abortStatement production.
	ExitAbortStatement(c *AbortStatementContext)

	// ExitBranchesStatement is called when exiting the branchesStatement production.
	ExitBranchesStatement(c *BranchesStatementContext)

	// ExitEdgeStatement is called when exiting the edgeStatement production.
	ExitEdgeStatement(c *EdgeStatementContext)

	// ExitBranchAssignment is called when exiting the branchAssignment production.
	ExitBranchAssignment(c *BranchAssignmentContext)

	// ExitBranchPair is called when exiting the branchPair production.
	ExitBranchPair(c *BranchPairContext)

	// ExitStringLiteral is called when exiting the stringLiteral production.
	ExitStringLiteral(c *StringLiteralContext)
}
