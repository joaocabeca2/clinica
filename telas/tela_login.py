from tkinter import *
from tkinter import messagebox
from banco.alterar_tabela import Comandos
from classes.paciente import Paciente
from tela_paciente import Tela_paciente

class Tela_login:
    def __init__(self):
        self.paciente = None
        self.janela_login = Tk()
        Label(self.janela_login,text="Digite seu email").grid(column=0,row=0)
        self.email_input = Entry(self.janela_login,justify=CENTER)
        self.email_input.grid(column=0,row=1)

        Label(self.janela_login,text="Digite sua senha").grid(column=0,row=2)
        self.senha_input = Entry(self.janela_login,justify=CENTER,show="*")
        self.senha_input.grid(column=0,row=3)

        botao_login = Button(self.janela_login,text="Entrar",command=self.entrar_tela_paciente)
        botao_login.grid(column=0,row=4)
        self.janela_login.mainloop()

    def validar_email(self):
        comando = Comandos()
        #pegando a tupla da consulta feita de acordo com email e senha
        paciente = comando.consultar_paciente(self.email_input.get(),self.senha_input.get())[0]
        if paciente != []:
            self.paciente = Paciente(paciente[1],paciente[2],paciente[3],paciente[4],paciente[5],paciente[6],paciente[7])
            return True
        else:
            messagebox.showinfo("Entrar", "Erro ao tentar realizar o login, tente novamente!")
            return False

    def entrar_tela_paciente(self):
        if self.validar_email():
            Tela_paciente(self.paciente)
            self.janela_login.destroy()

        else:
            messagebox.showinfo("Entrar", "Erro ao tentar realizar o login, tente novamente!")
            self.janela_login.destroy()
            

