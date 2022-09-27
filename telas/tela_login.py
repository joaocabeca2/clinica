from tkinter import *
from banco.alterar_tabela import Comandos
class Tela_login:
    def __init__(self):
        janela_login = Tk()
        Label(janela_login,text="Digite seu email").grid(column=0,row=0)
        self.email_input = Entry(janela_login,justify=CENTER)
        self.email_input.grid(column=0,row=1)

        Label(janela_login,text="Digite sua senha").grid(column=0,row=2)
        self.senha_input = Entry(janela_login,justify=CENTER,show="*")
        self.senha_input.grid(column=0,row=3)

        botao_login = Button(janela_login,text="Entrar",command=)
        botao_login.grid(column=0,row=4)
        janela_login.mainloop()

        def validar_email(self):
            comando = Comandos()
            

