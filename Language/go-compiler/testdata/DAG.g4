grammar DAG;

program: importStatement? (dagStatement)* EOF;

importStatement: IMPORTS COLON stringLiteral*;

dagStatement:
    DAG LBRACKET typ=IDENT RBRACKET name=IDENT LPAREN parameters? RPAREN
    GENERATES generates=IDENT LBRACE
        nodesStatement
        (successStatement
        | errorStatement
        | abortStatement
        | branchesStatement)*
    RBRACE;

parameters: parameter (COMMA parameter)*;
parameter: name=IDENT (COMMA name=IDENT)* typ=IDENT;

nodesStatement: NODES COLON nodeAssignment*;
nodeAssignment: name=IDENT COLON_ASSIGN initializer=IDENT LPAREN parameters? RPAREN;

successStatement: SUCCESS COLON edgeStatement*;
errorStatement: ERROR COLON edgeStatement*;
abortStatement: ABORT COLON edgeStatement*;
branchesStatement: BRANCHES COLON branchAssignment*;

edgeStatement: (IDENT|END) ((RIGHT_ARROW | LEFT_ARROW) edgeStatement)*;
branchAssignment: name=IDENT ASSIGN LBRACE branchPair (COMMA branchPair)* RBRACE;
branchPair: key=stringLiteral COLON value=IDENT;

stringLiteral: STRING;

IMPORTS: 'imports';
DAG: 'dag';
GENERATES: 'generates';
NODES: 'nodes';
SUCCESS: 'success';
ERROR: 'error';
ABORT: 'abort';
BRANCHES: 'branches';
END: 'end';

COLON_ASSIGN: ':=';
ASSIGN: '=';
RIGHT_ARROW: '->';
LEFT_ARROW: '<-';
COLON: ':';
LBRACE: '{';
RBRACE: '}';
LBRACKET: '[';
RBRACKET: ']';
LPAREN: '(';
RPAREN: ')';
COMMA: ',';

IDENT: [a-zA-Z_] [a-zA-Z0-9_]* ('.' [a-zA-Z_] [a-zA-Z0-9_]*)*;
STRING: '"' (~["\r\n])*? '"';
WS: [ \t\r\n]+ -> skip;