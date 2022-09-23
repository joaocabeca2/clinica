from tkinter import *
from classes.paciente import Paciente
class Tela_paciente:
    def __init__(self):
        janela_paciente = Tk()
        #lista com medido e seu horario de disponibilidade
        agendar_button = Button(janela_paciente,text="Agendar consulta",command='').grid(column=0,row=0)
        deslogar_button = Button(janela_paciente,text="Deslogar",command='').grid(column=0,row=1)

        janela_paciente = mainloop()