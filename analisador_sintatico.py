import ply.yacc as yacc
from analisador_lexico import tokens

# Definição da gramática
def p_program(p):
    'program : PROGRAM ID SEMICOLON declarations block DOT'
    pass

def p_declarations(p):
    '''declarations : VAR declarations_list
                    | empty'''

def p_declarations_list(p):
    '''declarations_list : ID COLON type SEMICOLON declarations_list
                        | ID COLON type declarations_list
                        | empty'''
def p_type(p):
    '''type : INTEGER'''

def p_block(p):
    'block : BEGIN statements END'

def p_statements(p):
    '''statements : statement SEMICOLON statements
                  | empty'''


def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | term'''
    pass

def p_expression_comma(p):
    'expression : expression COMMA expression'
    pass

def p_term_factor(p):
    '''term : factor
            | term TIMES factor
            | term DIVIDE factor'''

def p_factor_num(p):
    'factor : NUM'

def p_factor_id(p):
    'factor : ID'

def p_factor_string(p):
    'factor : STRING'

def p_statement_write(p):
    'statement : WRITE LPAREN expression RPAREN'

def p_statement_assign(p):
    'statement : ID ASSIGN expression'

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print(f"Erro sintático: Token inesperado {p.value} na linha {p.lineno}, coluna {find_column(p.lexer.lexdata, p)}")

def find_column(input, token):
    last_cr = input.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

# Construir o analisador sintático
parser = yacc.yacc()

def parse_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return parser.parse(content)

