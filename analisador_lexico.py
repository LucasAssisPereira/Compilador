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
    'STRING',
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
t_ignore = ' \t'

# Identificadores e palavras-chave
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value.upper(), 'ID')
    return t

# Números
def t_NUM(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    print(f"Recognized NUM: {t.value}")
    return t

# Expressões regulares para strings
def t_STRING(t):
    r'\"([^"]|\\.)*\"|\'([^\']|\\.)*\''
    t.value = t.value[1:-1]  # Remover as aspas
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

# Criar o analisador léxico
lexer = lex.lex()