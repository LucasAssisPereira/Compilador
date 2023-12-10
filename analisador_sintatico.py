import ply.yacc as yacc
from analisador_lexico import tokens

# Variável global para rastrear erros sintáticos
erro_sintatico = False


def read_code_blocks_from_content(content):
    global erro_sintatico
    lines = content.split('\n')
    statement_list = lines[5].strip().upper() if lines else ''
    end_name = lines[9].strip().upper() if lines else ''

    if statement_list != 'BEGIN' and  end_name != 'END.':
        print('Bloco valido')
        erro_sintatico = True


    return statement_list, end_name


def validate_code(program_name, lineno):
    global erro_sintatico
    expected_start = "exemplo"

    if program_name.lower() != expected_start:
        print(f"Erro sintático: O código deve começar com a palavra-chave '{expected_start}' na linha {lineno}.")
        erro_sintatico = True

    if not erro_sintatico:
        print("Código válido!")


# Regra de produção principal
def p_program(p):
    'program : PROGRAM ID SEMICOLON declarations block DOT'
    validate_code(p[2], p.lineno(2))


# Regras de produção para declarações
def p_declarations(p):
    '''declarations : VAR declarations_list
                    | empty'''


def p_declarations_list(p):
    '''declarations_list : ID COLON type SEMICOLON declarations_list
                        | ID COLON type declarations_list
                        | empty'''

def p_type(p):
    '''type : INTEGER SEMICOLON
    | FLOAT SEMICOLON
    | STRING SEMICOLON
    | BOOLEAN SEMICOLON
    | REAL SEMICOLON'''


# Regras de produção para o bloco
def p_block(p):
    'block : BEGIN statements END'


def p_statements(p):
    '''statements : statement SEMICOLON statements
                  | empty'''


# Regras de produção para expressões
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | term'''


def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | factor'''


def p_factor_num(p):
    'factor : NUM'


def p_factor_real(p):
    'factor : NUM DOT NUM'


def p_factor_id(p):
    'factor : ID'


def p_factor_string(p):
    'factor : STRING'


# Regras de produção para comandos
def p_statement_write(p):
    'statement : WRITE LPAREN expression RPAREN'


def p_statement_assign(p):
    'statement : ID ASSIGN expression'


# Regra para representar um valor opcional vazio
def p_empty(p):
    'empty :'
    pass


# Função de erro
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


# Função para analisar um arquivo
def parse_file(caminho_arquivo):
    global erro_sintatico
    erro_sintatico = False

    try:
        with open(caminho_arquivo, 'r') as file:
            content = file.read()
            read_code_blocks_from_content(content)
            result = parser.parse(content)
            print("\n\n",content, "\n\n")
            if not erro_sintatico:
                print("Análise sintática concluída com sucesso.")
            print(result)
            return result

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return None, None, None
    except Exception as e:
        print(f"Erro durante a análise sintática: {e}")
        return None, None, None
