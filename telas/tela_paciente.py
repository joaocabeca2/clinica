from tkinter import *
from tkinter import ttk
from classes.medico import Medico
from classes.paciente import Paciente
from classes.agendamento import Agendamento
from datetime import date
class Tela_paciente:
    def __init__(self,paciente=Paciente,doutor=Medico()):
        self.doutor = doutor
        self.paciente = paciente
        self.agendado = False
        self.janela_paciente = Tk()
        self.janela_paciente.geometry("500x500")
        #lista com medido e seu horario de disponibilidade
        Label(self.janela_paciente,text=f"Nome: {self.paciente.getNome()}",justify=LEFT).grid()
        Label(self.janela_paciente,text=f"Email: {self.paciente.getEmail()}",justify=LEFT).grid()
        Label(self.janela_paciente,text=f"Endereço: {self.paciente.getEndereco()}",justify=LEFT).grid()
        Label(self.janela_paciente,text=f"Sexo: {self.paciente.getSexo()}",justify=RIGHT).grid()
        Label(self.janela_paciente,text=f"Idade: {self.paciente.getIdade()}",justify=RIGHT).grid()
        #Label(self.janela_paciente,text=f"Data de Inscrição: {self.paciente.getDataInscricao()}",justify=RIGHT).grid()

        Label(self.janela_paciente,text="Descreva o motivo do porque deseja consultar na clinica:",padx=10,pady=10).grid()
        Text(self.janela_paciente,width=40,height=10).grid()

        Label(self.janela_paciente,text="Dia da semana").grid()
        self.dia = ttk.Combobox(self.janela_paciente,values=self.doutor.getDiaAtendimento())
        self.dia.grid()

        Label(self.janela_paciente,text="Horario de Atendimneto").grid()
        self.horario = ttk.Combobox(self.janela_paciente,values=self.doutor.listar_horarios())
        self.horario.grid()

        Button(self.janela_paciente,text="Agendar consulta",command='').grid()
        Button(self.janela_paciente,text="Deslogar",command=self.deslogar).grid()

        janela_paciente = mainloop()

    def deslogar(self):
        self.janela_paciente.destroy()
    
    def agendar_consulta(self):
        return Agendamento("data consulta",date.today(),"hora consulta","motivo")
    #def agendar_consulta(self):

