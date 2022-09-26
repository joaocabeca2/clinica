from tkinter import *
from tkinter import Tk,ttk
from tkinter import messagebox
from banco.alterar_tabela import Comandos
from classes.paciente import Paciente

class Tela_cadastro:
    def __init__(self):
        janela_principal = Tk()
        self.nome_label = Label(janela_principal,text="Digite seu nome").grid(column=0,row=0)
        self.nome_input = Entry(janela_principal,justify=CENTER)
        self.nome_input.grid(column=0,row=1)

        self.email_label = Label(janela_principal,text="Digite seu email").grid(column=0,row=2)
        self.email_input = Entry(janela_principal,justify=CENTER)
        self.email_input.grid(column=0,row=3)

        self.senha_label = Label(janela_principal,text="Digite sua senha").grid(column=0,row=4)
        self.senha_input = Entry(janela_principal,justify=CENTER,show="*")
        self.senha_input.grid(column=0,row=5)

        self.idade_label = Label(janela_principal,text="Digite sua idade").grid(column=50,row=0)
        self.idade_input = Entry(janela_principal,justify=CENTER)
        self.idade_input.grid(column=50,row=1)

        self.sexo_label = Label(janela_principal,text="Digite seu sexo").grid(column=50,row=2)
        self.sexo_input = Entry(janela_principal,justify=CENTER)
        self.sexo_input.grid(column=50,row=3)

        self.endereco_label = Label(janela_principal,text="Digite seu endereço").grid(column=50,row=4)
        self.endereco_input = Entry(janela_principal,justify=CENTER)
        self.endereco_input.grid(column=50,row=5)

        #caixa com opçoes do tipo sanguineo para marcar check

        register_button= Button(janela_principal,text="Register",command=self.concluir_registros if self.autenticar_email(self.email_input) and self.autenticar_senha(self.senha_input) else self.mostrar_erro)
        register_button.grid(column=50,row=10)

        janela_principal.mainloop()
    
    def autenticar_email(self,email):
        email = str(email)
        #if existe email no banc"""  """o
            #self.mostrar_erro()
        #else adiciona novo paciente
        return True
    
    def autenticar_senha(self,password):
        password = str(password)
        return True
        '''if password.isdigit():
            return True'''
    
    def mostrar_erro(self):
        janela_erro = Tk()
        Label(janela_erro,text="Erro na validação de dados, tente novamente!").grid(column=0,row=0)
        janela_erro.mainloop()

    def converter_valores(self):
        self.nome_input = self.nome_input.get()
        self.email_input = self.email_input.get()
        self.senha_input = self.senha_input.get()
        self.endereco_input = self.endereco_input.get()
        self.sexo_input = self.sexo_input.get()
        self.idade_input = int(self.idade_input.get())

    def cadastrar_usuario(self):
        return Paciente(self.nome_input,self.email_input,self.senha_input,self.endereco_input,self.sexo_input,self.idade_input,"A+")
    
    def inserir_paciente_banco(self):
        comando = Comandos()
        comando.add_paciente(self.cadastrar_usuario())
        messagebox.showinfo("Cadastro","Cadastro realizado com sucesso")

    def concluir_registros(self):
        self.converter_valores()
        self.inserir_paciente_banco()
        