from logging import exception
from tkinter import E
import pyodbc

class Conexao:
    def __init__(self):
        self.dados = (
            "Driver={SQL Server};"
            "Server=ETR65798\SQLEXPRESS;"
            "Database=clinica_medica;"
        )
        try:
            self.conexao = pyodbc.connect(self.dados)
        except(Exception):
            raise "Erro ao conectar no banco!"


