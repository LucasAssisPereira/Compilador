from analisador_lexico import lexer
from analisador_sintatico import parser, parse_file
from analisador_semantico import Semantico

def main():
    # Substitua 'caminho_do_arquivo' pelo caminho real do arquivo Mini Pascal que você deseja analisar
    caminho_do_arquivo = 'codigo_teste.txt'

    # Analisador léxico
    with open(caminho_do_arquivo, 'r') as file:
        lexer.input(file.read())
        for token in lexer:
            print(token)

    print("Análise léxica concluída.")

    # Analisador sintático
    ast = parse_file(caminho_do_arquivo)


    # Analisador semântico
    semantico = Semantico()
    semantico.analyze(ast)
    print("Análise semântica concluída.")

if __name__ == "__main__":
    main()
