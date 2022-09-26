from banco.conexao_sql import Conexao
from classes.paciente import Paciente

class Comandos:
    #comando para adicionar na tabela de pacientes
    def __init__(self):
        self.conexao = Conexao().conexao.cursor()

    def add_paciente(self,paciente=Paciente):
        comando = f"INSERT INTO pacientes(nome,email,senha,endereco,sexo,idade,tipo_sangue)\
        VALUES('{paciente.getNome()}','{paciente.getEmail()}','{paciente.getSenha()}','{paciente.getEndereco()}',\
        '{paciente.getSexo()}',{paciente.getIdade()},'{paciente.getTipoSangue()}');"

        self.conexao.execute(comando)
        self.conexao.commit()

    # comando para adicionar na tabela de secretarias
    #     
