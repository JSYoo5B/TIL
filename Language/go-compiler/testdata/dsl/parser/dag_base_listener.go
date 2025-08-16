// Code generated from DAG.g4 by ANTLR 4.13.2. DO NOT EDIT.

package parser // DAG
import "github.com/antlr4-go/antlr/v4"

// BaseDAGListener is a complete listener for a parse tree produced by DAGParser.
type BaseDAGListener struct{}

var _ DAGListener = &BaseDAGListener{}

// VisitTerminal is called when a terminal node is visited.
func (s *BaseDAGListener) VisitTerminal(node antlr.TerminalNode) {}

// VisitErrorNode is called when an error node is visited.
func (s *BaseDAGListener) VisitErrorNode(node antlr.ErrorNode) {}

// EnterEveryRule is called when any rule is entered.
func (s *BaseDAGListener) EnterEveryRule(ctx antlr.ParserRuleContext) {}

// ExitEveryRule is called when any rule is exited.
func (s *BaseDAGListener) ExitEveryRule(ctx antlr.ParserRuleContext) {}

// EnterProgram is called when production program is entered.
func (s *BaseDAGListener) EnterProgram(ctx *ProgramContext) {}

// ExitProgram is called when production program is exited.
func (s *BaseDAGListener) ExitProgram(ctx *ProgramContext) {}

// EnterImportStatement is called when production importStatement is entered.
func (s *BaseDAGListener) EnterImportStatement(ctx *ImportStatementContext) {}

// ExitImportStatement is called when production importStatement is exited.
func (s *BaseDAGListener) ExitImportStatement(ctx *ImportStatementContext) {}

// EnterDagStatement is called when production dagStatement is entered.
func (s *BaseDAGListener) EnterDagStatement(ctx *DagStatementContext) {}

// ExitDagStatement is called when production dagStatement is exited.
func (s *BaseDAGListener) ExitDagStatement(ctx *DagStatementContext) {}

// EnterParameters is called when production parameters is entered.
func (s *BaseDAGListener) EnterParameters(ctx *ParametersContext) {}

// ExitParameters is called when production parameters is exited.
func (s *BaseDAGListener) ExitParameters(ctx *ParametersContext) {}

// EnterParameter is called when production parameter is entered.
func (s *BaseDAGListener) EnterParameter(ctx *ParameterContext) {}

// ExitParameter is called when production parameter is exited.
func (s *BaseDAGListener) ExitParameter(ctx *ParameterContext) {}

// EnterNodesStatement is called when production nodesStatement is entered.
func (s *BaseDAGListener) EnterNodesStatement(ctx *NodesStatementContext) {}

// ExitNodesStatement is called when production nodesStatement is exited.
func (s *BaseDAGListener) ExitNodesStatement(ctx *NodesStatementContext) {}

// EnterNodeAssignment is called when production nodeAssignment is entered.
func (s *BaseDAGListener) EnterNodeAssignment(ctx *NodeAssignmentContext) {}

// ExitNodeAssignment is called when production nodeAssignment is exited.
func (s *BaseDAGListener) ExitNodeAssignment(ctx *NodeAssignmentContext) {}

// EnterSuccessStatement is called when production successStatement is entered.
func (s *BaseDAGListener) EnterSuccessStatement(ctx *SuccessStatementContext) {}

// ExitSuccessStatement is called when production successStatement is exited.
func (s *BaseDAGListener) ExitSuccessStatement(ctx *SuccessStatementContext) {}

// EnterErrorStatement is called when production errorStatement is entered.
func (s *BaseDAGListener) EnterErrorStatement(ctx *ErrorStatementContext) {}

// ExitErrorStatement is called when production errorStatement is exited.
func (s *BaseDAGListener) ExitErrorStatement(ctx *ErrorStatementContext) {}

// EnterAbortStatement is called when production abortStatement is entered.
func (s *BaseDAGListener) EnterAbortStatement(ctx *AbortStatementContext) {}

// ExitAbortStatement is called when production abortStatement is exited.
func (s *BaseDAGListener) ExitAbortStatement(ctx *AbortStatementContext) {}

// EnterBranchesStatement is called when production branchesStatement is entered.
func (s *BaseDAGListener) EnterBranchesStatement(ctx *BranchesStatementContext) {}

// ExitBranchesStatement is called when production branchesStatement is exited.
func (s *BaseDAGListener) ExitBranchesStatement(ctx *BranchesStatementContext) {}

// EnterEdgeStatement is called when production edgeStatement is entered.
func (s *BaseDAGListener) EnterEdgeStatement(ctx *EdgeStatementContext) {}

// ExitEdgeStatement is called when production edgeStatement is exited.
func (s *BaseDAGListener) ExitEdgeStatement(ctx *EdgeStatementContext) {}

// EnterBranchAssignment is called when production branchAssignment is entered.
func (s *BaseDAGListener) EnterBranchAssignment(ctx *BranchAssignmentContext) {}

// ExitBranchAssignment is called when production branchAssignment is exited.
func (s *BaseDAGListener) ExitBranchAssignment(ctx *BranchAssignmentContext) {}

// EnterBranchPair is called when production branchPair is entered.
func (s *BaseDAGListener) EnterBranchPair(ctx *BranchPairContext) {}

// ExitBranchPair is called when production branchPair is exited.
func (s *BaseDAGListener) ExitBranchPair(ctx *BranchPairContext) {}

// EnterStringLiteral is called when production stringLiteral is entered.
func (s *BaseDAGListener) EnterStringLiteral(ctx *StringLiteralContext) {}

// ExitStringLiteral is called when production stringLiteral is exited.
func (s *BaseDAGListener) ExitStringLiteral(ctx *StringLiteralContext) {}
