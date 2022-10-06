from tkinter import *
from tkinter import ttk
from banco.alterar_tabela import Comandos

class Tela_admin:
    def __init__(self):
        self.janela_admin = Tk()
        self.janela_admin.title("Administração")
        #self.janela_admin.geometry("500x500")

        #definindo colunas
        self.agendamentos = ttk.Treeview(self.janela_admin)
        self.agendamentos["columns"] = ("ID Agendamento","ID Paciente","Data Consulta","Data Agendamento","Hora Consulta","Motivo","Status Consulta")

        #formatando colunas
        self.agendamentos.column("#0",width=0,stretch=NO)
        self.agendamentos.column("ID Agendamento",anchor=W,width=120)
        self.agendamentos.column("ID Paciente",anchor=CENTER,width=120)
        self.agendamentos.column("Data Consulta",anchor=W,width=120)
        self.agendamentos.column("Data Agendamento",anchor=W,width=120)
        self.agendamentos.column("Hora Consulta",anchor=W,width=120)
        self.agendamentos.column("Motivo",anchor=W,width=120)
        self.agendamentos.column("Status Consulta",anchor=W,width=120)

        #criando headings
        self.agendamentos.heading("#0",text="",anchor=W)
        self.agendamentos.heading("ID Agendamento",anchor=W,text="ID Agendamento")
        self.agendamentos.heading("ID Paciente",anchor=CENTER,text="ID Paciente")
        self.agendamentos.heading("Data Consulta",anchor=W,text="Data Consulta")
        self.agendamentos.heading("Data Agendamento",anchor=W,text="Data Agendamento")
        self.agendamentos.heading("Hora Consulta",anchor=W,text="Hora Consulta")
        self.agendamentos.heading("Motivo",anchor=W,text="Motivo")
        self.agendamentos.heading("Status Consulta",anchor=W,text="Status Consulta")

        #adicionando dados
        comando = Comandos()
        all_agendamentos = comando.consultar_agendamentos()
        count = 0
        for agendamento in all_agendamentos:
            self.agendamentos.insert(parent="",index="end",iid=count,text="",values=(agendamento[0],agendamento[1],agendamento[2],agendamento[3],agendamento[4],agendamento[5],agendamento[6]))
            count += 1
        self.agendamentos.grid()
        self.janela_admin.mainloop()

