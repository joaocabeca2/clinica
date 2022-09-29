from tkinter import *
from turtle import left
from classes.paciente import Paciente
class Tela_paciente:
    def __init__(self,paciente=Paciente):
        self.paciente = paciente
        self.janela_paciente = Tk()
        #lista com medido e seu horario de disponibilidade
        Label(self.janela_paciente,text=f"Nome: {self.paciente.getNome()}",justify=LEFT).grid()
        Label(self.janela_paciente,text=f"Email: {self.paciente.getEmail()}",justify=LEFT).grid()
        Label(self.janela_paciente,text=f"Endereço: {self.paciente.getEndereco()}",justify=LEFT).grid()
        Label(self.janela_paciente,text=f"Sexo: {self.paciente.getSexo()}",justify=RIGHT).grid()
        Label(self.janela_paciente,text=f"Idade: {self.paciente.getIdade()}",justify=RIGHT).grid()
        Label(self.janela_paciente,text=f"Data de Inscrição: {self.paciente.getDataInscricao()}",justify=RIGHT).grid()

        Label(self.janela_paciente,text="Descreva o motivo do porque deseja consultar na clinica:",padx=10,pady=10).grid()

        Text(self.janela_paciente,width=40,height=10).grid()
        Button(self.janela_paciente,text="Agendar consulta",command='').grid()
        Button(self.janela_paciente,text="Deslogar",command=self.deslogar).grid()

        janela_paciente = mainloop()

    def deslogar(self):
        self.janela_paciente.destroy()
    
    #def agendar_consulta(self):
    
    #def agendar_consulta(self):

