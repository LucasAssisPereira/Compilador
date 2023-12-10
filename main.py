from analisador_lexico import lexer
from analisador_sintatico import parser, parse_file
from analisador_semantico import Semantico

def analise_lexica(caminho_do_arquivo):
    with open(caminho_do_arquivo, 'r') as file:
        lexer.input(file.read())
        for token in lexer:
            print(token)
    print("Análise léxica concluída.")

def analise_sintatica_e_semantica(caminho_do_arquivo):
    try:
        # Analisador sintático
        ast = parse_file(caminho_do_arquivo)

        if ast is None:
            print("Erro Semantico")
        else:
            # Analisador semântico
            semantico = Semantico()
            semantico.analyze(ast)
            print("Análise semântica concluída.")

    except Exception as e:
        print(f"Erro durante a análise: {e}")

def main():
    # Substitua 'caminho_do_arquivo' pelo caminho real do arquivo Mini Pascal que você deseja analisar
    caminho_do_arquivo = 'codigo_teste.txt'
    print(caminho_do_arquivo)
    analise_lexica(caminho_do_arquivo)
    analise_sintatica_e_semantica(caminho_do_arquivo)

if __name__ == "__main__":
    main()