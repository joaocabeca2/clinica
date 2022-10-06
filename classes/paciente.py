from classes.usuario import Usuario
class Paciente(Usuario):
    def __init__(self,id,nome,email,senha,endereco,sexo,idade,tipo_sangue,data_inscricao):
        super().__init__(id,nome,email,senha,endereco,sexo,idade,data_inscricao)
        self.tipo_sangue = tipo_sangue

    def getTipoSangue(self):
        return self.tipo_sangue
    def setTipoSangue(self,tipo_sangue):
        self.tipo_sangue = tipo_sangue



    
    