from banco.conexao_sql import Conexao
from classes.paciente import Paciente
from classes.agendamento import Agendamento

class Comandos:
    #comando para adicionar na tabela de pacientes
    def __init__(self):
        self.conexao = Conexao().conexao.cursor()

    def add_paciente(self,paciente=Paciente):
        comando = f"INSERT INTO pacientes(id,nome,email,senha,endereco,sexo,idade,tipo_sangue,data_inscricao)\
        VALUES('{paciente.getID()}','{paciente.getNome()}','{paciente.getEmail()}','{paciente.getSenha()}','{paciente.getEndereco()}',\
        '{paciente.getSexo()}',{paciente.getIdade()},'{paciente.getTipoSangue()}','{paciente.getDataInscricao()}');"

        self.conexao.execute(comando)
        self.conexao.commit()
    
    def add_agendamento(self,agendamento=Agendamento,paciente=Paciente):
        status_consulta =  "Agendamento Confirmado" if agendamento.getStatusConsulta() else "Aguardando Confirmação"

        comando = f"INSERT INTO agendamentos(id,id_paciente,data_consulta,data_agendamento,hora_consulta,motivo_consulta,status_consulta)\
            VALUES('{agendamento.getID()}','{paciente.getID()}','{agendamento.getDataConsulta()}','{agendamento.getDataAgendamento()}',\
                '{agendamento.getHoraConsulta()}','{agendamento.getMotivoConsulta()}','{status_consulta}');"
        self.conexao.execute(comando)
        self.conexao.commit()
    
    def add_agendamento_gambiarra(self,agendamento=Agendamento,id_paciente=int):
        status_consulta =  "Agendamento Confirmado" if agendamento.getStatusConsulta() else "Aguardando Confirmação"

        comando = f"INSERT INTO agendamentos(id,id_paciente,data_consulta,data_agendamento,hora_consulta,motivo_consulta,status_consulta)\
            VALUES('{agendamento.getID()}','{id_paciente}','{agendamento.getDataConsulta()}','{agendamento.getDataAgendamento()}',\
                '{agendamento.getHoraConsulta()}','{agendamento.getMotivoConsulta()}','{status_consulta}');"
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
    
    def consultar_quantidade_pacientes(self):
        comando = "SELECT COUNT(*) FROM pacientes"
        self.conexao.execute(comando)
        return self.conexao.fetchall()
    
    def consultar_quantidade_agendamentos(self):
        comando = "SELECT COUNT(*) FROM agendamentos"
        self.conexao.execute(comando)
        return self.conexao.fetchall()
    
    def consultar_agendamentos(self):
        comando = "SELECT * FROM agendamentos"
        self.conexao.execute(comando)
        return self.conexao.fetchall()
    
    def consultar_agendamento_especifico(self,id_agendamento):
        comando = f"SELECT * FROM agendamentos WHERE id = '{id_agendamento}'"
        self.conexao.execute(comando)
        return self.conexao.fetchall()

    def deletar_agendamento(self,id):
        comando = f"DELETE FROM agendamentos WHERE id = '{id}'" 
        self.conexao.execute(comando)
        self.conexao.commit()
