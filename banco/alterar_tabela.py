from banco.conexao_sql import Conexao
from classes.paciente import Paciente
from classes.agendamento import Agendamento

class Comandos:
    #comando para adicionar na tabela de pacientes
    def __init__(self):
        self.conexao = Conexao().conexao.cursor()

    def add_paciente(self,paciente=Paciente):
        comando = f"INSERT INTO pacientes(nome,email,senha,endereco,sexo,idade,tipo_sangue,data_inscricao,consulta_agendada)\
        VALUES('{paciente.getNome()}','{paciente.getEmail()}','{paciente.getSenha()}','{paciente.getEndereco()}',\
        '{paciente.getSexo()}',{paciente.getIdade()},'{paciente.getTipoSangue()}','{paciente.getDataInscricao()}','{str(paciente.isConsultaAgendada())}');"

        self.conexao.execute(comando)
        self.conexao.commit()
    
    def add_agendamento(self,agendamento=Agendamento):
        id_paciente = self.consultar_id_paciente(agendamento.getPaciente())[0][0]
        comando = f"INSERT INTO agendamentos(id_paciente,data_consulta,data_consulta_marcada,hora_consulta,motivo_consulta)\
            VALUES('{id_paciente}','{agendamento.getDataConsulta()}','{agendamento.getDataMarcacao()}',\
                '{agendamento.getHoraConsulta()}','{agendamento.getMotivoConsulta()}');"
        self.conexao.execute(comando)
        self.conexao.commit()
    
    def alterar_status_agendamento(self,status_consulta,id_paciente):
        comando = f"UPDATE pacientes SET consulta_agendada='{str(status_consulta)}'\
            WHERE id='{id_paciente}'"
        self.conexao.execute(comando)
        self.conexao.commit()
    
    def consultar_id_paciente(self,paciente=Paciente):
        comando = f"SELECT id FROM pacientes WHERE email = '{paciente.getEmail()}'"
        self.conexao.execute(comando)
        return self.conexao.fetchall()

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
    
    def consultar_agendamentos(self):
        comando = f"SELECT * FROM agendamentos"
        self.conexao.execute(comando)
        return self.conexao.fetchall()
    

    # comando para adicionar na tabela de secretarias
    #     
