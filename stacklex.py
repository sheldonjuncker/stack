import lib.ply.lex as lex

tokens = (
    'NUMBER',
    'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS', 'MODULUS',
    'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE',
    'LBRACKET', 'RBRACKET',
    'DOT', 'NEW',
    'OR', 'AND', 'NOT',
    'ID', 'TYPE',
    'IF', 'ELSE',
    'WHILE', 'FOR',
    'IN',
    'BREAK', 'CONTINUE',
    'RETURN',
    'CLASS', 'INTERFACE', 'EXTENDS', 'IMPLEMENTS',
    'PUBLIC', 'PRIVATE',
    'IMPORT', 'AS',
    'SLCOMMENT'
)

# Tokens

# Operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULUS = r'%'

# Assignment
t_EQUALS = r'='

# Logic
T_OR = r'\|\|'
T_AND = r'&&'
T_NOT = r'!'

# Paren/Brace/Bracket
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

# Class Keywords
t_CLASS = r'class'
t_INTERFACE = r'interface'
t_EXTENDS = r'extends'
t_IMPLEMENTS = r'implements'
T_PUBLIC = 'public'
T_PRIVATE = 'private'

# Objects
t_DOT = r'\.'
t_NEW = r'new'

# Control Keywords
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_FOR = r'for'
t_BREAK = 'break'
t_CONTINUE = 'continue'
t_IN = r'in'

# Function Keywords
t_RETURN = r'return'

# Import Keywords
t_IMPORT = r'import'
t_AS = r'as'

# Identifier
t_ID = r'[a-z][a-zA-Z0-9_]*'

# Type
t_TYPE = r'[A-Z][a-zA-Z0-9_]*'


def t_STRING(t):
    r'"(?:[^"\\]|\\.)*"'
    t.value = t.value[1:-1]
    t.value = int(t.value)
    return t


def t_SLCOMMENT(t):
    r'\# .*'
    t.lexer.skip(len(t.value))


def t_mlcomment(t):
    r"""/\*.*\*/"""
    t.lexer.skip(len(t.value))


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    t.lexer.skip(1)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def testLexing():
    lex.lex()
