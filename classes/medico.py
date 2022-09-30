class Medico:
    def __init__(self):
        self.doutor = "joaocabeca"
        self.dia_atendimento = []
        self.horario_atendimento = "08 ás 17"

    def getDoutor(self):
        return self.doutor
    def getDiaAtendimento(self):
        return self.dia_atendimento
    def getHorarioAtendimento(self):
        return self.horario_atendimento
    

    def listar_horarios(self):
        lista = self.horario_atendimento.split(" ")
        inicio = int(lista[0])
        final = int(lista[-1])
        #de meia em meia hora
        hora_consulta = inicio
        lista = [str(inicio)+":"+"00"]
        while hora_consulta < final:
            lista.append(str(hora_consulta)+":"+"30")
            hora_consulta += 1
            lista.append(str(hora_consulta)+":"+"00")
        return lista
    
    def listar_dias(self):
        #tirando os finais de semana

'''medico = Medico("j","a","a","a","a",56,"a")
print(medico.listar_horarios())  '''  