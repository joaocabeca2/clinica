from tkinter import *
from tela_login import Tela_login
from tela_cadastro import Tela_cadastro

class Tela_principal:
    def __init__(self):
        #criar a janela
        window = Tk()
        window.geometry('500x500')
        window.title('Clinica JP')
        login_buttom = Button(window,text="Login",command=lambda: Tela_login()).grid(column=0,row=0,padx=50,pady=50)
        register_buttom = Button(window,text="Register",command=lambda: Tela_cadastro()).grid(column=10,row=0,padx=50,pady=50)

        #para a janela permanecer aberta
        window.mainloop()

    

tela = Tela_principal()
