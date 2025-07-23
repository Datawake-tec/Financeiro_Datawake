import sqlite3


class LocalBank:

    def __init__(self, name):
        self.name = name
        self.connection = None

    def connection(self):
        """
        Conexao com o banco de dados

        :return: Retorna a conexão com o banco
        """
        if self.connection is not None:
            raise Exception('Você ja esta conectado com o banco de dados')
        try:
            self.connection = sqlite3.connect(self.name)
            print(f"Conexão ao banco de dados {self.name} estabelecida com sucesso.")
            return self.connection
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados {self.name}: {e}")
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

    def close(self):
        """
        Fecha a conexao com o banco

        :return: None
        """
        if self.connection:
            self.connection.close()
            print(f"Conexão ao banco de dados {self.name} fechada.")
