from agendamento import Agendamento
from medico import Medico
from usuario import Usuario
class Paciente(Usuario):
    def __init__(self,nome,email,senha,endereco,sexo,tipo_sangue):
        super().__init__(nome,email,senha,endereco,sexo)
        self.tipo_sangue = tipo_sangue
    
    def solicitar_consulta(self,doutor)
        return Agendamento(doutor)

    #def deslogar()