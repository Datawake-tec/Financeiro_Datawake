import pyodbc


class Bank:

    def __init__(self, name):
        self.name = name
        self.connection = None

    def bank_connection(self, user, password, server, data_base):
        """
        Conexao com o banco de dados

        :param user: Usuario do banco
        :param password: senha do banco
        :param server: servidor aonde o banco esta alocado
        :param data_base: Nome do banco de dados
        :return: retorna a conexão ou None
        """
        if self.connection is not None:
            raise Exception('Você ja esta conectado com o banco de dados')
        try:
            con = pyodbc.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                                 f"SERVER={server};DATABASE={data_base};"
                                 f"UID={user};PWD={password}")
            self.connection = con
            print(f'Conexão com o banco {self.name} realizada com sucesso!')
            return self.connection
        except Exception as error_connection_bank:
            print(f'Erro ao conectar com o banco de dados {self.name}: {error_connection_bank}')
            return None

    def execution_query(self, query, parameters=None):
        """
            Executar consulta no banco

            :param query: A consulta que deseja realizar no banco de dados;
            :param parameters: Parametros da consulta, opcional;
            :return: Retorna os valores da consulta.
        """
        if self.connection is None:
            raise Exception("Conexão com o banco de dados nao esta aberta.")
        try:
            with self.connection.cursor() as cursor:
                if parameters:
                    cursor.execute(query, parameters)
                else:
                    cursor.execute(query)
                return cursor.fetchall()
        except Exception as error_query:
            print(f'Erro ao executar a consulta no banco {self.name}: {error_query}')

    def close_bank_connection(self):
        """
            Fecha a conexao com o banco

            :return: None
        """
        if self.connection:
            self.connection.close()
            print(f'Conexão com o banco de dados {self.name} fechada.')
