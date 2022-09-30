#from classes.paciente import Paciente
from classes.medico import Medico
class Agendamento:
    def __init__(self,data_consulta,data_marcacao,hora_consulta,motivo_consulta,doutor=Medico):
        self.data_consulta = data_consulta
        self.data_marcacao = data_marcacao
        self.hora_consulta = hora_consulta
        self.motivo_consulta = motivo_consulta
    
    def getDataConsulta(self):
        return self.data_consulta
    def setDataConsulta(self,data_consulta):
        self.data_consulta = data_consulta

    def getDatamarcacao(self):
        return self.data_marcacao
    def setDatamarcao(self,data_marcacao):
        self.data_marcacao = data_marcacao
        
    def getHoraConsulta(self):
        return self.hora_consulta
    def setHoraConsulta(self,hora_consulta):
        self.hora_consulta = hora_consulta

    def getMotivoConsulta(self):
        return self.motivo_consulta
    def setMotivoConsulta(self,motivo_consulta):
        self.motivo_consulta = motivo_consulta
    


