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
        self.janela_paciente.title(f"Bem vindo {self.paciente.getNome().capitalize()}")

        #definindo colunas
        self.info_paciente = ttk.Treeview(self.janela_paciente)
        self.info_paciente["columns"] = ("Nome","Email","Endereço","Sexo","Idade","Tipo Sanguineo")

        #formatando colunas
        self.info_paciente.column("#0",width=0,stretch=NO)
        self.info_paciente.column("Nome",anchor=W,width=80)
        self.info_paciente.column("Email",anchor=W,width=200)
        self.info_paciente.column("Endereço",anchor=W,width=200)
        self.info_paciente.column("Sexo",anchor=W,width=80)
        self.info_paciente.column("Idade",anchor=W,width=40)
        self.info_paciente.column("Tipo Sanguineo",anchor=W,width=40)

        #criando headings
        self.info_paciente.heading("#0",text="",anchor=W)
        self.info_paciente.heading("Nome",anchor=W,text="Nome")
        self.info_paciente.heading("Email",anchor=CENTER,text="Email")
        self.info_paciente.heading("Endereço",anchor=W,text="Endereço")
        self.info_paciente.heading("Sexo",anchor=W,text="Sexo")
        self.info_paciente.heading("Idade",anchor=W,text="Idade")
        self.info_paciente.heading("Tipo Sanguineo",anchor=W,text="Tipo Sanguineo")

        #adicionando dados
        self.add_dados_tabela()

        Label(self.janela_paciente,text="Motivo da Consulta:",padx=10,pady=10).grid()
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
        self.janela_paciente.mainloop()

    def deslogar(self):
        self.janela_paciente.destroy()
    
    def agendar_consulta(self):
        comando = Comandos()
        #so posso agendar consulta se naoo houver uma ja marcada, mas pode solicitar agendamento de quantas quiser
        id = comando.consultar_quantidade_agendamentos()[0][0] + 1
        try:
            agendamento = Agendamento(id,self.dia.get(),date.today(),self.horario.get(),self.motivo_consulta.get(1.0,END),False,self.paciente)
            comando.add_agendamento(agendamento,self.paciente)
            messagebox.showinfo("Agendamento","Solicitação de agendamento feito!")
            #a coluna boolean no sql esta como string entao ...
        except(Exception):
            messagebox.showwarning("Agendamento","algum campo está vazio ou com valores errados")
    
    def add_dados_tabela(self):
        comando = Comandos()
        paciente = comando.consultar_paciente(self.paciente.getEmail(),self.paciente.getSenha())[0]

        for x in range(len(paciente)):
            if type(paciente[x])==str and x!=2:
                paciente[x] = paciente[x].capitalize()
        self.info_paciente.insert(parent="",index="end",text="",values=(paciente[1],paciente[2],paciente[4],paciente[5],paciente[6],paciente[7]))
        self.info_paciente.grid()
            

