from agendamento import Agendamento
from medico import Medico
from usuario import Usuario
class Paciente(Usuario):
    def __init__(self,nome,email,senha,endereco,sexo,tipo_sangue):
        super().__init__(nome,email,senha,endereco,sexo)
        self.tipo_sangue = tipo_sangue
    
    def solicitar_consulta(self,doutor):
        return Agendamento(doutor)

    def getNome(self):
        return self.nome
    def getEmail(self):
        return self.email
    def getSenha(self):
        return self.senha
    def getEndereco(self):
        return self.endereco
    def getSexo(self):
        return self.sexo
    def getTipoSangue(self):
        return self.tipo_sangue
    #def deslogar()