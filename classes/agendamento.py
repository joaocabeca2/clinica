from classes.usuario import Usuario
from classes.medico import Medico
class Agendamento:
    def __init__(self,doutor,motivo_consulta):
        self.data_consulta = None
        self.marcacao = None
        self.hora_consulta = None
        self.doutor = Medico()
        self.motivo_consulta = motivo_consulta
