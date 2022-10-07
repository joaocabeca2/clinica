from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from banco.alterar_tabela import Comandos
from classes.agendamento import Agendamento

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
        self.agendamentos.column("Status Consulta",anchor=W,width=180)

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
        self.add_dados_tabela()

        Button(self.janela_admin,text="Confirmar Agendamento",command=self.pegar_item_selecionado).grid()
        self.janela_admin.mainloop()

    def add_dados_tabela(self): 
        #adicionando dados
        self.comando = Comandos()
        all_agendamentos = self.comando.consultar_agendamentos()
        count = 0
        for agendamento in all_agendamentos:
            self.agendamentos.insert(parent="",index="end",iid=count,text="",values=(agendamento[0],agendamento[1],agendamento[2],agendamento[3],agendamento[4],agendamento[5],agendamento[6]))
            count += 1
        self.agendamentos.grid()
    
    def pegar_item_selecionado(self):
        #pegando item selecionado da tabela
        item_selecionado = self.agendamentos.focus()
        item_selecionado = self.agendamentos.item(item_selecionado)
        id_agendamento = item_selecionado.get("values")[0]
        id_paciente = item_selecionado.get("values")[1]
        agendamento = self.comando.consultar_agendamento_especifico(id_agendamento)[0]

        #deletando agendamento com antigo status
        self.comando.deletar_agendamento(id_agendamento)

        #adicionando mesmo agendamento, porem com status alterado
        novo_agendamento = Agendamento(agendamento[0],agendamento[1],agendamento[2],agendamento[3],agendamento[4],agendamento[5],True)
        self.comando.add_agendamento_gambiarra(novo_agendamento,id_paciente)
        messagebox.showinfo("Agendamneto","Consulta confirmada com sucesso!")
        self.reininicar_tabela()
    
    def reininicar_tabela(self):
        self.janela_admin.destroy()
        Tela_admin()

