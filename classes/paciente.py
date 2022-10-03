from classes.usuario import Usuario
class Paciente(Usuario):
    def __init__(self,nome,email,senha,endereco,sexo,idade,tipo_sangue,data_inscricao,consulta_agendada):
        super().__init__(nome,email,senha,endereco,sexo,idade,data_inscricao)
        self.consulta_agendada = consulta_agendada
        self.tipo_sangue = tipo_sangue

    def getTipoSangue(self):
        return self.tipo_sangue
    def setTipoSangue(self,tipo_sangue):
        self.tipo_sangue = tipo_sangue

    def isConsultaAgendada(self):
        return self.consulta_agendada
    def setConsultaAgendada(self,consulta_agendada):
        self.consulta_agendada = consulta_agendada


    
    