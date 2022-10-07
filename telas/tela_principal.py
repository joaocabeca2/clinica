from tkinter import *
from tela_login import Tela_login
from tela_cadastro import Tela_cadastro

class Tela_principal:
    def __init__(self):
        #criar a janela
        self.janela_principal = Tk()
        self.janela_principal.geometry('500x500')
        self.janela_principal.title('Clinica')
        Button(self.janela_principal,text="Entrar",command=lambda: Tela_login()).grid(column=0,row=10)
        Button(self.janela_principal,text="Cadastrar",command=lambda: Tela_cadastro()).grid(column=,row=10)
        Button(self.janela_principal,text="Sair",command=self.janela_principal.destroy).grid(column=5,row=20)

        #para a janela permanecer aberta
        self.janela_principal.mainloop()

tela = Tela_principal()

