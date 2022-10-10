from tkinter import *
from tkinter import messagebox
from banco.alterar_tabela import Comandos
from classes.paciente import Paciente
from tela_paciente import Tela_paciente
from tela_admin import Tela_admin

class Tela_login:
    def __init__(self):
        self.paciente = None
        self.janela_login = Tk()
        self.janela_login.title("Login")
        Label(self.janela_login,text="Email").grid(column=0,row=0,sticky=E)
        self.email_input = Entry(self.janela_login,justify=CENTER)
        self.email_input.grid(column=1,row=0)

        Label(self.janela_login,text="Senha").grid(column=0,row=2,sticky=E)
        self.senha_input = Entry(self.janela_login,justify=CENTER,show="*")
        self.senha_input.grid(column=1,row=2)

        botao_login = Button(self.janela_login,text="Entrar",command=self.entrar_tela_paciente)
        botao_login.grid(column=1,row=3,pady=5,padx=0)
        self.janela_login.mainloop()

    def validar_email(self):
        comando = Comandos()
        #pegando a tupla da consulta feita de acordo com email e senha
        try:
            paciente = comando.consultar_paciente(self.email_input.get(),self.senha_input.get())[0]
            self.paciente = Paciente(paciente[0],paciente[1],paciente[2],paciente[3],paciente[4],paciente[5],paciente[6],paciente[7],paciente[8])
            return True
        except(Exception):
            messagebox.showwarning("Entrar", "Erro ao tentar realizar o login, email ou senha incorretos!")
            self.reiniciar_tela_login()

    def verificar_admin(self):
        return self.email_input.get() == "admin" and self.senha_input.get() == "admin"

    def entrar_tela_paciente(self):
        if self.verificar_admin():
            self.janela_login.destroy()
            Tela_admin()
        
        else: 
            self.validar_email()
            self.janela_login.destroy()
            Tela_paciente(self.paciente)  
    
    def reiniciar_tela_login(self):
        self.janela_login.destroy()
        Tela_login()
            

