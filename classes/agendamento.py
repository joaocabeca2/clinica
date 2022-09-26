from classes.usuario import Usuario
from classes.medico import Medico
class Agendamento:
    def __init__(self,doutor):
        self.data_consulta = None
        self.marcacao = None
        self.hora_consulta = None
        self.doutor = Medico()
