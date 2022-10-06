#from classes.paciente import Paciente
from classes.medico import Medico
from classes.paciente import Paciente
class Agendamento:
    def __init__(self,id,data_consulta,data_agendamento,hora_consulta,motivo_consulta,status_consulta,paciente=Paciente):
        self.id = id
        self.data_consulta = data_consulta
        self.data_marcacao = data_agendamento
        self.hora_consulta = hora_consulta
        self.motivo_consulta = motivo_consulta
        self.status_consulta = status_consulta
        self.paciente = paciente

    def getID(self):
        return self.id

    def getDataConsulta(self):
        return self.data_consulta
    def setDataConsulta(self,data_consulta):
        self.data_consulta = data_consulta

    def getDataAgendamento(self):
        return self.data_marcacao
    def setAgendamento(self,data_marcacao):
        self.data_marcacao = data_marcacao
        
    def getHoraConsulta(self):
        return self.hora_consulta
    def setHoraConsulta(self,hora_consulta):
        self.hora_consulta = hora_consulta

    def getMotivoConsulta(self):
        return self.motivo_consulta
    def setMotivoConsulta(self,motivo_consulta):
        self.motivo_consulta = motivo_consulta
    
    def getStatusConsulta(self):
        return self.status_consulta
    def setStatusConta(self,status):
        self.status_consulta = status
    
    def getPaciente(self):
        return self.paciente
    


