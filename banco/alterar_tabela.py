from banco.conexao_sql import Conexao
from classes.paciente import Paciente

class Comandos:
    #comando para adicionar na tabela de pacientes
    def __init__(self):
        self.conexao = Conexao().conexao.cursor()

    def add_paciente(self,paciente=Paciente):
        comando = f"INSERT INTO pacientes(nome,email,senha,endereco,sexo,idade,tipo_sangue,data_inscricao)\
        VALUES('{paciente.getNome()}','{paciente.getEmail()}','{paciente.getSenha()}','{paciente.getEndereco()}',\
        '{paciente.getSexo()}',{paciente.getIdade()},'{paciente.getTipoSangue()}','{paciente.getDataInscricao()}');"

        self.conexao.execute(comando)
        self.conexao.commit()

    def consultar_email(self):
        comando = "SELECT email FROM pacientes"
        self.conexao.execute(comando)
        return self.conexao.fetchall()


    def consultar_senha(self,email):
        #essa conculta é para retornar sómente um elemento pois nao pode haver mais de um cadastro com o mesmo email
        comando = f"SELECT senha FROM pacientes WHERE email = '{email}'"
        self.conexao.execute(comando)
        return self.conexao.fetchall()
    
    def consultar_paciente(self,email,senha):
        comando = f"SELECT * FROM pacientes WHERE email = '{email}' AND senha = '{senha}'"
        self.conexao.execute(comando)
        return self.conexao.fetchall()
    
    def consultar_medico(self):
        comando = "SELECT * FROM medicos"
        self.conexao.execute(comando)
        return self.conexao.fetchall()

    # comando para adicionar na tabela de secretarias
    #     
