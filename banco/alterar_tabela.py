from conexao_sql import Conexao
from classes.paciente import Paciente

class Comandos:
    #comando para adicionar na tabela de pacientes
    def __init__(self):
        self.conexao = Conexao().conexao.cursor()

    def add_paciente(self,paciente=Paciente):
        comando = f"INSERT INTO pacientes(nome,email,senha,endereco,sexo,tipo_sangue)\
        VALUES({0},{paciente.getNome},{paciente.getEmail},{paciente.getSenha},{paciente.getEndereco},\
        {paciente.getSexo},{paciente.getTipoSangue})"

    # comando para adicionar na tabela de secretarias
    #     
