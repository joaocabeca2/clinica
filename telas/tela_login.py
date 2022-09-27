from tkinter import *
from tkinter import messagebox
from banco.alterar_tabela import Comandos
from classes.paciente import Paciente
class Tela_login:
    def __init__(self):
        self.paciente = None
        janela_login = Tk()
        Label(janela_login,text="Digite seu email").grid(column=0,row=0)
        self.email_input = Entry(janela_login,justify=CENTER)
        self.email_input.grid(column=0,row=1)

        Label(janela_login,text="Digite sua senha").grid(column=0,row=2)
        self.senha_input = Entry(janela_login,justify=CENTER,show="*")
        self.senha_input.grid(column=0,row=3)

        botao_login = Button(janela_login,text="Entrar",command=self.validar_email)
        botao_login.grid(column=0,row=4)
        janela_login.mainloop()

    def validar_email(self):
        comando = Comandos()
        #pegando a tupla da consulta feita de acordo com email e senha
        paciente = comando.consultar_paciente()[0]
        if paciente != []:
            self.paciente = Paciente(paciente[1],paciente[2],paciente[3],paciente[4],paciente[5],paciente[6],paciente[7])
        else:
            messagebox.showinfo("Entrar", "Erro ao tentar realizar o login, tente novamente!")

