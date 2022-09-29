from classes.agendamento import Agendamento
from classes.medico import Medico
from classes.usuario import Usuario
class Paciente(Usuario):
    def __init__(self,nome,email,senha,endereco,sexo,idade,tipo_sangue,data_inscricao):
        super().__init__(nome,email,senha,endereco,sexo,idade,data_inscricao)
        self.tipo_sangue = tipo_sangue
    
    def solicitar_consulta(self,doutor):
        return Agendamento(doutor)

    def getTipoSangue(self):
        return self.tipo_sangue
    
    