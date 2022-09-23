from urllib.parse import non_hierarchical
from medico import Medico
class Agendamento:
    def __init__(self,doutor):
        self.data_consulta = None
        self.marcacao = None
        self.hora_consulta = None
        self.doutor = Medico()
