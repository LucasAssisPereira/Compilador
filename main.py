from analisador_lexico import lexer
from analisador_sintatico import parser
from analisador_semantico import Semantico

def read_source_code(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main():
    # Caminho para o arquivo de código fonte
    arquivo_fonte = "codigo_teste.txt"

    # Lê o código fonte do arquivo
    codigo_fonte = read_source_code(arquivo_fonte)

    # Análise Léxica
    lexer.input(codigo_fonte)
    for token in lexer:
        print(token)

    # Análise Sintática
    try:
        ast = parser.parse(codigo_fonte)
        print("Análise sintática concluída com sucesso!")
    except Exception as e:
        print(f"Erro sintático: {e}")
        return

    # Análise Semântica
    semantico = Semantico()
    try:
        semantico.analyze(ast)
        print("Análise semântica concluída com sucesso!")
    except Exception as e:
        print(f"Erro semântico: {e}")
        return

if __name__ == "__main__":
    main()