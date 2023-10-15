import json, re, argparse, os, logging
from datetime import datetime


def fetch_reserved_words(file_path:str='reserved_words.json') -> dict[str]:
    """
    Read a .json with reserved words.

    Parameters
    ----------
    file_path : str, optional
        The .json file must be write in format:

        .. code-block:: json
        {
            "name" : regex
        }
        
    Returns
    -------
    dict[str]
        relation between reseverd word and regex.
    """    

    with open(file_path, 'r') as f:
        data = json.loads(f.read())

    for key, value in data.items():
        if key == 'var_declaration':
            data[key] = r'\b(?!'
            data[key] += '|'.join(data['reseverd_words'].values())
            data[key] += r')[a-zA-Z]\w*:'

        elif key != 'reseverd_words':
            data[key] = re.compile(f'{value}{data["end_line"]}?')

    return data
    
def fetch_source_code(file_path:str) -> str:
    """
    Read a source code.

    Parameters
    ----------
    file_path : str
        path to the source code.

    Returns
    -------
    str
        source code in string format.
    """    

    with open(file_path, 'r') as f:
        return ''.join(f.readlines())

def lexic_analyse(reserved_word:dict, source_code:str, print_correct:bool=True, path_log=None) -> None:
    """
    Analyse the source code with reseverd words relation.

    Parameters
    ----------
    reserved_word : dict
        relation 'name' : regex.
    source_code : str
        source code to analyze.
    print_correct : bool, optional
        if ```True``` : print correct lexic words.
        if ```False``` : not print correct lexic words.
    path_log : str, optional
        path to log file,
        if ```None``` not create a log file
        by default = None
    """    

    if path_log is not None:
        folder_path = os.path.join(path_log, 'logs')

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Pasta 'logs' criado com sucesso em '{folder_path}'.")
        else:
            print(f"Pasta 'logs' já existe em '{folder_path}'.")

        logging.basicConfig(filename=f'{folder_path}\\lexic_analyse.log', encoding='utf-8', level=logging.ERROR)

    lines = source_code.splitlines()
    print('=-' * 10, 'ANÁLISE', '=-' * 10)

    for num_line, line in enumerate(lines):
        for word in line.split():
            is_correct_word = False
            for keyword, regex in reserved_word.items():
                if keyword == 'reseverd_words':
                    for r_word in reserved_word['reseverd_words'].values():
                        if re.fullmatch(pattern=r_word, string=word):
                            is_correct_word = True

                elif re.fullmatch(pattern=regex, string=word):
                    is_correct_word = True
                    break 
            
            if is_correct_word and print_correct:
                print('\x1b[1;32;40m' + f'Encontrado palavra reservada : "{keyword}" em "{word}" na linha {num_line + 1}' + '\x1b[0m')

            elif is_correct_word is False: 
                if path_log:
                    logging.error(f'Erro na palavra "{word}" na linha {num_line + 1}')

                print('\x1b[1;31;40m' + f'Erro na palavra "{word}" na linha {num_line + 1}' + '\x1b[0m')
            
def main():
    path_reserved = 'reserved_words.json'
    path_code = 'codigo_teste.txt'
    show_correct_word = False
    path_log = None

    argParser = argparse.ArgumentParser()
    argParser.add_argument("-r", "--reserved", help="reserved words, json file")
    argParser.add_argument("-c", "--code", help="source code")
    argParser.add_argument("-s", "--show", help="show correct words")
    argParser.add_argument("-l", "--log", help="path to log file")
    args = argParser.parse_args()
    
    if args.reserved:
        path_reserved = args.reserved
    
    if args.code:
        path_code = args.code

    if args.show:
        show_correct_word = args.show.lower() == 'true'

    if args.log:
        path_log = args.log

    reserved = fetch_reserved_words(path_reserved)
    source_code = fetch_source_code(path_code)

    lexic_analyse(reserved, source_code, print_correct=show_correct_word, path_log=path_log)


if __name__ == '__main__':
    main()