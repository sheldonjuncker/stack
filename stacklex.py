import lib.ply.lex as lex

tokens = [
    'ID',
    'NUMBER',
    'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS', 'MODULUS',
    'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE',
    'LBRACKET', 'RBRACKET',
    'DOT',
    'OR', 'AND', 'NOT',
    'EQEQ', 'LT', 'GT', 'LTE', 'GTE', 'NE',
    'SEMI', 'COLON', 'COMMA', 'RANGE', 'ELLIPSIS',
    'TYPE',
    'SLCOMMENT', 'MLCOMMENT',
    'QMARK'
]

keywords = [
    'IF', 'ELSE',
    'WHILE', 'FOR',
    'IN',
    'BREAK', 'CONTINUE',
    'RETURN',
    'CLASS', 'INTERFACE', 'EXTENDS', 'IMPLEMENTS',
    'PUBLIC', 'PRIVATE',
    'IMPORT', 'AS',
    'NEW',
    'TRUE', 'FALSE', 'NULL'
]

tokens += keywords

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
t_OR = r'\|\|'
t_AND = r'&&'
t_NOT = r'!'

# Comparison
t_EQEQ = r'=='
t_LT = '<'
t_GT = '>'
t_LTE = '<='
t_GTE = '>='
t_NE = '!='

# Paren/Brace/Bracket
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

# Separators
t_SEMI = r';'
t_COLON = r':'
t_COMMA = r','
t_RANGE = r'\.\.'
t_ELLIPSIS = r'\.\.\.'

# Optional
t_QMARK = r'\?'

# Objects
t_DOT = r'\.'

# Type
t_TYPE = r'[A-Z][a-zA-Z0-9_]*'


# Identifiers and Keywords
def t_ID(t):
    r'[a-z][a-zA-Z0-9_]*'
    keywordUpper = t.value.upper()
    keywordLower = t.value.lower()
    if keywordUpper in keywords:
        t.type = keywordUpper
        t.value = keywordLower
    return t


def t_STRING(t):
    r'"(?:[^"\\]|\\.)*"'
    t.value = t.value[1:-1]
    t.value = int(t.value)
    return t


def t_SLCOMMENT(t):
    r'\# .*'
    t.lexer.skip(len(t.value))


def t_MLCOMMENT(t):
    r"""/\*.*\*/"""
    t.lexer.skip(len(t.value))


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Ignored characters
t_ignore = " \t\r"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    t.lexer.skip(1)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def testLexing():
    lex.lex()
