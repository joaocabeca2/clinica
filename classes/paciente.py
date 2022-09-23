from usuario import Usuario
class Paciente(Usuario):
    def __init__(self,nome,email,senha,endereco,tipo_sangue):
        super().__init__(nome,email,senha,endereco)
        self.tipo_sangue = tipo_sangue

    