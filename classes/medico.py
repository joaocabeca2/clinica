from classes.usuario import Usuario
class Medico(Usuario):
    def __init__(self,nome,email,senha,endereco,sexo):
        super().__init__(nome,email,senha,endereco,sexo)
        self.horario_atendimento = []
    