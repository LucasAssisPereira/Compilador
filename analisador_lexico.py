# Importe a biblioteca ply.lex
import ply.lex as lex

# Palavras-chave
reserved = {
    'PROGRAM': 'PROGRAM',
    'VAR': 'VAR',
    'BEGIN': 'BEGIN',
    'END': 'END',
    'INTEGER': 'INTEGER',
    'WRITE': 'WRITE',
    'READ': 'READ',
    'REAL': 'REAL',
    'BOOLEAN': 'BOOLEAN',
    'FLOAT': 'FLOAT',
    'STRING': 'STRING',
    'IF': 'IF',
    'WHILE': 'WHILE',
}

# Lista de tokens
tokens = [
    'ID',
    'NUM',
    'SEMICOLON',
    'COLON',
    'ASSIGN',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'DOT',
    'COMMA',
    'EMPTY',
] + list(reserved.values())

# Expressões regulares para os tokens

t_SEMICOLON = r';'
t_COLON = r':'
t_ASSIGN = r':='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOT = r'\.'
t_ignore = ' \t\n'

# Identificadores e palavras-chave

def t_PROGRAM(t):
    r'PROGRAM'
    return t

def t_VAR(t):
    r'VAR'
    return t

def t_INTEGER(t):
    r'INTEGER'
    return t

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # Remove as aspas duplas
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_IF(t):  # Adicione a regra para IF
    r'IF'
    return t

def t_WHILE(t):  # Adicione a regra para WHILE
    r'WHILE'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica se é uma palavra reservada
    return t

# Números
def t_NUM(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    print(f"Recognized NUM: {t.value}")
    return t

# Tratar vírgula como um token válido
def t_COMMA(t):
    r','
    return t

def t_EMPTY(t):
    r' [ \t\n]+'
    pass

# Manipulador de erro para caracteres inválidos
def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno = len(t.value)
    print(t.lexer.lineno)

# Criar o analisador léxico
lexer = lex.lex()