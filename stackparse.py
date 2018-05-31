import stacklex
import lib.ply.yacc as yacc

tokens = stacklex.tokens5

# Precedence rules for the arithmetic operators
precedence = (
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE'),
	('right', 'UMINUS'),
)

# dictionary of names (for storing variables)
names = {}


def p_statement_assign(p):
	'statement : NAME EQUALS expression'
	names[p[1]] = p[3]


def p_statement_expr(p):
	'statement : expression'
	print(p[1])


def p_expression_binop(p):
	'''expression : expression PLUS expression
	  | expression MINUS expression
	  | expression TIMES expression
	  | expression DIVIDE expression'''
	if p[2] == '+':
		p[0] = p[1] + p[3]
	elif p[2] == '-':
		p[0] = p[1] - p[3]
	elif p[2] == '*':
		p[0] = p[1] * p[3]
	elif p[2] == '/':
		p[0] = p[1] / p[3]


def p_expression_uminus(p):
	'expression : MINUS expression %prec UMINUS'
	p[0] = -p[2]


def p_expression_group(p):
	'expression : LPAREN expression RPAREN'
	p[0] = p[2]


def p_expression_number(p):
	'expression : NUMBER'
	p[0] = p[1]


def p_expression_name(p):
	'expression : NAME'
	try:
		p[0] = names[p[1]]
	except LookupError:
		print("Undefined name '%s'" % p[1])
		p[0] = 0


def p_error(p):
	print("Syntax error at '%s'" % p.value)


def testParsing():
	stacklex.testLexing()
	yacc.yacc()

	while True:
		try:
			s = input('calc > ')  # use input() on Python 3
		except EOFError:
			break
		yacc.parse(s)