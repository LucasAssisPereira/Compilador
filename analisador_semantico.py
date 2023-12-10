class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_variable(self, name, data_type):
        if name in self.symbols:
            raise Exception(f"Erro semântico: Variável '{name}' já declarada.")
        self.symbols[name] = data_type

    def get_variable_type(self, name):
        return self.symbols.get(name, None)


class Semantico:
    def __init__(self):
        self.symbol_table = SymbolTable()

    def analyze(self, ast):
        self.visit(ast)
        print("Tabela de Símbolos:")
        for var_name, var_type in self.symbol_table.symbols.items():
            print(f"{var_name}: {var_type}")

    def visit(self, node):
        method_name = f'visit_{node[0]}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        for child in node[1:]:
            self.visit(child)

    def visit_program(self, node):
        self.visit(node[5])  # Visitando o bloco

    def visit_block(self, node):
        for declaration in node[1]:
            self.visit(declaration)
        self.visit(node[3])  # Visitando o compound_statement

    def visit_vardeclaration(self, node):
        data_type = node[3][1]
        for variable in node[1]:
            var_name = variable[1]
            if self.symbol_table.get_variable_type(var_name) is not None:
                raise Exception(f"Erro semântico: Variável '{var_name}' já declarada.")
            self.symbol_table.add_variable(var_name, data_type)

    def visit_Assignment(self, node):
        var_name = node[1][1]
        print(f"Tentando analisar atribuição para a variável '{var_name}'...")

        try:
            # Adicionando variável à tabela de símbolos
            if var_name not in self.symbol_table.symbols:
                self.symbol_table.add_variable(var_name, 'INTEGER')

            var_type = self.symbol_table.get_variable_type(var_name)
            if var_type is None:
                raise Exception(f"Erro semântico: Variável '{var_name}' não declarada.")

            print(f"Tipo da variável '{var_name}': {var_type}")

            expr_type = self.visit(node[3])  # Visitando a expressão
            print(f"Tipo da expressão: {expr_type}")

            if var_type != expr_type:
                raise Exception(f"Erro semântico: Atribuição inválida para variável '{var_name}'.")
            print(f"Atribuição válida: {var_name} := {expr_type}")

        except Exception as e:
            print(f"Erro semântico durante a análise da atribuição: {e}")
            raise  # Re-raise a exceção para que ela seja capturada no código de teste

    def visit_binop(self, node):
        left_type = self.visit(node[1])  # Visitando o nó à esquerda
        right_type = self.visit(node[3])  # Visitando o nó à direita

        if node[2][0] in {'PLUS', 'MINUS', 'TIMES', 'DIVIDE'}:
            if left_type == right_type == 'INTEGER':
                return 'INTEGER'
            else:
                raise Exception("Erro semântico: Operação aritmética inválida.")

    def visit_num(self, node):
        return 'INTEGER'