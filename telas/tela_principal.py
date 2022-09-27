from tkinter import *
from tela_login import Tela_login
from tela_cadastro import Tela_cadastro

class Tela_principal:
    def __init__(self):
        #criar a janela
        janela_principal = Tk()
        janela_principal.geometry('500x500')
        janela_principal.title('Clinica JP')
        Button(janela_principal,text="Entrar",command=lambda: Tela_login()).grid(column=0,row=0,padx=50,pady=50)
        Button(janela_principal,text="Cadastrar",command=lambda: Tela_cadastro()).grid(column=10,row=0,padx=50,pady=50)

        #para a janela permanecer aberta
        janela_principal.mainloop()

    

tela = Tela_principal()
