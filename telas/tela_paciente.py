from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from classes.medico import Medico
from classes.paciente import Paciente
from classes.agendamento import Agendamento
from banco.alterar_tabela import Comandos
from datetime import date

class Tela_paciente:
    def __init__(self,paciente=Paciente,doutor=Medico):
        self.doutor =  Medico()
        self.paciente = paciente
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
        self.motivo_consulta = Text(self.janela_paciente,width=40,height=10)
        self.motivo_consulta.grid()

        Label(self.janela_paciente,text="Dia do mês").grid()
        self.dia = ttk.Combobox(self.janela_paciente,values=self.doutor.getDiaAtendimento())
        self.dia.grid()

        Label(self.janela_paciente,text="Horario de Atendimneto").grid()
        self.horario = ttk.Combobox(self.janela_paciente,values=self.doutor.listar_horarios())
        self.horario.grid()

        Button(self.janela_paciente,text="Agendar consulta",command=self.agendar_consulta).grid()
        Button(self.janela_paciente,text="Deslogar",command=self.deslogar).grid()

        janela_paciente = mainloop()

    def deslogar(self):
        self.janela_paciente.destroy()
    
    def agendar_consulta(self):
        comando = Comandos()
        #so posso agendar consulta se naoo houver uma ja marcada, mas pode solicitar agendamento de quantas quiser
        if not self.paciente.isConsultaAgendada():
            try:
                agendamento = Agendamento(self.dia.get(),date.today(),self.horario.get(),self.motivo_consulta.get(1.0,END),self.paciente)
                comando.add_agendamento(agendamento)
                messagebox.showinfo("Agendamento","Solicitação de agendamento feito!")
                #a coluna boolean no sql esta como string entao ...
                self.paciente.setConsultaAgendada(True)
                comando.alterar_status_agendamento(False)
            except(Exception):
                messagebox.showwarning("Agendamento","algum campo está vazio ou com valores errados")
        else:
            messagebox.showwarning("Agendamento","Você já possui uma consulta marcada com a Dr")
            

