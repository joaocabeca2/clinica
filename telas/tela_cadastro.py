from tkinter import *
from banco.alterar_tabela import Comandos
from classes.paciente import Paciente

class Tela_cadastro:
    def __init__(self):
        janela_principal = Tk()
        self.nome_label = Label(janela_principal,text="Digite seu nome").grid(column=0,row=0)
        self.nome_input = Entry(janela_principal,justify=CENTER).grid(column=0,row=1)

        self.email_label = Label(janela_principal,text="Digite seu email").grid(column=0,row=2)
        self.email_input = Entry(janela_principal,justify=CENTER).grid(column=0,row=3)

        self.senha_label = Label(janela_principal,text="Digite sua senha").grid(column=0,row=4)
        self.senha_input = Entry(janela_principal,justify=CENTER).grid(column=0,row=5)

        self.idade_label = Label(janela_principal,text="Digite sua idade").grid(column=50,row=0)
        self.idade_input = Entry(janela_principal,justify=CENTER).grid(column=50,row=1)

        self.sexo_label = Label(janela_principal,text="Digite seu sexo").grid(column=50,row=1)
        self.sexo_input = Entry(janela_principal,justify=CENTER).grid(column=50,row=2)

        self.endereco_label = Label(janela_principal,text="Digite seu endereço").grid(column=50,row=3)
        self.endereco_input = Entry(janela_principal,justify=CENTER).grid(column=50,row=4)

        #caixa com opçoes do tipo sanguineo para marcar check

        register_button= Button(janela_principal,text="Register",command=self.registration_suscefully_message if self.autenticar_email(email_input) and self.autenticar_senha(senha_input) else self.mostrar_erro)
        register_button.grid(column=50,row=4)

        janela_principal.mainloop()
    
    def autenticar_email(self,email):
        email = str(email)
        #if existe email no banco
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
        self.nome_input = str(self.nome_input)
        self.email = str(self.email_input)
        self.senha = str(self.senha_input)
        self.idade = int(self.idade_input)
        self.endereco = str(self.endereco)
        self.sexo = str(self.sexo)

    def cadastrar_usuario(self):
        return Paciente(self.nome_input,self.email_input,self.senha_input,self.idade_input,self.endereco_input,self.sexo,"A+")

    def registration_suscefully_message(self):
        self.converter_valores()
        paciente  = self.cadastrar_usuario()
        #cadastrar_paciente = Comandos()
        #cadastrar_paciente.add_paciente(paciente)
        registration_suscefully_window = Tk()
        Label(registration_suscefully_window,text="Cadastro realizado com sucesso!").grid(column=0,row=0)
        