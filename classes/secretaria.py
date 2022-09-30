from usuario import Usuario
from classes.agendamento import Agendamento

class Secretaria(Usuario):
    def __init__(self,nome,email,senha,endereco,sexo,idade,cargo,data_inscricao):
        super().__init__(nome,email,senha,endereco,sexo,idade,data_inscricao)
        self.cargo = cargo

    #todo agendamento que o paciente fizer pelo site vai ir para uma lista que será devidamente agendada pela secretaria
    #def agendar_consulta(self):

    #def alterar_dados_paciente(self,paciente)
