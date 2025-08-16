// Code generated from DAG.g4 by ANTLR 4.13.2. DO NOT EDIT.

package parser // DAG
import (
	"fmt"
	"strconv"
	"sync"

	"github.com/antlr4-go/antlr/v4"
)

// Suppress unused import errors
var _ = fmt.Printf
var _ = strconv.Itoa
var _ = sync.Once{}

type DAGParser struct {
	*antlr.BaseParser
}

var DAGParserStaticData struct {
	once                   sync.Once
	serializedATN          []int32
	LiteralNames           []string
	SymbolicNames          []string
	RuleNames              []string
	PredictionContextCache *antlr.PredictionContextCache
	atn                    *antlr.ATN
	decisionToDFA          []*antlr.DFA
}

func dagParserInit() {
	staticData := &DAGParserStaticData
	staticData.LiteralNames = []string{
		"", "'imports'", "'dag'", "'generates'", "'nodes'", "'success'", "'error'",
		"'abort'", "'branches'", "'end'", "':='", "'='", "'->'", "'<-'", "':'",
		"'{'", "'}'", "'['", "']'", "'('", "')'", "','",
	}
	staticData.SymbolicNames = []string{
		"", "IMPORTS", "DAG", "GENERATES", "NODES", "SUCCESS", "ERROR", "ABORT",
		"BRANCHES", "END", "COLON_ASSIGN", "ASSIGN", "RIGHT_ARROW", "LEFT_ARROW",
		"COLON", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "LPAREN", "RPAREN",
		"COMMA", "IDENT", "STRING", "WS",
	}
	staticData.RuleNames = []string{
		"program", "importStatement", "dagStatement", "parameters", "parameter",
		"nodesStatement", "nodeAssignment", "successStatement", "errorStatement",
		"abortStatement", "branchesStatement", "edgeStatement", "branchAssignment",
		"branchPair", "stringLiteral",
	}
	staticData.PredictionContextCache = antlr.NewPredictionContextCache()
	staticData.serializedATN = []int32{
		4, 1, 24, 169, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 2, 4, 7,
		4, 2, 5, 7, 5, 2, 6, 7, 6, 2, 7, 7, 7, 2, 8, 7, 8, 2, 9, 7, 9, 2, 10, 7,
		10, 2, 11, 7, 11, 2, 12, 7, 12, 2, 13, 7, 13, 2, 14, 7, 14, 1, 0, 3, 0,
		32, 8, 0, 1, 0, 5, 0, 35, 8, 0, 10, 0, 12, 0, 38, 9, 0, 1, 0, 1, 0, 1,
		1, 1, 1, 1, 1, 5, 1, 45, 8, 1, 10, 1, 12, 1, 48, 9, 1, 1, 2, 1, 2, 1, 2,
		1, 2, 1, 2, 1, 2, 1, 2, 3, 2, 57, 8, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1,
		2, 1, 2, 1, 2, 1, 2, 5, 2, 68, 8, 2, 10, 2, 12, 2, 71, 9, 2, 1, 2, 1, 2,
		1, 3, 1, 3, 1, 3, 5, 3, 78, 8, 3, 10, 3, 12, 3, 81, 9, 3, 1, 4, 1, 4, 1,
		4, 5, 4, 86, 8, 4, 10, 4, 12, 4, 89, 9, 4, 1, 4, 1, 4, 1, 5, 1, 5, 1, 5,
		5, 5, 96, 8, 5, 10, 5, 12, 5, 99, 9, 5, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 3,
		6, 106, 8, 6, 1, 6, 1, 6, 1, 7, 1, 7, 1, 7, 5, 7, 113, 8, 7, 10, 7, 12,
		7, 116, 9, 7, 1, 8, 1, 8, 1, 8, 5, 8, 121, 8, 8, 10, 8, 12, 8, 124, 9,
		8, 1, 9, 1, 9, 1, 9, 5, 9, 129, 8, 9, 10, 9, 12, 9, 132, 9, 9, 1, 10, 1,
		10, 1, 10, 5, 10, 137, 8, 10, 10, 10, 12, 10, 140, 9, 10, 1, 11, 1, 11,
		1, 11, 5, 11, 145, 8, 11, 10, 11, 12, 11, 148, 9, 11, 1, 12, 1, 12, 1,
		12, 1, 12, 1, 12, 1, 12, 5, 12, 156, 8, 12, 10, 12, 12, 12, 159, 9, 12,
		1, 12, 1, 12, 1, 13, 1, 13, 1, 13, 1, 13, 1, 14, 1, 14, 1, 14, 0, 0, 15,
		0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 0, 2, 2, 0, 9, 9,
		22, 22, 1, 0, 12, 13, 171, 0, 31, 1, 0, 0, 0, 2, 41, 1, 0, 0, 0, 4, 49,
		1, 0, 0, 0, 6, 74, 1, 0, 0, 0, 8, 82, 1, 0, 0, 0, 10, 92, 1, 0, 0, 0, 12,
		100, 1, 0, 0, 0, 14, 109, 1, 0, 0, 0, 16, 117, 1, 0, 0, 0, 18, 125, 1,
		0, 0, 0, 20, 133, 1, 0, 0, 0, 22, 141, 1, 0, 0, 0, 24, 149, 1, 0, 0, 0,
		26, 162, 1, 0, 0, 0, 28, 166, 1, 0, 0, 0, 30, 32, 3, 2, 1, 0, 31, 30, 1,
		0, 0, 0, 31, 32, 1, 0, 0, 0, 32, 36, 1, 0, 0, 0, 33, 35, 3, 4, 2, 0, 34,
		33, 1, 0, 0, 0, 35, 38, 1, 0, 0, 0, 36, 34, 1, 0, 0, 0, 36, 37, 1, 0, 0,
		0, 37, 39, 1, 0, 0, 0, 38, 36, 1, 0, 0, 0, 39, 40, 5, 0, 0, 1, 40, 1, 1,
		0, 0, 0, 41, 42, 5, 1, 0, 0, 42, 46, 5, 14, 0, 0, 43, 45, 3, 28, 14, 0,
		44, 43, 1, 0, 0, 0, 45, 48, 1, 0, 0, 0, 46, 44, 1, 0, 0, 0, 46, 47, 1,
		0, 0, 0, 47, 3, 1, 0, 0, 0, 48, 46, 1, 0, 0, 0, 49, 50, 5, 2, 0, 0, 50,
		51, 5, 17, 0, 0, 51, 52, 5, 22, 0, 0, 52, 53, 5, 18, 0, 0, 53, 54, 5, 22,
		0, 0, 54, 56, 5, 19, 0, 0, 55, 57, 3, 6, 3, 0, 56, 55, 1, 0, 0, 0, 56,
		57, 1, 0, 0, 0, 57, 58, 1, 0, 0, 0, 58, 59, 5, 20, 0, 0, 59, 60, 5, 3,
		0, 0, 60, 61, 5, 22, 0, 0, 61, 62, 5, 15, 0, 0, 62, 69, 3, 10, 5, 0, 63,
		68, 3, 14, 7, 0, 64, 68, 3, 16, 8, 0, 65, 68, 3, 18, 9, 0, 66, 68, 3, 20,
		10, 0, 67, 63, 1, 0, 0, 0, 67, 64, 1, 0, 0, 0, 67, 65, 1, 0, 0, 0, 67,
		66, 1, 0, 0, 0, 68, 71, 1, 0, 0, 0, 69, 67, 1, 0, 0, 0, 69, 70, 1, 0, 0,
		0, 70, 72, 1, 0, 0, 0, 71, 69, 1, 0, 0, 0, 72, 73, 5, 16, 0, 0, 73, 5,
		1, 0, 0, 0, 74, 79, 3, 8, 4, 0, 75, 76, 5, 21, 0, 0, 76, 78, 3, 8, 4, 0,
		77, 75, 1, 0, 0, 0, 78, 81, 1, 0, 0, 0, 79, 77, 1, 0, 0, 0, 79, 80, 1,
		0, 0, 0, 80, 7, 1, 0, 0, 0, 81, 79, 1, 0, 0, 0, 82, 87, 5, 22, 0, 0, 83,
		84, 5, 21, 0, 0, 84, 86, 5, 22, 0, 0, 85, 83, 1, 0, 0, 0, 86, 89, 1, 0,
		0, 0, 87, 85, 1, 0, 0, 0, 87, 88, 1, 0, 0, 0, 88, 90, 1, 0, 0, 0, 89, 87,
		1, 0, 0, 0, 90, 91, 5, 22, 0, 0, 91, 9, 1, 0, 0, 0, 92, 93, 5, 4, 0, 0,
		93, 97, 5, 14, 0, 0, 94, 96, 3, 12, 6, 0, 95, 94, 1, 0, 0, 0, 96, 99, 1,
		0, 0, 0, 97, 95, 1, 0, 0, 0, 97, 98, 1, 0, 0, 0, 98, 11, 1, 0, 0, 0, 99,
		97, 1, 0, 0, 0, 100, 101, 5, 22, 0, 0, 101, 102, 5, 10, 0, 0, 102, 103,
		5, 22, 0, 0, 103, 105, 5, 19, 0, 0, 104, 106, 3, 6, 3, 0, 105, 104, 1,
		0, 0, 0, 105, 106, 1, 0, 0, 0, 106, 107, 1, 0, 0, 0, 107, 108, 5, 20, 0,
		0, 108, 13, 1, 0, 0, 0, 109, 110, 5, 5, 0, 0, 110, 114, 5, 14, 0, 0, 111,
		113, 3, 22, 11, 0, 112, 111, 1, 0, 0, 0, 113, 116, 1, 0, 0, 0, 114, 112,
		1, 0, 0, 0, 114, 115, 1, 0, 0, 0, 115, 15, 1, 0, 0, 0, 116, 114, 1, 0,
		0, 0, 117, 118, 5, 6, 0, 0, 118, 122, 5, 14, 0, 0, 119, 121, 3, 22, 11,
		0, 120, 119, 1, 0, 0, 0, 121, 124, 1, 0, 0, 0, 122, 120, 1, 0, 0, 0, 122,
		123, 1, 0, 0, 0, 123, 17, 1, 0, 0, 0, 124, 122, 1, 0, 0, 0, 125, 126, 5,
		7, 0, 0, 126, 130, 5, 14, 0, 0, 127, 129, 3, 22, 11, 0, 128, 127, 1, 0,
		0, 0, 129, 132, 1, 0, 0, 0, 130, 128, 1, 0, 0, 0, 130, 131, 1, 0, 0, 0,
		131, 19, 1, 0, 0, 0, 132, 130, 1, 0, 0, 0, 133, 134, 5, 8, 0, 0, 134, 138,
		5, 14, 0, 0, 135, 137, 3, 24, 12, 0, 136, 135, 1, 0, 0, 0, 137, 140, 1,
		0, 0, 0, 138, 136, 1, 0, 0, 0, 138, 139, 1, 0, 0, 0, 139, 21, 1, 0, 0,
		0, 140, 138, 1, 0, 0, 0, 141, 146, 7, 0, 0, 0, 142, 143, 7, 1, 0, 0, 143,
		145, 3, 22, 11, 0, 144, 142, 1, 0, 0, 0, 145, 148, 1, 0, 0, 0, 146, 144,
		1, 0, 0, 0, 146, 147, 1, 0, 0, 0, 147, 23, 1, 0, 0, 0, 148, 146, 1, 0,
		0, 0, 149, 150, 5, 22, 0, 0, 150, 151, 5, 11, 0, 0, 151, 152, 5, 15, 0,
		0, 152, 157, 3, 26, 13, 0, 153, 154, 5, 21, 0, 0, 154, 156, 3, 26, 13,
		0, 155, 153, 1, 0, 0, 0, 156, 159, 1, 0, 0, 0, 157, 155, 1, 0, 0, 0, 157,
		158, 1, 0, 0, 0, 158, 160, 1, 0, 0, 0, 159, 157, 1, 0, 0, 0, 160, 161,
		5, 16, 0, 0, 161, 25, 1, 0, 0, 0, 162, 163, 3, 28, 14, 0, 163, 164, 5,
		14, 0, 0, 164, 165, 5, 22, 0, 0, 165, 27, 1, 0, 0, 0, 166, 167, 5, 23,
		0, 0, 167, 29, 1, 0, 0, 0, 16, 31, 36, 46, 56, 67, 69, 79, 87, 97, 105,
		114, 122, 130, 138, 146, 157,
	}
	deserializer := antlr.NewATNDeserializer(nil)
	staticData.atn = deserializer.Deserialize(staticData.serializedATN)
	atn := staticData.atn
	staticData.decisionToDFA = make([]*antlr.DFA, len(atn.DecisionToState))
	decisionToDFA := staticData.decisionToDFA
	for index, state := range atn.DecisionToState {
		decisionToDFA[index] = antlr.NewDFA(state, index)
	}
}

// DAGParserInit initializes any static state used to implement DAGParser. By default the
// static state used to implement the parser is lazily initialized during the first call to
// NewDAGParser(). You can call this function if you wish to initialize the static state ahead
// of time.
func DAGParserInit() {
	staticData := &DAGParserStaticData
	staticData.once.Do(dagParserInit)
}

// NewDAGParser produces a new parser instance for the optional input antlr.TokenStream.
func NewDAGParser(input antlr.TokenStream) *DAGParser {
	DAGParserInit()
	this := new(DAGParser)
	this.BaseParser = antlr.NewBaseParser(input)
	staticData := &DAGParserStaticData
	this.Interpreter = antlr.NewParserATNSimulator(this, staticData.atn, staticData.decisionToDFA, staticData.PredictionContextCache)
	this.RuleNames = staticData.RuleNames
	this.LiteralNames = staticData.LiteralNames
	this.SymbolicNames = staticData.SymbolicNames
	this.GrammarFileName = "DAG.g4"

	return this
}

// DAGParser tokens.
const (
	DAGParserEOF          = antlr.TokenEOF
	DAGParserIMPORTS      = 1
	DAGParserDAG          = 2
	DAGParserGENERATES    = 3
	DAGParserNODES        = 4
	DAGParserSUCCESS      = 5
	DAGParserERROR        = 6
	DAGParserABORT        = 7
	DAGParserBRANCHES     = 8
	DAGParserEND          = 9
	DAGParserCOLON_ASSIGN = 10
	DAGParserASSIGN       = 11
	DAGParserRIGHT_ARROW  = 12
	DAGParserLEFT_ARROW   = 13
	DAGParserCOLON        = 14
	DAGParserLBRACE       = 15
	DAGParserRBRACE       = 16
	DAGParserLBRACKET     = 17
	DAGParserRBRACKET     = 18
	DAGParserLPAREN       = 19
	DAGParserRPAREN       = 20
	DAGParserCOMMA        = 21
	DAGParserIDENT        = 22
	DAGParserSTRING       = 23
	DAGParserWS           = 24
)

// DAGParser rules.
const (
	DAGParserRULE_program           = 0
	DAGParserRULE_importStatement   = 1
	DAGParserRULE_dagStatement      = 2
	DAGParserRULE_parameters        = 3
	DAGParserRULE_parameter         = 4
	DAGParserRULE_nodesStatement    = 5
	DAGParserRULE_nodeAssignment    = 6
	DAGParserRULE_successStatement  = 7
	DAGParserRULE_errorStatement    = 8
	DAGParserRULE_abortStatement    = 9
	DAGParserRULE_branchesStatement = 10
	DAGParserRULE_edgeStatement     = 11
	DAGParserRULE_branchAssignment  = 12
	DAGParserRULE_branchPair        = 13
	DAGParserRULE_stringLiteral     = 14
)

// IProgramContext is an interface to support dynamic dispatch.
type IProgramContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	EOF() antlr.TerminalNode
	ImportStatement() IImportStatementContext
	AllDagStatement() []IDagStatementContext
	DagStatement(i int) IDagStatementContext

	// IsProgramContext differentiates from other interfaces.
	IsProgramContext()
}

type ProgramContext struct {
	antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyProgramContext() *ProgramContext {
	var p = new(ProgramContext)
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_program
	return p
}

func InitEmptyProgramContext(p *ProgramContext) {
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_program
}

func (*ProgramContext) IsProgramContext() {}

func NewProgramContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *ProgramContext {
	var p = new(ProgramContext)

	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, parent, invokingState)

	p.parser = parser
	p.RuleIndex = DAGParserRULE_program

	return p
}

func (s *ProgramContext) GetParser() antlr.Parser { return s.parser }

func (s *ProgramContext) EOF() antlr.TerminalNode {
	return s.GetToken(DAGParserEOF, 0)
}

func (s *ProgramContext) ImportStatement() IImportStatementContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IImportStatementContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IImportStatementContext)
}

func (s *ProgramContext) AllDagStatement() []IDagStatementContext {
	children := s.GetChildren()
	len := 0
	for _, ctx := range children {
		if _, ok := ctx.(IDagStatementContext); ok {
			len++
		}
	}

	tst := make([]IDagStatementContext, len)
	i := 0
	for _, ctx := range children {
		if t, ok := ctx.(IDagStatementContext); ok {
			tst[i] = t.(IDagStatementContext)
			i++
		}
	}

	return tst
}

func (s *ProgramContext) DagStatement(i int) IDagStatementContext {
	var t antlr.RuleContext
	j := 0
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IDagStatementContext); ok {
			if j == i {
				t = ctx.(antlr.RuleContext)
				break
			}
			j++
		}
	}

	if t == nil {
		return nil
	}

	return t.(IDagStatementContext)
}

func (s *ProgramContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *ProgramContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *ProgramContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.EnterProgram(s)
	}
}

func (s *ProgramContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.ExitProgram(s)
	}
}

func (s *ProgramContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case DAGVisitor:
		return t.VisitProgram(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *DAGParser) Program() (localctx IProgramContext) {
	localctx = NewProgramContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 0, DAGParserRULE_program)
	var _la int

	p.EnterOuterAlt(localctx, 1)
	p.SetState(31)
	p.GetErrorHandler().Sync(p)
	if p.HasError() {
		goto errorExit
	}
	_la = p.GetTokenStream().LA(1)

	if _la == DAGParserIMPORTS {
		{
			p.SetState(30)
			p.ImportStatement()
		}

	}
	p.SetState(36)
	p.GetErrorHandler().Sync(p)
	if p.HasError() {
		goto errorExit
	}
	_la = p.GetTokenStream().LA(1)

	for _la == DAGParserDAG {
		{
			p.SetState(33)
			p.DagStatement()
		}

		p.SetState(38)
		p.GetErrorHandler().Sync(p)
		if p.HasError() {
			goto errorExit
		}
		_la = p.GetTokenStream().LA(1)
	}
	{
		p.SetState(39)
		p.Match(DAGParserEOF)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}

errorExit:
	if p.HasError() {
		v := p.GetError()
		localctx.SetException(v)
		p.GetErrorHandler().ReportError(p, v)
		p.GetErrorHandler().Recover(p, v)
		p.SetError(nil)
	}
	p.ExitRule()
	return localctx
	goto errorExit // Trick to prevent compiler error if the label is not used
}

// IImportStatementContext is an interface to support dynamic dispatch.
type IImportStatementContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	IMPORTS() antlr.TerminalNode
	COLON() antlr.TerminalNode
	AllStringLiteral() []IStringLiteralContext
	StringLiteral(i int) IStringLiteralContext

	// IsImportStatementContext differentiates from other interfaces.
	IsImportStatementContext()
}

type ImportStatementContext struct {
	antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyImportStatementContext() *ImportStatementContext {
	var p = new(ImportStatementContext)
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_importStatement
	return p
}

func InitEmptyImportStatementContext(p *ImportStatementContext) {
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_importStatement
}

func (*ImportStatementContext) IsImportStatementContext() {}

func NewImportStatementContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *ImportStatementContext {
	var p = new(ImportStatementContext)

	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, parent, invokingState)

	p.parser = parser
	p.RuleIndex = DAGParserRULE_importStatement

	return p
}

func (s *ImportStatementContext) GetParser() antlr.Parser { return s.parser }

func (s *ImportStatementContext) IMPORTS() antlr.TerminalNode {
	return s.GetToken(DAGParserIMPORTS, 0)
}

func (s *ImportStatementContext) COLON() antlr.TerminalNode {
	return s.GetToken(DAGParserCOLON, 0)
}

func (s *ImportStatementContext) AllStringLiteral() []IStringLiteralContext {
	children := s.GetChildren()
	len := 0
	for _, ctx := range children {
		if _, ok := ctx.(IStringLiteralContext); ok {
			len++
		}
	}

	tst := make([]IStringLiteralContext, len)
	i := 0
	for _, ctx := range children {
		if t, ok := ctx.(IStringLiteralContext); ok {
			tst[i] = t.(IStringLiteralContext)
			i++
		}
	}

	return tst
}

func (s *ImportStatementContext) StringLiteral(i int) IStringLiteralContext {
	var t antlr.RuleContext
	j := 0
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IStringLiteralContext); ok {
			if j == i {
				t = ctx.(antlr.RuleContext)
				break
			}
			j++
		}
	}

	if t == nil {
		return nil
	}

	return t.(IStringLiteralContext)
}

func (s *ImportStatementContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *ImportStatementContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *ImportStatementContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.EnterImportStatement(s)
	}
}

func (s *ImportStatementContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.ExitImportStatement(s)
	}
}

func (s *ImportStatementContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case DAGVisitor:
		return t.VisitImportStatement(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *DAGParser) ImportStatement() (localctx IImportStatementContext) {
	localctx = NewImportStatementContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 2, DAGParserRULE_importStatement)
	var _la int

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(41)
		p.Match(DAGParserIMPORTS)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	{
		p.SetState(42)
		p.Match(DAGParserCOLON)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	p.SetState(46)
	p.GetErrorHandler().Sync(p)
	if p.HasError() {
		goto errorExit
	}
	_la = p.GetTokenStream().LA(1)

	for _la == DAGParserSTRING {
		{
			p.SetState(43)
			p.StringLiteral()
		}

		p.SetState(48)
		p.GetErrorHandler().Sync(p)
		if p.HasError() {
			goto errorExit
		}
		_la = p.GetTokenStream().LA(1)
	}

errorExit:
	if p.HasError() {
		v := p.GetError()
		localctx.SetException(v)
		p.GetErrorHandler().ReportError(p, v)
		p.GetErrorHandler().Recover(p, v)
		p.SetError(nil)
	}
	p.ExitRule()
	return localctx
	goto errorExit // Trick to prevent compiler error if the label is not used
}

// IDagStatementContext is an interface to support dynamic dispatch.
type IDagStatementContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// GetTyp returns the typ token.
	GetTyp() antlr.Token

	// GetName returns the name token.
	GetName() antlr.Token

	// GetGenerates returns the generates token.
	GetGenerates() antlr.Token

	// SetTyp sets the typ token.
	SetTyp(antlr.Token)

	// SetName sets the name token.
	SetName(antlr.Token)

	// SetGenerates sets the generates token.
	SetGenerates(antlr.Token)

	// Getter signatures
	DAG() antlr.TerminalNode
	LBRACKET() antlr.TerminalNode
	RBRACKET() antlr.TerminalNode
	LPAREN() antlr.TerminalNode
	RPAREN() antlr.TerminalNode
	GENERATES() antlr.TerminalNode
	LBRACE() antlr.TerminalNode
	NodesStatement() INodesStatementContext
	RBRACE() antlr.TerminalNode
	AllIDENT() []antlr.TerminalNode
	IDENT(i int) antlr.TerminalNode
	Parameters() IParametersContext
	AllSuccessStatement() []ISuccessStatementContext
	SuccessStatement(i int) ISuccessStatementContext
	AllErrorStatement() []IErrorStatementContext
	ErrorStatement(i int) IErrorStatementContext
	AllAbortStatement() []IAbortStatementContext
	AbortStatement(i int) IAbortStatementContext
	AllBranchesStatement() []IBranchesStatementContext
	BranchesStatement(i int) IBranchesStatementContext

	// IsDagStatementContext differentiates from other interfaces.
	IsDagStatementContext()
}

type DagStatementContext struct {
	antlr.BaseParserRuleContext
	parser    antlr.Parser
	typ       antlr.Token
	name      antlr.Token
	generates antlr.Token
}

func NewEmptyDagStatementContext() *DagStatementContext {
	var p = new(DagStatementContext)
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_dagStatement
	return p
}

func InitEmptyDagStatementContext(p *DagStatementContext) {
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_dagStatement
}

func (*DagStatementContext) IsDagStatementContext() {}

func NewDagStatementContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *DagStatementContext {
	var p = new(DagStatementContext)

	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, parent, invokingState)

	p.parser = parser
	p.RuleIndex = DAGParserRULE_dagStatement

	return p
}

func (s *DagStatementContext) GetParser() antlr.Parser { return s.parser }

func (s *DagStatementContext) GetTyp() antlr.Token { return s.typ }

func (s *DagStatementContext) GetName() antlr.Token { return s.name }

func (s *DagStatementContext) GetGenerates() antlr.Token { return s.generates }

func (s *DagStatementContext) SetTyp(v antlr.Token) { s.typ = v }

func (s *DagStatementContext) SetName(v antlr.Token) { s.name = v }

func (s *DagStatementContext) SetGenerates(v antlr.Token) { s.generates = v }

func (s *DagStatementContext) DAG() antlr.TerminalNode {
	return s.GetToken(DAGParserDAG, 0)
}

func (s *DagStatementContext) LBRACKET() antlr.TerminalNode {
	return s.GetToken(DAGParserLBRACKET, 0)
}

func (s *DagStatementContext) RBRACKET() antlr.TerminalNode {
	return s.GetToken(DAGParserRBRACKET, 0)
}

func (s *DagStatementContext) LPAREN() antlr.TerminalNode {
	return s.GetToken(DAGParserLPAREN, 0)
}

func (s *DagStatementContext) RPAREN() antlr.TerminalNode {
	return s.GetToken(DAGParserRPAREN, 0)
}

func (s *DagStatementContext) GENERATES() antlr.TerminalNode {
	return s.GetToken(DAGParserGENERATES, 0)
}

func (s *DagStatementContext) LBRACE() antlr.TerminalNode {
	return s.GetToken(DAGParserLBRACE, 0)
}

func (s *DagStatementContext) NodesStatement() INodesStatementContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(INodesStatementContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(INodesStatementContext)
}

func (s *DagStatementContext) RBRACE() antlr.TerminalNode {
	return s.GetToken(DAGParserRBRACE, 0)
}

func (s *DagStatementContext) AllIDENT() []antlr.TerminalNode {
	return s.GetTokens(DAGParserIDENT)
}

func (s *DagStatementContext) IDENT(i int) antlr.TerminalNode {
	return s.GetToken(DAGParserIDENT, i)
}

func (s *DagStatementContext) Parameters() IParametersContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IParametersContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IParametersContext)
}

func (s *DagStatementContext) AllSuccessStatement() []ISuccessStatementContext {
	children := s.GetChildren()
	len := 0
	for _, ctx := range children {
		if _, ok := ctx.(ISuccessStatementContext); ok {
			len++
		}
	}

	tst := make([]ISuccessStatementContext, len)
	i := 0
	for _, ctx := range children {
		if t, ok := ctx.(ISuccessStatementContext); ok {
			tst[i] = t.(ISuccessStatementContext)
			i++
		}
	}

	return tst
}

func (s *DagStatementContext) SuccessStatement(i int) ISuccessStatementContext {
	var t antlr.RuleContext
	j := 0
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(ISuccessStatementContext); ok {
			if j == i {
				t = ctx.(antlr.RuleContext)
				break
			}
			j++
		}
	}

	if t == nil {
		return nil
	}

	return t.(ISuccessStatementContext)
}

func (s *DagStatementContext) AllErrorStatement() []IErrorStatementContext {
	children := s.GetChildren()
	len := 0
	for _, ctx := range children {
		if _, ok := ctx.(IErrorStatementContext); ok {
			len++
		}
	}

	tst := make([]IErrorStatementContext, len)
	i := 0
	for _, ctx := range children {
		if t, ok := ctx.(IErrorStatementContext); ok {
			tst[i] = t.(IErrorStatementContext)
			i++
		}
	}

	return tst
}

func (s *DagStatementContext) ErrorStatement(i int) IErrorStatementContext {
	var t antlr.RuleContext
	j := 0
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IErrorStatementContext); ok {
			if j == i {
				t = ctx.(antlr.RuleContext)
				break
			}
			j++
		}
	}

	if t == nil {
		return nil
	}

	return t.(IErrorStatementContext)
}

func (s *DagStatementContext) AllAbortStatement() []IAbortStatementContext {
	children := s.GetChildren()
	len := 0
	for _, ctx := range children {
		if _, ok := ctx.(IAbortStatementContext); ok {
			len++
		}
	}

	tst := make([]IAbortStatementContext, len)
	i := 0
	for _, ctx := range children {
		if t, ok := ctx.(IAbortStatementContext); ok {
			tst[i] = t.(IAbortStatementContext)
			i++
		}
	}

	return tst
}

func (s *DagStatementContext) AbortStatement(i int) IAbortStatementContext {
	var t antlr.RuleContext
	j := 0
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IAbortStatementContext); ok {
			if j == i {
				t = ctx.(antlr.RuleContext)
				break
			}
			j++
		}
	}

	if t == nil {
		return nil
	}

	return t.(IAbortStatementContext)
}

func (s *DagStatementContext) AllBranchesStatement() []IBranchesStatementContext {
	children := s.GetChildren()
	len := 0
	for _, ctx := range children {
		if _, ok := ctx.(IBranchesStatementContext); ok {
			len++
		}
	}

	tst := make([]IBranchesStatementContext, len)
	i := 0
	for _, ctx := range children {
		if t, ok := ctx.(IBranchesStatementContext); ok {
			tst[i] = t.(IBranchesStatementContext)
			i++
		}
	}

	return tst
}

func (s *DagStatementContext) BranchesStatement(i int) IBranchesStatementContext {
	var t antlr.RuleContext
	j := 0
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IBranchesStatementContext); ok {
			if j == i {
				t = ctx.(antlr.RuleContext)
				break
			}
			j++
		}
	}

	if t == nil {
		return nil
	}

	return t.(IBranchesStatementContext)
}

func (s *DagStatementContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *DagStatementContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *DagStatementContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.EnterDagStatement(s)
	}
}

func (s *DagStatementContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.ExitDagStatement(s)
	}
}

func (s *DagStatementContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case DAGVisitor:
		return t.VisitDagStatement(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *DAGParser) DagStatement() (localctx IDagStatementContext) {
	localctx = NewDagStatementContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 4, DAGParserRULE_dagStatement)
	var _la int

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(49)
		p.Match(DAGParserDAG)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	{
		p.SetState(50)
		p.Match(DAGParserLBRACKET)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	{
		p.SetState(51)

		var _m = p.Match(DAGParserIDENT)

		localctx.(*DagStatementContext).typ = _m
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	{
		p.SetState(52)
		p.Match(DAGParserRBRACKET)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	{
		p.SetState(53)

		var _m = p.Match(DAGParserIDENT)

		localctx.(*DagStatementContext).name = _m
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	{
		p.SetState(54)
		p.Match(DAGParserLPAREN)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	p.SetState(56)
	p.GetErrorHandler().Sync(p)
	if p.HasError() {
		goto errorExit
	}
	_la = p.GetTokenStream().LA(1)

	if _la == DAGParserIDENT {
		{
			p.SetState(55)
			p.Parameters()
		}

	}
	{
		p.SetState(58)
		p.Match(DAGParserRPAREN)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	{
		p.SetState(59)
		p.Match(DAGParserGENERATES)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	{
		p.SetState(60)

		var _m = p.Match(DAGParserIDENT)

		localctx.(*DagStatementContext).generates = _m
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	{
		p.SetState(61)
		p.Match(DAGParserLBRACE)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	{
		p.SetState(62)
		p.NodesStatement()
	}
	p.SetState(69)
	p.GetErrorHandler().Sync(p)
	if p.HasError() {
		goto errorExit
	}
	_la = p.GetTokenStream().LA(1)

	for (int64(_la) & ^0x3f) == 0 && ((int64(1)<<_la)&480) != 0 {
		p.SetState(67)
		p.GetErrorHandler().Sync(p)
		if p.HasError() {
			goto errorExit
		}

		switch p.GetTokenStream().LA(1) {
		case DAGParserSUCCESS:
			{
				p.SetState(63)
				p.SuccessStatement()
			}

		case DAGParserERROR:
			{
				p.SetState(64)
				p.ErrorStatement()
			}

		case DAGParserABORT:
			{
				p.SetState(65)
				p.AbortStatement()
			}

		case DAGParserBRANCHES:
			{
				p.SetState(66)
				p.BranchesStatement()
			}

		default:
			p.SetError(antlr.NewNoViableAltException(p, nil, nil, nil, nil, nil))
			goto errorExit
		}

		p.SetState(71)
		p.GetErrorHandler().Sync(p)
		if p.HasError() {
			goto errorExit
		}
		_la = p.GetTokenStream().LA(1)
	}
	{
		p.SetState(72)
		p.Match(DAGParserRBRACE)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}

errorExit:
	if p.HasError() {
		v := p.GetError()
		localctx.SetException(v)
		p.GetErrorHandler().ReportError(p, v)
		p.GetErrorHandler().Recover(p, v)
		p.SetError(nil)
	}
	p.ExitRule()
	return localctx
	goto errorExit // Trick to prevent compiler error if the label is not used
}

// IParametersContext is an interface to support dynamic dispatch.
type IParametersContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	AllParameter() []IParameterContext
	Parameter(i int) IParameterContext
	AllCOMMA() []antlr.TerminalNode
	COMMA(i int) antlr.TerminalNode

	// IsParametersContext differentiates from other interfaces.
	IsParametersContext()
}

type ParametersContext struct {
	antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyParametersContext() *ParametersContext {
	var p = new(ParametersContext)
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_parameters
	return p
}

func InitEmptyParametersContext(p *ParametersContext) {
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_parameters
}

func (*ParametersContext) IsParametersContext() {}

func NewParametersContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *ParametersContext {
	var p = new(ParametersContext)

	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, parent, invokingState)

	p.parser = parser
	p.RuleIndex = DAGParserRULE_parameters

	return p
}

func (s *ParametersContext) GetParser() antlr.Parser { return s.parser }

func (s *ParametersContext) AllParameter() []IParameterContext {
	children := s.GetChildren()
	len := 0
	for _, ctx := range children {
		if _, ok := ctx.(IParameterContext); ok {
			len++
		}
	}

	tst := make([]IParameterContext, len)
	i := 0
	for _, ctx := range children {
		if t, ok := ctx.(IParameterContext); ok {
			tst[i] = t.(IParameterContext)
			i++
		}
	}

	return tst
}

func (s *ParametersContext) Parameter(i int) IParameterContext {
	var t antlr.RuleContext
	j := 0
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IParameterContext); ok {
			if j == i {
				t = ctx.(antlr.RuleContext)
				break
			}
			j++
		}
	}

	if t == nil {
		return nil
	}

	return t.(IParameterContext)
}

func (s *ParametersContext) AllCOMMA() []antlr.TerminalNode {
	return s.GetTokens(DAGParserCOMMA)
}

func (s *ParametersContext) COMMA(i int) antlr.TerminalNode {
	return s.GetToken(DAGParserCOMMA, i)
}

func (s *ParametersContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *ParametersContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *ParametersContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.EnterParameters(s)
	}
}

func (s *ParametersContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.ExitParameters(s)
	}
}

func (s *ParametersContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case DAGVisitor:
		return t.VisitParameters(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *DAGParser) Parameters() (localctx IParametersContext) {
	localctx = NewParametersContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 6, DAGParserRULE_parameters)
	var _la int

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(74)
		p.Parameter()
	}
	p.SetState(79)
	p.GetErrorHandler().Sync(p)
	if p.HasError() {
		goto errorExit
	}
	_la = p.GetTokenStream().LA(1)

	for _la == DAGParserCOMMA {
		{
			p.SetState(75)
			p.Match(DAGParserCOMMA)
			if p.HasError() {
				// Recognition error - abort rule
				goto errorExit
			}
		}
		{
			p.SetState(76)
			p.Parameter()
		}

		p.SetState(81)
		p.GetErrorHandler().Sync(p)
		if p.HasError() {
			goto errorExit
		}
		_la = p.GetTokenStream().LA(1)
	}

errorExit:
	if p.HasError() {
		v := p.GetError()
		localctx.SetException(v)
		p.GetErrorHandler().ReportError(p, v)
		p.GetErrorHandler().Recover(p, v)
		p.SetError(nil)
	}
	p.ExitRule()
	return localctx
	goto errorExit // Trick to prevent compiler error if the label is not used
}

// IParameterContext is an interface to support dynamic dispatch.
type IParameterContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// GetName returns the name token.
	GetName() antlr.Token

	// GetTyp returns the typ token.
	GetTyp() antlr.Token

	// SetName sets the name token.
	SetName(antlr.Token)

	// SetTyp sets the typ token.
	SetTyp(antlr.Token)

	// Getter signatures
	AllIDENT() []antlr.TerminalNode
	IDENT(i int) antlr.TerminalNode
	AllCOMMA() []antlr.TerminalNode
	COMMA(i int) antlr.TerminalNode

	// IsParameterContext differentiates from other interfaces.
	IsParameterContext()
}

type ParameterContext struct {
	antlr.BaseParserRuleContext
	parser antlr.Parser
	name   antlr.Token
	typ    antlr.Token
}

func NewEmptyParameterContext() *ParameterContext {
	var p = new(ParameterContext)
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_parameter
	return p
}

func InitEmptyParameterContext(p *ParameterContext) {
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_parameter
}

func (*ParameterContext) IsParameterContext() {}

func NewParameterContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *ParameterContext {
	var p = new(ParameterContext)

	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, parent, invokingState)

	p.parser = parser
	p.RuleIndex = DAGParserRULE_parameter

	return p
}

func (s *ParameterContext) GetParser() antlr.Parser { return s.parser }

func (s *ParameterContext) GetName() antlr.Token { return s.name }

func (s *ParameterContext) GetTyp() antlr.Token { return s.typ }

func (s *ParameterContext) SetName(v antlr.Token) { s.name = v }

func (s *ParameterContext) SetTyp(v antlr.Token) { s.typ = v }

func (s *ParameterContext) AllIDENT() []antlr.TerminalNode {
	return s.GetTokens(DAGParserIDENT)
}

func (s *ParameterContext) IDENT(i int) antlr.TerminalNode {
	return s.GetToken(DAGParserIDENT, i)
}

func (s *ParameterContext) AllCOMMA() []antlr.TerminalNode {
	return s.GetTokens(DAGParserCOMMA)
}

func (s *ParameterContext) COMMA(i int) antlr.TerminalNode {
	return s.GetToken(DAGParserCOMMA, i)
}

func (s *ParameterContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *ParameterContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *ParameterContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.EnterParameter(s)
	}
}

func (s *ParameterContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.ExitParameter(s)
	}
}

func (s *ParameterContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case DAGVisitor:
		return t.VisitParameter(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *DAGParser) Parameter() (localctx IParameterContext) {
	localctx = NewParameterContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 8, DAGParserRULE_parameter)
	var _la int

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(82)

		var _m = p.Match(DAGParserIDENT)

		localctx.(*ParameterContext).name = _m
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	p.SetState(87)
	p.GetErrorHandler().Sync(p)
	if p.HasError() {
		goto errorExit
	}
	_la = p.GetTokenStream().LA(1)

	for _la == DAGParserCOMMA {
		{
			p.SetState(83)
			p.Match(DAGParserCOMMA)
			if p.HasError() {
				// Recognition error - abort rule
				goto errorExit
			}
		}
		{
			p.SetState(84)

			var _m = p.Match(DAGParserIDENT)

			localctx.(*ParameterContext).name = _m
			if p.HasError() {
				// Recognition error - abort rule
				goto errorExit
			}
		}

		p.SetState(89)
		p.GetErrorHandler().Sync(p)
		if p.HasError() {
			goto errorExit
		}
		_la = p.GetTokenStream().LA(1)
	}
	{
		p.SetState(90)

		var _m = p.Match(DAGParserIDENT)

		localctx.(*ParameterContext).typ = _m
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}

errorExit:
	if p.HasError() {
		v := p.GetError()
		localctx.SetException(v)
		p.GetErrorHandler().ReportError(p, v)
		p.GetErrorHandler().Recover(p, v)
		p.SetError(nil)
	}
	p.ExitRule()
	return localctx
	goto errorExit // Trick to prevent compiler error if the label is not used
}

// INodesStatementContext is an interface to support dynamic dispatch.
type INodesStatementContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	NODES() antlr.TerminalNode
	COLON() antlr.TerminalNode
	AllNodeAssignment() []INodeAssignmentContext
	NodeAssignment(i int) INodeAssignmentContext

	// IsNodesStatementContext differentiates from other interfaces.
	IsNodesStatementContext()
}

type NodesStatementContext struct {
	antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyNodesStatementContext() *NodesStatementContext {
	var p = new(NodesStatementContext)
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_nodesStatement
	return p
}

func InitEmptyNodesStatementContext(p *NodesStatementContext) {
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_nodesStatement
}

func (*NodesStatementContext) IsNodesStatementContext() {}

func NewNodesStatementContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *NodesStatementContext {
	var p = new(NodesStatementContext)

	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, parent, invokingState)

	p.parser = parser
	p.RuleIndex = DAGParserRULE_nodesStatement

	return p
}

func (s *NodesStatementContext) GetParser() antlr.Parser { return s.parser }

func (s *NodesStatementContext) NODES() antlr.TerminalNode {
	return s.GetToken(DAGParserNODES, 0)
}

func (s *NodesStatementContext) COLON() antlr.TerminalNode {
	return s.GetToken(DAGParserCOLON, 0)
}

func (s *NodesStatementContext) AllNodeAssignment() []INodeAssignmentContext {
	children := s.GetChildren()
	len := 0
	for _, ctx := range children {
		if _, ok := ctx.(INodeAssignmentContext); ok {
			len++
		}
	}

	tst := make([]INodeAssignmentContext, len)
	i := 0
	for _, ctx := range children {
		if t, ok := ctx.(INodeAssignmentContext); ok {
			tst[i] = t.(INodeAssignmentContext)
			i++
		}
	}

	return tst
}

func (s *NodesStatementContext) NodeAssignment(i int) INodeAssignmentContext {
	var t antlr.RuleContext
	j := 0
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(INodeAssignmentContext); ok {
			if j == i {
				t = ctx.(antlr.RuleContext)
				break
			}
			j++
		}
	}

	if t == nil {
		return nil
	}

	return t.(INodeAssignmentContext)
}

func (s *NodesStatementContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *NodesStatementContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *NodesStatementContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.EnterNodesStatement(s)
	}
}

func (s *NodesStatementContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.ExitNodesStatement(s)
	}
}

func (s *NodesStatementContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case DAGVisitor:
		return t.VisitNodesStatement(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *DAGParser) NodesStatement() (localctx INodesStatementContext) {
	localctx = NewNodesStatementContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 10, DAGParserRULE_nodesStatement)
	var _la int

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(92)
		p.Match(DAGParserNODES)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	{
		p.SetState(93)
		p.Match(DAGParserCOLON)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	p.SetState(97)
	p.GetErrorHandler().Sync(p)
	if p.HasError() {
		goto errorExit
	}
	_la = p.GetTokenStream().LA(1)

	for _la == DAGParserIDENT {
		{
			p.SetState(94)
			p.NodeAssignment()
		}

		p.SetState(99)
		p.GetErrorHandler().Sync(p)
		if p.HasError() {
			goto errorExit
		}
		_la = p.GetTokenStream().LA(1)
	}

errorExit:
	if p.HasError() {
		v := p.GetError()
		localctx.SetException(v)
		p.GetErrorHandler().ReportError(p, v)
		p.GetErrorHandler().Recover(p, v)
		p.SetError(nil)
	}
	p.ExitRule()
	return localctx
	goto errorExit // Trick to prevent compiler error if the label is not used
}

// INodeAssignmentContext is an interface to support dynamic dispatch.
type INodeAssignmentContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// GetName returns the name token.
	GetName() antlr.Token

	// GetInitializer returns the initializer token.
	GetInitializer() antlr.Token

	// SetName sets the name token.
	SetName(antlr.Token)

	// SetInitializer sets the initializer token.
	SetInitializer(antlr.Token)

	// Getter signatures
	COLON_ASSIGN() antlr.TerminalNode
	LPAREN() antlr.TerminalNode
	RPAREN() antlr.TerminalNode
	AllIDENT() []antlr.TerminalNode
	IDENT(i int) antlr.TerminalNode
	Parameters() IParametersContext

	// IsNodeAssignmentContext differentiates from other interfaces.
	IsNodeAssignmentContext()
}

type NodeAssignmentContext struct {
	antlr.BaseParserRuleContext
	parser      antlr.Parser
	name        antlr.Token
	initializer antlr.Token
}

func NewEmptyNodeAssignmentContext() *NodeAssignmentContext {
	var p = new(NodeAssignmentContext)
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_nodeAssignment
	return p
}

func InitEmptyNodeAssignmentContext(p *NodeAssignmentContext) {
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_nodeAssignment
}

func (*NodeAssignmentContext) IsNodeAssignmentContext() {}

func NewNodeAssignmentContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *NodeAssignmentContext {
	var p = new(NodeAssignmentContext)

	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, parent, invokingState)

	p.parser = parser
	p.RuleIndex = DAGParserRULE_nodeAssignment

	return p
}

func (s *NodeAssignmentContext) GetParser() antlr.Parser { return s.parser }

func (s *NodeAssignmentContext) GetName() antlr.Token { return s.name }

func (s *NodeAssignmentContext) GetInitializer() antlr.Token { return s.initializer }

func (s *NodeAssignmentContext) SetName(v antlr.Token) { s.name = v }

func (s *NodeAssignmentContext) SetInitializer(v antlr.Token) { s.initializer = v }

func (s *NodeAssignmentContext) COLON_ASSIGN() antlr.TerminalNode {
	return s.GetToken(DAGParserCOLON_ASSIGN, 0)
}

func (s *NodeAssignmentContext) LPAREN() antlr.TerminalNode {
	return s.GetToken(DAGParserLPAREN, 0)
}

func (s *NodeAssignmentContext) RPAREN() antlr.TerminalNode {
	return s.GetToken(DAGParserRPAREN, 0)
}

func (s *NodeAssignmentContext) AllIDENT() []antlr.TerminalNode {
	return s.GetTokens(DAGParserIDENT)
}

func (s *NodeAssignmentContext) IDENT(i int) antlr.TerminalNode {
	return s.GetToken(DAGParserIDENT, i)
}

func (s *NodeAssignmentContext) Parameters() IParametersContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IParametersContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IParametersContext)
}

func (s *NodeAssignmentContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *NodeAssignmentContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *NodeAssignmentContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.EnterNodeAssignment(s)
	}
}

func (s *NodeAssignmentContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.ExitNodeAssignment(s)
	}
}

func (s *NodeAssignmentContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case DAGVisitor:
		return t.VisitNodeAssignment(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *DAGParser) NodeAssignment() (localctx INodeAssignmentContext) {
	localctx = NewNodeAssignmentContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 12, DAGParserRULE_nodeAssignment)
	var _la int

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(100)

		var _m = p.Match(DAGParserIDENT)

		localctx.(*NodeAssignmentContext).name = _m
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	{
		p.SetState(101)
		p.Match(DAGParserCOLON_ASSIGN)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	{
		p.SetState(102)

		var _m = p.Match(DAGParserIDENT)

		localctx.(*NodeAssignmentContext).initializer = _m
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	{
		p.SetState(103)
		p.Match(DAGParserLPAREN)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	p.SetState(105)
	p.GetErrorHandler().Sync(p)
	if p.HasError() {
		goto errorExit
	}
	_la = p.GetTokenStream().LA(1)

	if _la == DAGParserIDENT {
		{
			p.SetState(104)
			p.Parameters()
		}

	}
	{
		p.SetState(107)
		p.Match(DAGParserRPAREN)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}

errorExit:
	if p.HasError() {
		v := p.GetError()
		localctx.SetException(v)
		p.GetErrorHandler().ReportError(p, v)
		p.GetErrorHandler().Recover(p, v)
		p.SetError(nil)
	}
	p.ExitRule()
	return localctx
	goto errorExit // Trick to prevent compiler error if the label is not used
}

// ISuccessStatementContext is an interface to support dynamic dispatch.
type ISuccessStatementContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	SUCCESS() antlr.TerminalNode
	COLON() antlr.TerminalNode
	AllEdgeStatement() []IEdgeStatementContext
	EdgeStatement(i int) IEdgeStatementContext

	// IsSuccessStatementContext differentiates from other interfaces.
	IsSuccessStatementContext()
}

type SuccessStatementContext struct {
	antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptySuccessStatementContext() *SuccessStatementContext {
	var p = new(SuccessStatementContext)
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_successStatement
	return p
}

func InitEmptySuccessStatementContext(p *SuccessStatementContext) {
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_successStatement
}

func (*SuccessStatementContext) IsSuccessStatementContext() {}

func NewSuccessStatementContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *SuccessStatementContext {
	var p = new(SuccessStatementContext)

	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, parent, invokingState)

	p.parser = parser
	p.RuleIndex = DAGParserRULE_successStatement

	return p
}

func (s *SuccessStatementContext) GetParser() antlr.Parser { return s.parser }

func (s *SuccessStatementContext) SUCCESS() antlr.TerminalNode {
	return s.GetToken(DAGParserSUCCESS, 0)
}

func (s *SuccessStatementContext) COLON() antlr.TerminalNode {
	return s.GetToken(DAGParserCOLON, 0)
}

func (s *SuccessStatementContext) AllEdgeStatement() []IEdgeStatementContext {
	children := s.GetChildren()
	len := 0
	for _, ctx := range children {
		if _, ok := ctx.(IEdgeStatementContext); ok {
			len++
		}
	}

	tst := make([]IEdgeStatementContext, len)
	i := 0
	for _, ctx := range children {
		if t, ok := ctx.(IEdgeStatementContext); ok {
			tst[i] = t.(IEdgeStatementContext)
			i++
		}
	}

	return tst
}

func (s *SuccessStatementContext) EdgeStatement(i int) IEdgeStatementContext {
	var t antlr.RuleContext
	j := 0
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IEdgeStatementContext); ok {
			if j == i {
				t = ctx.(antlr.RuleContext)
				break
			}
			j++
		}
	}

	if t == nil {
		return nil
	}

	return t.(IEdgeStatementContext)
}

func (s *SuccessStatementContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *SuccessStatementContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *SuccessStatementContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.EnterSuccessStatement(s)
	}
}

func (s *SuccessStatementContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.ExitSuccessStatement(s)
	}
}

func (s *SuccessStatementContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case DAGVisitor:
		return t.VisitSuccessStatement(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *DAGParser) SuccessStatement() (localctx ISuccessStatementContext) {
	localctx = NewSuccessStatementContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 14, DAGParserRULE_successStatement)
	var _la int

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(109)
		p.Match(DAGParserSUCCESS)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	{
		p.SetState(110)
		p.Match(DAGParserCOLON)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	p.SetState(114)
	p.GetErrorHandler().Sync(p)
	if p.HasError() {
		goto errorExit
	}
	_la = p.GetTokenStream().LA(1)

	for _la == DAGParserEND || _la == DAGParserIDENT {
		{
			p.SetState(111)
			p.EdgeStatement()
		}

		p.SetState(116)
		p.GetErrorHandler().Sync(p)
		if p.HasError() {
			goto errorExit
		}
		_la = p.GetTokenStream().LA(1)
	}

errorExit:
	if p.HasError() {
		v := p.GetError()
		localctx.SetException(v)
		p.GetErrorHandler().ReportError(p, v)
		p.GetErrorHandler().Recover(p, v)
		p.SetError(nil)
	}
	p.ExitRule()
	return localctx
	goto errorExit // Trick to prevent compiler error if the label is not used
}

// IErrorStatementContext is an interface to support dynamic dispatch.
type IErrorStatementContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	ERROR() antlr.TerminalNode
	COLON() antlr.TerminalNode
	AllEdgeStatement() []IEdgeStatementContext
	EdgeStatement(i int) IEdgeStatementContext

	// IsErrorStatementContext differentiates from other interfaces.
	IsErrorStatementContext()
}

type ErrorStatementContext struct {
	antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyErrorStatementContext() *ErrorStatementContext {
	var p = new(ErrorStatementContext)
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_errorStatement
	return p
}

func InitEmptyErrorStatementContext(p *ErrorStatementContext) {
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_errorStatement
}

func (*ErrorStatementContext) IsErrorStatementContext() {}

func NewErrorStatementContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *ErrorStatementContext {
	var p = new(ErrorStatementContext)

	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, parent, invokingState)

	p.parser = parser
	p.RuleIndex = DAGParserRULE_errorStatement

	return p
}

func (s *ErrorStatementContext) GetParser() antlr.Parser { return s.parser }

func (s *ErrorStatementContext) ERROR() antlr.TerminalNode {
	return s.GetToken(DAGParserERROR, 0)
}

func (s *ErrorStatementContext) COLON() antlr.TerminalNode {
	return s.GetToken(DAGParserCOLON, 0)
}

func (s *ErrorStatementContext) AllEdgeStatement() []IEdgeStatementContext {
	children := s.GetChildren()
	len := 0
	for _, ctx := range children {
		if _, ok := ctx.(IEdgeStatementContext); ok {
			len++
		}
	}

	tst := make([]IEdgeStatementContext, len)
	i := 0
	for _, ctx := range children {
		if t, ok := ctx.(IEdgeStatementContext); ok {
			tst[i] = t.(IEdgeStatementContext)
			i++
		}
	}

	return tst
}

func (s *ErrorStatementContext) EdgeStatement(i int) IEdgeStatementContext {
	var t antlr.RuleContext
	j := 0
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IEdgeStatementContext); ok {
			if j == i {
				t = ctx.(antlr.RuleContext)
				break
			}
			j++
		}
	}

	if t == nil {
		return nil
	}

	return t.(IEdgeStatementContext)
}

func (s *ErrorStatementContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *ErrorStatementContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *ErrorStatementContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.EnterErrorStatement(s)
	}
}

func (s *ErrorStatementContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.ExitErrorStatement(s)
	}
}

func (s *ErrorStatementContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case DAGVisitor:
		return t.VisitErrorStatement(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *DAGParser) ErrorStatement() (localctx IErrorStatementContext) {
	localctx = NewErrorStatementContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 16, DAGParserRULE_errorStatement)
	var _la int

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(117)
		p.Match(DAGParserERROR)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	{
		p.SetState(118)
		p.Match(DAGParserCOLON)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	p.SetState(122)
	p.GetErrorHandler().Sync(p)
	if p.HasError() {
		goto errorExit
	}
	_la = p.GetTokenStream().LA(1)

	for _la == DAGParserEND || _la == DAGParserIDENT {
		{
			p.SetState(119)
			p.EdgeStatement()
		}

		p.SetState(124)
		p.GetErrorHandler().Sync(p)
		if p.HasError() {
			goto errorExit
		}
		_la = p.GetTokenStream().LA(1)
	}

errorExit:
	if p.HasError() {
		v := p.GetError()
		localctx.SetException(v)
		p.GetErrorHandler().ReportError(p, v)
		p.GetErrorHandler().Recover(p, v)
		p.SetError(nil)
	}
	p.ExitRule()
	return localctx
	goto errorExit // Trick to prevent compiler error if the label is not used
}

// IAbortStatementContext is an interface to support dynamic dispatch.
type IAbortStatementContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	ABORT() antlr.TerminalNode
	COLON() antlr.TerminalNode
	AllEdgeStatement() []IEdgeStatementContext
	EdgeStatement(i int) IEdgeStatementContext

	// IsAbortStatementContext differentiates from other interfaces.
	IsAbortStatementContext()
}

type AbortStatementContext struct {
	antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyAbortStatementContext() *AbortStatementContext {
	var p = new(AbortStatementContext)
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_abortStatement
	return p
}

func InitEmptyAbortStatementContext(p *AbortStatementContext) {
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_abortStatement
}

func (*AbortStatementContext) IsAbortStatementContext() {}

func NewAbortStatementContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *AbortStatementContext {
	var p = new(AbortStatementContext)

	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, parent, invokingState)

	p.parser = parser
	p.RuleIndex = DAGParserRULE_abortStatement

	return p
}

func (s *AbortStatementContext) GetParser() antlr.Parser { return s.parser }

func (s *AbortStatementContext) ABORT() antlr.TerminalNode {
	return s.GetToken(DAGParserABORT, 0)
}

func (s *AbortStatementContext) COLON() antlr.TerminalNode {
	return s.GetToken(DAGParserCOLON, 0)
}

func (s *AbortStatementContext) AllEdgeStatement() []IEdgeStatementContext {
	children := s.GetChildren()
	len := 0
	for _, ctx := range children {
		if _, ok := ctx.(IEdgeStatementContext); ok {
			len++
		}
	}

	tst := make([]IEdgeStatementContext, len)
	i := 0
	for _, ctx := range children {
		if t, ok := ctx.(IEdgeStatementContext); ok {
			tst[i] = t.(IEdgeStatementContext)
			i++
		}
	}

	return tst
}

func (s *AbortStatementContext) EdgeStatement(i int) IEdgeStatementContext {
	var t antlr.RuleContext
	j := 0
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IEdgeStatementContext); ok {
			if j == i {
				t = ctx.(antlr.RuleContext)
				break
			}
			j++
		}
	}

	if t == nil {
		return nil
	}

	return t.(IEdgeStatementContext)
}

func (s *AbortStatementContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *AbortStatementContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *AbortStatementContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.EnterAbortStatement(s)
	}
}

func (s *AbortStatementContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.ExitAbortStatement(s)
	}
}

func (s *AbortStatementContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case DAGVisitor:
		return t.VisitAbortStatement(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *DAGParser) AbortStatement() (localctx IAbortStatementContext) {
	localctx = NewAbortStatementContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 18, DAGParserRULE_abortStatement)
	var _la int

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(125)
		p.Match(DAGParserABORT)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	{
		p.SetState(126)
		p.Match(DAGParserCOLON)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	p.SetState(130)
	p.GetErrorHandler().Sync(p)
	if p.HasError() {
		goto errorExit
	}
	_la = p.GetTokenStream().LA(1)

	for _la == DAGParserEND || _la == DAGParserIDENT {
		{
			p.SetState(127)
			p.EdgeStatement()
		}

		p.SetState(132)
		p.GetErrorHandler().Sync(p)
		if p.HasError() {
			goto errorExit
		}
		_la = p.GetTokenStream().LA(1)
	}

errorExit:
	if p.HasError() {
		v := p.GetError()
		localctx.SetException(v)
		p.GetErrorHandler().ReportError(p, v)
		p.GetErrorHandler().Recover(p, v)
		p.SetError(nil)
	}
	p.ExitRule()
	return localctx
	goto errorExit // Trick to prevent compiler error if the label is not used
}

// IBranchesStatementContext is an interface to support dynamic dispatch.
type IBranchesStatementContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	BRANCHES() antlr.TerminalNode
	COLON() antlr.TerminalNode
	AllBranchAssignment() []IBranchAssignmentContext
	BranchAssignment(i int) IBranchAssignmentContext

	// IsBranchesStatementContext differentiates from other interfaces.
	IsBranchesStatementContext()
}

type BranchesStatementContext struct {
	antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyBranchesStatementContext() *BranchesStatementContext {
	var p = new(BranchesStatementContext)
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_branchesStatement
	return p
}

func InitEmptyBranchesStatementContext(p *BranchesStatementContext) {
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_branchesStatement
}

func (*BranchesStatementContext) IsBranchesStatementContext() {}

func NewBranchesStatementContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *BranchesStatementContext {
	var p = new(BranchesStatementContext)

	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, parent, invokingState)

	p.parser = parser
	p.RuleIndex = DAGParserRULE_branchesStatement

	return p
}

func (s *BranchesStatementContext) GetParser() antlr.Parser { return s.parser }

func (s *BranchesStatementContext) BRANCHES() antlr.TerminalNode {
	return s.GetToken(DAGParserBRANCHES, 0)
}

func (s *BranchesStatementContext) COLON() antlr.TerminalNode {
	return s.GetToken(DAGParserCOLON, 0)
}

func (s *BranchesStatementContext) AllBranchAssignment() []IBranchAssignmentContext {
	children := s.GetChildren()
	len := 0
	for _, ctx := range children {
		if _, ok := ctx.(IBranchAssignmentContext); ok {
			len++
		}
	}

	tst := make([]IBranchAssignmentContext, len)
	i := 0
	for _, ctx := range children {
		if t, ok := ctx.(IBranchAssignmentContext); ok {
			tst[i] = t.(IBranchAssignmentContext)
			i++
		}
	}

	return tst
}

func (s *BranchesStatementContext) BranchAssignment(i int) IBranchAssignmentContext {
	var t antlr.RuleContext
	j := 0
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IBranchAssignmentContext); ok {
			if j == i {
				t = ctx.(antlr.RuleContext)
				break
			}
			j++
		}
	}

	if t == nil {
		return nil
	}

	return t.(IBranchAssignmentContext)
}

func (s *BranchesStatementContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *BranchesStatementContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *BranchesStatementContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.EnterBranchesStatement(s)
	}
}

func (s *BranchesStatementContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.ExitBranchesStatement(s)
	}
}

func (s *BranchesStatementContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case DAGVisitor:
		return t.VisitBranchesStatement(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *DAGParser) BranchesStatement() (localctx IBranchesStatementContext) {
	localctx = NewBranchesStatementContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 20, DAGParserRULE_branchesStatement)
	var _la int

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(133)
		p.Match(DAGParserBRANCHES)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	{
		p.SetState(134)
		p.Match(DAGParserCOLON)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	p.SetState(138)
	p.GetErrorHandler().Sync(p)
	if p.HasError() {
		goto errorExit
	}
	_la = p.GetTokenStream().LA(1)

	for _la == DAGParserIDENT {
		{
			p.SetState(135)
			p.BranchAssignment()
		}

		p.SetState(140)
		p.GetErrorHandler().Sync(p)
		if p.HasError() {
			goto errorExit
		}
		_la = p.GetTokenStream().LA(1)
	}

errorExit:
	if p.HasError() {
		v := p.GetError()
		localctx.SetException(v)
		p.GetErrorHandler().ReportError(p, v)
		p.GetErrorHandler().Recover(p, v)
		p.SetError(nil)
	}
	p.ExitRule()
	return localctx
	goto errorExit // Trick to prevent compiler error if the label is not used
}

// IEdgeStatementContext is an interface to support dynamic dispatch.
type IEdgeStatementContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	IDENT() antlr.TerminalNode
	END() antlr.TerminalNode
	AllEdgeStatement() []IEdgeStatementContext
	EdgeStatement(i int) IEdgeStatementContext
	AllRIGHT_ARROW() []antlr.TerminalNode
	RIGHT_ARROW(i int) antlr.TerminalNode
	AllLEFT_ARROW() []antlr.TerminalNode
	LEFT_ARROW(i int) antlr.TerminalNode

	// IsEdgeStatementContext differentiates from other interfaces.
	IsEdgeStatementContext()
}

type EdgeStatementContext struct {
	antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyEdgeStatementContext() *EdgeStatementContext {
	var p = new(EdgeStatementContext)
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_edgeStatement
	return p
}

func InitEmptyEdgeStatementContext(p *EdgeStatementContext) {
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_edgeStatement
}

func (*EdgeStatementContext) IsEdgeStatementContext() {}

func NewEdgeStatementContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *EdgeStatementContext {
	var p = new(EdgeStatementContext)

	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, parent, invokingState)

	p.parser = parser
	p.RuleIndex = DAGParserRULE_edgeStatement

	return p
}

func (s *EdgeStatementContext) GetParser() antlr.Parser { return s.parser }

func (s *EdgeStatementContext) IDENT() antlr.TerminalNode {
	return s.GetToken(DAGParserIDENT, 0)
}

func (s *EdgeStatementContext) END() antlr.TerminalNode {
	return s.GetToken(DAGParserEND, 0)
}

func (s *EdgeStatementContext) AllEdgeStatement() []IEdgeStatementContext {
	children := s.GetChildren()
	len := 0
	for _, ctx := range children {
		if _, ok := ctx.(IEdgeStatementContext); ok {
			len++
		}
	}

	tst := make([]IEdgeStatementContext, len)
	i := 0
	for _, ctx := range children {
		if t, ok := ctx.(IEdgeStatementContext); ok {
			tst[i] = t.(IEdgeStatementContext)
			i++
		}
	}

	return tst
}

func (s *EdgeStatementContext) EdgeStatement(i int) IEdgeStatementContext {
	var t antlr.RuleContext
	j := 0
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IEdgeStatementContext); ok {
			if j == i {
				t = ctx.(antlr.RuleContext)
				break
			}
			j++
		}
	}

	if t == nil {
		return nil
	}

	return t.(IEdgeStatementContext)
}

func (s *EdgeStatementContext) AllRIGHT_ARROW() []antlr.TerminalNode {
	return s.GetTokens(DAGParserRIGHT_ARROW)
}

func (s *EdgeStatementContext) RIGHT_ARROW(i int) antlr.TerminalNode {
	return s.GetToken(DAGParserRIGHT_ARROW, i)
}

func (s *EdgeStatementContext) AllLEFT_ARROW() []antlr.TerminalNode {
	return s.GetTokens(DAGParserLEFT_ARROW)
}

func (s *EdgeStatementContext) LEFT_ARROW(i int) antlr.TerminalNode {
	return s.GetToken(DAGParserLEFT_ARROW, i)
}

func (s *EdgeStatementContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *EdgeStatementContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *EdgeStatementContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.EnterEdgeStatement(s)
	}
}

func (s *EdgeStatementContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.ExitEdgeStatement(s)
	}
}

func (s *EdgeStatementContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case DAGVisitor:
		return t.VisitEdgeStatement(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *DAGParser) EdgeStatement() (localctx IEdgeStatementContext) {
	localctx = NewEdgeStatementContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 22, DAGParserRULE_edgeStatement)
	var _la int

	var _alt int

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(141)
		_la = p.GetTokenStream().LA(1)

		if !(_la == DAGParserEND || _la == DAGParserIDENT) {
			p.GetErrorHandler().RecoverInline(p)
		} else {
			p.GetErrorHandler().ReportMatch(p)
			p.Consume()
		}
	}
	p.SetState(146)
	p.GetErrorHandler().Sync(p)
	if p.HasError() {
		goto errorExit
	}
	_alt = p.GetInterpreter().AdaptivePredict(p.BaseParser, p.GetTokenStream(), 14, p.GetParserRuleContext())
	if p.HasError() {
		goto errorExit
	}
	for _alt != 2 && _alt != antlr.ATNInvalidAltNumber {
		if _alt == 1 {
			{
				p.SetState(142)
				_la = p.GetTokenStream().LA(1)

				if !(_la == DAGParserRIGHT_ARROW || _la == DAGParserLEFT_ARROW) {
					p.GetErrorHandler().RecoverInline(p)
				} else {
					p.GetErrorHandler().ReportMatch(p)
					p.Consume()
				}
			}
			{
				p.SetState(143)
				p.EdgeStatement()
			}

		}
		p.SetState(148)
		p.GetErrorHandler().Sync(p)
		if p.HasError() {
			goto errorExit
		}
		_alt = p.GetInterpreter().AdaptivePredict(p.BaseParser, p.GetTokenStream(), 14, p.GetParserRuleContext())
		if p.HasError() {
			goto errorExit
		}
	}

errorExit:
	if p.HasError() {
		v := p.GetError()
		localctx.SetException(v)
		p.GetErrorHandler().ReportError(p, v)
		p.GetErrorHandler().Recover(p, v)
		p.SetError(nil)
	}
	p.ExitRule()
	return localctx
	goto errorExit // Trick to prevent compiler error if the label is not used
}

// IBranchAssignmentContext is an interface to support dynamic dispatch.
type IBranchAssignmentContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// GetName returns the name token.
	GetName() antlr.Token

	// SetName sets the name token.
	SetName(antlr.Token)

	// Getter signatures
	ASSIGN() antlr.TerminalNode
	LBRACE() antlr.TerminalNode
	AllBranchPair() []IBranchPairContext
	BranchPair(i int) IBranchPairContext
	RBRACE() antlr.TerminalNode
	IDENT() antlr.TerminalNode
	AllCOMMA() []antlr.TerminalNode
	COMMA(i int) antlr.TerminalNode

	// IsBranchAssignmentContext differentiates from other interfaces.
	IsBranchAssignmentContext()
}

type BranchAssignmentContext struct {
	antlr.BaseParserRuleContext
	parser antlr.Parser
	name   antlr.Token
}

func NewEmptyBranchAssignmentContext() *BranchAssignmentContext {
	var p = new(BranchAssignmentContext)
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_branchAssignment
	return p
}

func InitEmptyBranchAssignmentContext(p *BranchAssignmentContext) {
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_branchAssignment
}

func (*BranchAssignmentContext) IsBranchAssignmentContext() {}

func NewBranchAssignmentContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *BranchAssignmentContext {
	var p = new(BranchAssignmentContext)

	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, parent, invokingState)

	p.parser = parser
	p.RuleIndex = DAGParserRULE_branchAssignment

	return p
}

func (s *BranchAssignmentContext) GetParser() antlr.Parser { return s.parser }

func (s *BranchAssignmentContext) GetName() antlr.Token { return s.name }

func (s *BranchAssignmentContext) SetName(v antlr.Token) { s.name = v }

func (s *BranchAssignmentContext) ASSIGN() antlr.TerminalNode {
	return s.GetToken(DAGParserASSIGN, 0)
}

func (s *BranchAssignmentContext) LBRACE() antlr.TerminalNode {
	return s.GetToken(DAGParserLBRACE, 0)
}

func (s *BranchAssignmentContext) AllBranchPair() []IBranchPairContext {
	children := s.GetChildren()
	len := 0
	for _, ctx := range children {
		if _, ok := ctx.(IBranchPairContext); ok {
			len++
		}
	}

	tst := make([]IBranchPairContext, len)
	i := 0
	for _, ctx := range children {
		if t, ok := ctx.(IBranchPairContext); ok {
			tst[i] = t.(IBranchPairContext)
			i++
		}
	}

	return tst
}

func (s *BranchAssignmentContext) BranchPair(i int) IBranchPairContext {
	var t antlr.RuleContext
	j := 0
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IBranchPairContext); ok {
			if j == i {
				t = ctx.(antlr.RuleContext)
				break
			}
			j++
		}
	}

	if t == nil {
		return nil
	}

	return t.(IBranchPairContext)
}

func (s *BranchAssignmentContext) RBRACE() antlr.TerminalNode {
	return s.GetToken(DAGParserRBRACE, 0)
}

func (s *BranchAssignmentContext) IDENT() antlr.TerminalNode {
	return s.GetToken(DAGParserIDENT, 0)
}

func (s *BranchAssignmentContext) AllCOMMA() []antlr.TerminalNode {
	return s.GetTokens(DAGParserCOMMA)
}

func (s *BranchAssignmentContext) COMMA(i int) antlr.TerminalNode {
	return s.GetToken(DAGParserCOMMA, i)
}

func (s *BranchAssignmentContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *BranchAssignmentContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *BranchAssignmentContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.EnterBranchAssignment(s)
	}
}

func (s *BranchAssignmentContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.ExitBranchAssignment(s)
	}
}

func (s *BranchAssignmentContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case DAGVisitor:
		return t.VisitBranchAssignment(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *DAGParser) BranchAssignment() (localctx IBranchAssignmentContext) {
	localctx = NewBranchAssignmentContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 24, DAGParserRULE_branchAssignment)
	var _la int

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(149)

		var _m = p.Match(DAGParserIDENT)

		localctx.(*BranchAssignmentContext).name = _m
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	{
		p.SetState(150)
		p.Match(DAGParserASSIGN)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	{
		p.SetState(151)
		p.Match(DAGParserLBRACE)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	{
		p.SetState(152)
		p.BranchPair()
	}
	p.SetState(157)
	p.GetErrorHandler().Sync(p)
	if p.HasError() {
		goto errorExit
	}
	_la = p.GetTokenStream().LA(1)

	for _la == DAGParserCOMMA {
		{
			p.SetState(153)
			p.Match(DAGParserCOMMA)
			if p.HasError() {
				// Recognition error - abort rule
				goto errorExit
			}
		}
		{
			p.SetState(154)
			p.BranchPair()
		}

		p.SetState(159)
		p.GetErrorHandler().Sync(p)
		if p.HasError() {
			goto errorExit
		}
		_la = p.GetTokenStream().LA(1)
	}
	{
		p.SetState(160)
		p.Match(DAGParserRBRACE)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}

errorExit:
	if p.HasError() {
		v := p.GetError()
		localctx.SetException(v)
		p.GetErrorHandler().ReportError(p, v)
		p.GetErrorHandler().Recover(p, v)
		p.SetError(nil)
	}
	p.ExitRule()
	return localctx
	goto errorExit // Trick to prevent compiler error if the label is not used
}

// IBranchPairContext is an interface to support dynamic dispatch.
type IBranchPairContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// GetValue returns the value token.
	GetValue() antlr.Token

	// SetValue sets the value token.
	SetValue(antlr.Token)

	// GetKey returns the key rule contexts.
	GetKey() IStringLiteralContext

	// SetKey sets the key rule contexts.
	SetKey(IStringLiteralContext)

	// Getter signatures
	COLON() antlr.TerminalNode
	StringLiteral() IStringLiteralContext
	IDENT() antlr.TerminalNode

	// IsBranchPairContext differentiates from other interfaces.
	IsBranchPairContext()
}

type BranchPairContext struct {
	antlr.BaseParserRuleContext
	parser antlr.Parser
	key    IStringLiteralContext
	value  antlr.Token
}

func NewEmptyBranchPairContext() *BranchPairContext {
	var p = new(BranchPairContext)
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_branchPair
	return p
}

func InitEmptyBranchPairContext(p *BranchPairContext) {
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_branchPair
}

func (*BranchPairContext) IsBranchPairContext() {}

func NewBranchPairContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *BranchPairContext {
	var p = new(BranchPairContext)

	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, parent, invokingState)

	p.parser = parser
	p.RuleIndex = DAGParserRULE_branchPair

	return p
}

func (s *BranchPairContext) GetParser() antlr.Parser { return s.parser }

func (s *BranchPairContext) GetValue() antlr.Token { return s.value }

func (s *BranchPairContext) SetValue(v antlr.Token) { s.value = v }

func (s *BranchPairContext) GetKey() IStringLiteralContext { return s.key }

func (s *BranchPairContext) SetKey(v IStringLiteralContext) { s.key = v }

func (s *BranchPairContext) COLON() antlr.TerminalNode {
	return s.GetToken(DAGParserCOLON, 0)
}

func (s *BranchPairContext) StringLiteral() IStringLiteralContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IStringLiteralContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IStringLiteralContext)
}

func (s *BranchPairContext) IDENT() antlr.TerminalNode {
	return s.GetToken(DAGParserIDENT, 0)
}

func (s *BranchPairContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *BranchPairContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *BranchPairContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.EnterBranchPair(s)
	}
}

func (s *BranchPairContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.ExitBranchPair(s)
	}
}

func (s *BranchPairContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case DAGVisitor:
		return t.VisitBranchPair(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *DAGParser) BranchPair() (localctx IBranchPairContext) {
	localctx = NewBranchPairContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 26, DAGParserRULE_branchPair)
	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(162)

		var _x = p.StringLiteral()

		localctx.(*BranchPairContext).key = _x
	}
	{
		p.SetState(163)
		p.Match(DAGParserCOLON)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}
	{
		p.SetState(164)

		var _m = p.Match(DAGParserIDENT)

		localctx.(*BranchPairContext).value = _m
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}

errorExit:
	if p.HasError() {
		v := p.GetError()
		localctx.SetException(v)
		p.GetErrorHandler().ReportError(p, v)
		p.GetErrorHandler().Recover(p, v)
		p.SetError(nil)
	}
	p.ExitRule()
	return localctx
	goto errorExit // Trick to prevent compiler error if the label is not used
}

// IStringLiteralContext is an interface to support dynamic dispatch.
type IStringLiteralContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	STRING() antlr.TerminalNode

	// IsStringLiteralContext differentiates from other interfaces.
	IsStringLiteralContext()
}

type StringLiteralContext struct {
	antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyStringLiteralContext() *StringLiteralContext {
	var p = new(StringLiteralContext)
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_stringLiteral
	return p
}

func InitEmptyStringLiteralContext(p *StringLiteralContext) {
	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, nil, -1)
	p.RuleIndex = DAGParserRULE_stringLiteral
}

func (*StringLiteralContext) IsStringLiteralContext() {}

func NewStringLiteralContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *StringLiteralContext {
	var p = new(StringLiteralContext)

	antlr.InitBaseParserRuleContext(&p.BaseParserRuleContext, parent, invokingState)

	p.parser = parser
	p.RuleIndex = DAGParserRULE_stringLiteral

	return p
}

func (s *StringLiteralContext) GetParser() antlr.Parser { return s.parser }

func (s *StringLiteralContext) STRING() antlr.TerminalNode {
	return s.GetToken(DAGParserSTRING, 0)
}

func (s *StringLiteralContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *StringLiteralContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *StringLiteralContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.EnterStringLiteral(s)
	}
}

func (s *StringLiteralContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(DAGListener); ok {
		listenerT.ExitStringLiteral(s)
	}
}

func (s *StringLiteralContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case DAGVisitor:
		return t.VisitStringLiteral(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *DAGParser) StringLiteral() (localctx IStringLiteralContext) {
	localctx = NewStringLiteralContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 28, DAGParserRULE_stringLiteral)
	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(166)
		p.Match(DAGParserSTRING)
		if p.HasError() {
			// Recognition error - abort rule
			goto errorExit
		}
	}

errorExit:
	if p.HasError() {
		v := p.GetError()
		localctx.SetException(v)
		p.GetErrorHandler().ReportError(p, v)
		p.GetErrorHandler().Recover(p, v)
		p.SetError(nil)
	}
	p.ExitRule()
	return localctx
	goto errorExit // Trick to prevent compiler error if the label is not used
}
