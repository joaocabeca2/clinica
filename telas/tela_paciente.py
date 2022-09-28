from tkinter import *
from classes.paciente import Paciente
class Tela_paciente:
    def __init__(self,paciente=Paciente):
        self.paciente = paciente
        self.janela_paciente = Tk()
        #lista com medido e seu horario de disponibilidade
        Button(self.janela_paciente,text="Agendar consulta",command='').grid(column=0,row=0)
        Button(self.janela_paciente,text="Deslogar",command=self.deslogar).grid(column=0,row=1)

        janela_paciente = mainloop()

    def deslogar(self):
        self.janela_paciente.destroy()
