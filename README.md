### Compilador Simples
Um compilador simples em Python que realiza análise léxica, análise sintática e análise semântica para MINI PASCAL.

* Pré-requisitos
``` 
Python 3.11
Ply (instalável via pip install ply)
```
* Estrutura do Projeto
``` 
├── analisador_lexico.py
├── analisador_sintatico.py
├── analisador_semantico.py
├── main.py
├── README.md
```
Como Usar
Instalação de Dependências:
```
pip install ply
```
Execução do Compilador:

```
python main.py
```
###### Isso executará o programa principal, que demonstra a análise léxica, sintática e semântica de um exemplo de código.

* Detalhes do Código
  - ##### analisador_lexico.py: 
    - ###### Contém o analisador léxico que converte o código-fonte em uma sequência de tokens.
  - ##### analisador_sintatico.py:
    - ###### Implementa o analisador sintático usando PLY para criar a árvore de sintaxe abstrata (AST).
  - ##### analisador_semantico.py:
    - ###### Implementa o analisador semântico que verifica tipos e realiza análise de escopo.
  - ##### main.py:
    - ###### Arquivo principal que inicia o processo de compilação.
  - ##### codigo_teste.txt:
    - ###### Arquivo que é lido para ser analisado. 
# Exemplo de código-fonte
```
PROGRAM exemplo;
VAR
    x: INTEGER;
    y: INTEGER;
BEGIN
    x := 10;
    y := 20;
    WRITE('A soma de ', x, ' e ', y, ' é: ', x + y);
END.
```
Licença
Este projeto está licenciado sob a Licença MIT.
