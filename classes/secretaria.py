from usuario import Usuario
class Secretaria(Usuario):
    def __init__(self,nome,email,senha,endereco,sexo,cargo):
        super().__init__(nome,email,senha,endereco,sexo)
        self.cargo = cargo
        self.lista_agendamentos = []

    #todo agendamento que o paciente fizer pelo site vai ir para uma lista que será devidamente agendada pela secretaria
    #def agendar_consulta(self):

    #def alterar_dados_paciente(self,paciente)
