# Analisador Léxico

Código usado para a disciplina de Linguagens Formais e Autômatos.

```Python version: 3.11```

## Como Usar

- Clone o projeto

```bash
  git clone https://github.com/VictorDMe/analisador_lexico
```

- Entre no diretório do projeto

```bash
  cd analisador_lexico
```

- Modifique o arquivo reserved_words.json com as palavras reservadas e expressões regulares de seu interesse

- Rode o programa pelo terminal passando o código que quer analisar como argumento.

```bash
  python main.py -c <arquivo>
```

## Documentação

### Argumentos 

| Abreviação | O que é                     | Necessidade                                 | Descrição                                                                    |
| ---------- | --------------------------- | ------------------------------------------- | ---------------------------------------------------------------------------- |
| `-r`       | `Palavras Reservadas`       | **Opcional, default='reserved_words.json'** | Caminho para outro arquivo .json caso deseje usar                            |
| `-c`       | `Código`                    | **Obrigatório**                             | Código que será analisado                                                    |
| `-s`       | `Mostrar palavras corretas?`| **Opcional, padrão=False**                  | Booleano que determina se serão ou não mostrado na tela as palavras corretas |
| `-l`       | `Fazer log da análise`      | **Opcional, padrão=None**                   | Caminho da pasta onde será criado uma pasta 'logs' e o primeiro arquivo.     |

### Exemplo

```bash
  python main.py -r new_reseverd_words.json -c teste_arquivo.txt -s true -l path/to/my/folder
```

## Licença

[MIT](https://choosealicense.com/licenses/mit/)
