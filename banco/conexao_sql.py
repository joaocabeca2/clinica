import pyodbc

class Conexao:
    def __init__(self):
        self.dados = (
            "Driver={SQL Server};"
            "Server=DESKTOP-55696US\SQLEXPRESS;"
            "Database=clinica_medica;"
        )
        self.conexao = pyodbc.connect(self.dados)


